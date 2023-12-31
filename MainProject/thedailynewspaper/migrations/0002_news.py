# Generated by Django 3.2.4 on 2021-09-29 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thedailynewspaper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('headlines', models.CharField(max_length=400)),
                ('subject', models.CharField(max_length=800)),
                ('newsdes', models.TextField(max_length=8000)),
                ('newspic', models.ImageField(default='', upload_to='static/news/')),
                ('ndate', models.DateField()),
                ('ncategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedailynewspaper.category')),
            ],
        ),
    ]
