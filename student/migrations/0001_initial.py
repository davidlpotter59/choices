# Generated by Django 2.2.1 on 2019-07-17 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=0, max_length=50)),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='houses.House')),
            ],
        ),
    ]
