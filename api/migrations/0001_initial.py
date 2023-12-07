# Generated by Django 4.2.4 on 2023-08-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]