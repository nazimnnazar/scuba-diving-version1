# Generated by Django 4.1 on 2023-04-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantform', '0013_alter_team_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='first_choice',
        ),
        migrations.RemoveField(
            model_name='team',
            name='padi_specialty',
        ),
        migrations.AlterField(
            model_name='team',
            name='package',
            field=models.CharField(choices=[('Bubble Maker', 'Bubble Maker '), ('Seal Team', 'Seal Team'), ('Open Water Diver', 'Open Water Diver'), ('Adventure Diver', 'Adventure Diver'), ('Advanced Open Water Diver', 'Advanced Open Water Diver'), ('EFR Primary & Secondary Care', 'EFR Primary & Secondary Care'), ('Rescue Diver', 'Rescue Diver'), ('Dive Master', 'Dive Master'), ('Deep Diver', 'Deep Diver'), ('Digital Underwater Photography', 'Digital Underwater Photography'), ('Enriched Air Diver', 'Enriched Air Diver'), ('Night Diver', 'Night Diver'), ('Adaptive Support Diver', 'Adaptive Support Diver'), ('Adaptive Techniques', 'Adaptive Techniques'), ('DSMB Diver', 'DSMB Diver'), ('Emergency Oxygen Provider', 'Emergency Oxygen Provider'), ('Underwater Navigator', 'Underwater Navigator'), ('Wreck Diver', 'Wreck Diver'), ('Peak Performance Buoyancy', 'Peak Performance Buoyancy'), ('Fun Dive Package', 'Fun Dive Package'), ('Fun Dive + Course Package', 'Fun Dive + Course Package'), ('Open Water Dive Course Package', 'Open Water Dive Course Package'), ('Advanced Open Water Diver Course Package', 'Advanced Open Water Diver Course Package'), ('Open & Advanced Open Water Diver Course', 'Open & Advanced Open Water Diver Course'), ('Open Water To Dive Master', 'Open Water To Dive Master'), ('Explore Lakshadweep', 'Explore Lakshadweep')], max_length=240),
        ),
    ]
