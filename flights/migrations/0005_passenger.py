# Generated by Django 4.2 on 2023-04-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_rename_flights_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight')),
            ],
        ),
    ]