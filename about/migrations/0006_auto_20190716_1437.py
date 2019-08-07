# Generated by Django 2.2.3 on 2019-07-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20190716_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='full',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]