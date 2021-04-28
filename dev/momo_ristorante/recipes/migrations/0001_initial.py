# Generated by Django 3.2 on 2021-04-26 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0004_auto_20210426_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('excerpt', models.CharField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True)),
                ('create_date', models.DateField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
            ],
        ),
    ]
