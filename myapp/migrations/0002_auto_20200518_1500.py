# Generated by Django 3.0.6 on 2020-05-18 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=100)),
                ('end_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=100)),
                ('tz', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ActivityPeriod',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='myapp.UserData'),
        ),
    ]
