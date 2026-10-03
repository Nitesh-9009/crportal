"""Seed demo data so the merged portal can be explored locally.

Run:  python manage.py shell < seed_demo.py
"""
from django.contrib.auth.models import User
from aakarapp.models import TaskZero, Task, Submission

# --- Admin ---
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@aakaariitb.org.in', 'admin123', first_name='Portal Admin')
    print('superuser: admin / admin123')

# --- Tasks ---
task_specs = [
    ("TASK 1", "Share the official Aakaar 2027 poster on your WhatsApp status and Instagram story. Submit a screenshot link as proof.", 100),
    ("TASK 2", "Get your college's civil engineering department head's permission to put up the Aakaar banner. Submit a photo of the banner.", 150),
    ("TASK 3", "Organize a 30-minute intro session about Aakaar and the CR program in your class. Submit attendance proof or photos.", 200),
    ("TASK 4", "Bring a minimum of 5 registrations for Aakaar workshops from your college. Submit the registration list.", 250),
    ("TASK 5", "Watch the instruction video and record a short campus promo reel for Aakaar 2027. Submit the reel link.", 300),
]
tasks = {}
for title, desc, points in task_specs:
    task, _ = Task.objects.get_or_create(title=title, defaults={'description': desc, 'points': points})
    tasks[title] = task

# --- Demo CRs with submissions ---
crs = [
    ('aarav@example.edu', 'Aarav Sharma', 'NIT Trichy', 'Tamil Nadu', {'TASK 1': 95, 'TASK 2': 140, 'TASK 3': 180}),
    ('pooja@example.edu', 'Pooja Deshmukh', 'COEP Pune', 'Maharashtra', {'TASK 1': 90, 'TASK 2': 130}),
    ('karthik@example.edu', 'Karthik Raja', 'BITS Pilani', 'Rajasthan', {'TASK 1': 100}),
    ('ananya@example.edu', 'Ananya Roy', 'Jadavpur University', 'West Bengal', {'TASK 1': 85, 'TASK 3': 150}),
    ('rohan@example.edu', 'Rohan Kulkarni', 'VNIT Nagpur', 'Maharashtra', {}),
]
avatars = ['rhino-orange', 'black-bear', 'koala', 'owl', 'deer']
for idx, (email, name, college, state, subs) in enumerate(crs):
    user, created = User.objects.get_or_create(username=email, defaults={'email': email, 'first_name': name})
    user.set_password('demo1234')
    user.save()
    if created:
        TaskZero.objects.create(
            crid=f"AK{250000 + user.id}", names=name, username=email, email=email, emails=email,
            colgName=college, state=state, city='Demo City', pincode='400001',
            mobileNo='9876543210', whatsappNo='9876543210', avatar=avatars[idx % len(avatars)],
        )
    for task_title, marks in subs.items():
        Submission.objects.get_or_create(
            user=user, task=tasks[task_title],
            defaults={'link': 'https://example.com/proof', 'marks': marks, 'graded': True},
        )
    print(f"CR: {email} / demo1234 — {name}")

print('Demo data ready.')
