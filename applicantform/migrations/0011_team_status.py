# Generated by Django 4.1 on 2023-04-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantform', '0010_team_ac_or_nonac_team_number_of_rooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('open', 'open'), ('Confirm', 'Confirm'), ('Closed', 'Closed'), ('Complete', 'Complete')], default='Processing', max_length=100),
        ),
    ]
