# Generated by Django 5.0.7 on 2024-07-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('facebook_link', models.CharField(max_length=100)),
                ('twitter_link', models.CharField(max_length=100)),
                ('goole_plus_link', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
