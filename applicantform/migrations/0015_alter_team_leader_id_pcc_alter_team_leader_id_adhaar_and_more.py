# Generated by Django 4.1 on 2023-04-10 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicantform', '0014_remove_team_first_choice_remove_team_padi_specialty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='leader_id_PCC',
            field=models.FileField(upload_to='id_pcc'),
        ),
        migrations.AlterField(
            model_name='team',
            name='leader_id_adhaar',
            field=models.FileField(upload_to='id_adhaar'),
        ),
        migrations.AlterField(
            model_name='team',
            name='leader_photo',
            field=models.FileField(upload_to='photos'),
        ),
    ]