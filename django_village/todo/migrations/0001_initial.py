# Generated by Django 2.2 on 2019-08-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=128)),
                ('is_completed', models.BooleanField(default=False)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]