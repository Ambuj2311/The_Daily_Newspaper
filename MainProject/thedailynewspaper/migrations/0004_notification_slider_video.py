# Generated by Django 3.2.4 on 2021-10-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thedailynewspaper', '0003_cities'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ndes', models.TextField(max_length=5000)),
                ('ndate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stitle', models.CharField(max_length=200)),
                ('sdes', models.CharField(max_length=500)),
                ('spic', models.ImageField(default='', upload_to='static/slider/')),
                ('sdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vtitle', models.CharField(max_length=200)),
                ('vdes', models.TextField(max_length=600)),
                ('thumb', models.ImageField(default='', upload_to='static/thumbnail/')),
                ('vlink', models.CharField(max_length=500)),
                ('vdate', models.DateField()),
            ],
        ),
    ]
