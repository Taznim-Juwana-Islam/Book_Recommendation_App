# Generated by Django 4.2.4 on 2023-08-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('status', models.TextField()),
            ],
        ),
    ]
