# Generated by Django 3.2.7 on 2023-09-30 12:04

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('admission_number', models.CharField(max_length=10, unique=True)),
                ('parent_phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KE')),
                ('date_added_at', models.DateTimeField(auto_now_add=True)),
                ('date_updated_at', models.DateTimeField(auto_now=True)),
                ('class_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade.grade')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.parent')),
            ],
        ),
    ]
