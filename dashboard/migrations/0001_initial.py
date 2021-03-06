# Generated by Django 2.2 on 2020-06-22 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(help_text='Phone Number', max_length=13)),
                ('nrc', models.CharField(blank=True, max_length=13, null=True, verbose_name='NRC Number')),
                ('address', models.TextField(help_text='Enter Full Address.')),
                ('salary', models.IntegerField()),
                ('account_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
