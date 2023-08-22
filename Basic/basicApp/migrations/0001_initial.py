# Generated by Django 4.2.4 on 2023-08-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=255, null=True)),
                ('publication', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
