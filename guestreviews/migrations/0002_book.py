# Generated by Django 3.2.4 on 2021-12-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestreviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
    ]
