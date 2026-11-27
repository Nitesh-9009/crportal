from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("aakarapp", "0033_taskzero_avatar")]
    operations = [
        migrations.AddField(
            model_name="task",
            name="publish_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Scheduled publish time", help_text="Leave blank to publish immediately. Otherwise the task becomes available at this date and time (in the admin's displayed time zone)."),
        ),
    ]
