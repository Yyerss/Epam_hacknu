# Generated by Django 5.0.4 on 2024-04-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_determined_lvl', '0003_submissiondetail_submission_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsubmission',
            name='details',
        ),
        migrations.RemoveField(
            model_name='question',
            name='weight',
        ),
        migrations.AddField(
            model_name='testsubmission',
            name='answers',
            field=models.ManyToManyField(related_name='submissions', to='test_determined_lvl.answer'),
        ),
        migrations.DeleteModel(
            name='SubmissionDetail',
        ),
    ]