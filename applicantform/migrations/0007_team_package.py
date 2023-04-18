# Generated by Django 4.1 on 2023-04-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantform', '0006_team_padi_specialty'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='package',
            field=models.CharField(choices=[('Fun Dive Package', 'Fun Dive Package'), ('Fun Dive + Course Package', 'Fun Dive + Course Package'), ('Open Water Dive Course Package', 'Open Water Dive Course Package'), ('Advanced Open Water Diver Course Package', 'Advanced Open Water Diver Course Package'), ('Open & Advanced Open Water Diver Course', 'Open & Advanced Open Water Diver Course'), ('Open Water To Dive Master', 'Open Water To Dive Master'), ('Explore Lakshadweep', 'Explore Lakshadweep')], default=1, max_length=240),
            preserve_default=False,
        ),
    ]
