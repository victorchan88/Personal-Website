# Generated by Django 2.2.3 on 2019-07-16 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='full',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]