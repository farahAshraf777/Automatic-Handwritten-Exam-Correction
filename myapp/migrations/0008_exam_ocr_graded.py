# Generated by Django 5.0.4 on 2024-05-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_examsubmissionocr_is_graded_examsubmissionocr_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="exam",
            name="ocr_graded",
            field=models.BooleanField(default=False),
        ),
    ]
