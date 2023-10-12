# Generated by Django 3.2.16 on 2023-10-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('avatarUrl', models.ImageField(upload_to='')),
                ('usertag', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
    ]
