# Generated by Django 3.2.4 on 2021-10-03 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thedailynewspaper', '0008_publishad'),
    ]

    operations = [
        migrations.CreateModel(
            name='world',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wheadlines', models.CharField(max_length=400)),
                ('country', models.CharField(max_length=20)),
                ('wsubject', models.CharField(max_length=800)),
                ('wdes', models.TextField(max_length=8000)),
                ('wpic', models.ImageField(default='', upload_to='static/news/')),
                ('wdate', models.DateField()),
            ],
        ),
    ]
