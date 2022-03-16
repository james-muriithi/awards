# Generated by Django 4.0.3 on 2022-03-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_user_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]