# Generated by Django 4.1 on 2022-09-07 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hosps', '0002_alter_hospital_hosp_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hosp_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hosptype', to='hosps.hosptype'),
        ),
    ]