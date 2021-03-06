# Generated by Django 3.1 on 2020-09-23 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='platform',
            name='controllers',
            field=models.ManyToManyField(to='main_app.Controller'),
        ),
    ]
