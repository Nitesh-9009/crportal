from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .admin import SubmissionAdminForm
from .models import Submission, Task, TaskZero


class TaskSchedulingTests(TestCase):
    def test_availability_and_submission_before_publication(self):
        from datetime import timedelta
        from django.utils import timezone
        now = timezone.now()
        scheduled = Task.objects.create(title="Future task", description="Later", publish_at=now + timedelta(days=1))
        live = Task.objects.create(title="Live task", description="Now", publish_at=now - timedelta(minutes=1))
        immediate = Task.objects.create(title="Immediate", description="Now")
        expired = Task.objects.create(title="Expired", description="Closed", deadline=now - timedelta(minutes=1))
        self.assertSetEqual(set(Task.objects.available()), {live, immediate})
        user = User.objects.create_user(username="scheduled-test")
        self.client.force_login(user)
        response = self.client.get(reverse("tasks_page"))
        self.assertNotContains(response, "Future task")
        self.client.post(reverse("tasks_page"), {"task_id": scheduled.pk, "link": "https://example.com/proof"})
        self.assertFalse(Submission.objects.filter(task=scheduled).exists())
        scheduled.publish_at = now - timedelta(seconds=1)
        scheduled.save()
        self.assertIn(scheduled, Task.objects.available())

    def test_deadline_must_follow_publication(self):
        from django.core.exceptions import ValidationError
        from django.utils import timezone
        now = timezone.now()
        with self.assertRaises(ValidationError):
            Task(title="Invalid", description="Invalid", publish_at=now, deadline=now).full_clean()


class AdminOperationsTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="operations",
            email="operations@example.com",
            password="temporary-test-password",
        )
        self.participant = User.objects.create_user(
            username="participant",
            email="participant@example.com",
        )
        self.task = Task.objects.create(
            title="Campus outreach",
            description="Document the outreach activity.",
            points=100,
        )
        self.submission = Submission.objects.create(
            task=self.task,
            user=self.participant,
            link="https://example.com/proof",
        )
        self.client.force_login(self.admin)

    def test_admin_dashboard_prioritises_review_workflow(self):
        response = self.client.get(reverse("admin:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Manage tasks, reviews and points.")
        self.assertContains(response, "Review pending submissions")
        self.assertContains(response, "Awaiting review")

    def test_submission_queue_renders_scoring_controls(self):
        response = self.client.get(reverse("admin:aakarapp_submission_changelist"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Open link")
        self.assertContains(response, "Pending")
        self.assertContains(response, "Maximum")

    def test_submission_form_rejects_score_above_task_maximum(self):
        form = SubmissionAdminForm(
            data={
                "task": self.task.pk,
                "user": self.participant.pk,
                "link": "https://example.com/proof",
                "marks": 101,
                "graded": True,
            },
            instance=self.submission,
        )

        self.assertFalse(form.is_valid())
        self.assertIn("worth 100 points", form.errors["marks"][0])

    def test_full_points_action_updates_score_and_review_state(self):
        response = self.client.post(
            reverse("admin:aakarapp_submission_changelist"),
            {
                "action": "award_full_points",
                "_selected_action": [self.submission.pk],
                "index": 0,
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.submission.refresh_from_db()
        self.assertEqual(self.submission.marks, 100)
        self.assertTrue(self.submission.graded)


class ParticipantAvatarTests(TestCase):
    def setUp(self):
        self.participant = User.objects.create_user(
            username="diva",
            email="diva@example.com",
            password="participant-test-password",
            first_name="Diva",
        )
        self.profile = TaskZero.objects.create(
            crid="AK250002",
            names="Diva Agrawal",
            username="diva",
            email="diva@example.com",
            emails="diva@example.com",
            colgName="IIT Bombay",
            state="Maharashtra",
            city="Mumbai",
            mobileNo="9999999999",
            dept="Civil Engineering",
            whatsappNo="9999999999",
            pincode="400076",
            address="Powai",
            avatar="fox",
        )
        self.client.force_login(self.participant)

    def test_dashboard_uses_avatar_without_decorative_heading_or_symbol(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "avatar-fox")
        self.assertNotContains(response, "CR control room")
        self.assertNotContains(response, "✦")

    def test_profile_update_saves_selected_avatar(self):
        response = self.client.post(
            reverse("updateProfile"),
            {
                "names": "Diva Agrawal",
                "colName": "IIT Bombay",
                "state": "Maharashtra",
                "phoneNo": "9999999999",
                "avatar": "owl",
            },
        )

        self.assertRedirects(response, reverse("dashboard"))
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.avatar, "owl")

    def test_leaderboard_shows_participant_avatar(self):
        task = Task.objects.create(title="Outreach", description="Share Aakaar", points=100)
        Submission.objects.create(
            task=task,
            user=self.participant,
            link="https://example.com/proof",
            marks=75,
            graded=True,
        )

        response = self.client.get(reverse("leaderboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "avatar-fox")
        self.assertContains(response, "Diva Agrawal")


class PublicContactTests(TestCase):
    def test_home_shows_contact_without_an_organiser_phone_number(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sarthak Kastiya")
        self.assertNotContains(response, "9926967455")
        self.assertNotContains(response, "tel:")
        self.assertContains(response, "mailto:sarthak@aakaariitb.ac.in")
        self.assertNotContains(response, "Nidhi Patel")
