# Generated by Django 3.1.5 on 2021-04-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
