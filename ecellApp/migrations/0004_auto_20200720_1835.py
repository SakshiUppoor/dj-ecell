# Generated by Django 3.0.8 on 2020-07-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecellApp', '0003_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('intro', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='achievement',
            name='intro',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='startup',
            name='intro',
            field=models.CharField(max_length=200),
        ),
    ]
