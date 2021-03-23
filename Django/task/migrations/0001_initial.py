# Generated by Django 3.1.7 on 2021-03-23 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('done', 'Done'), ('todo', 'Todo')], default='todo', max_length=10)),
            ],
        ),
    ]
