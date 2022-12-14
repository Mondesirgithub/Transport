# Generated by Django 4.1.4 on 2022-12-17 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_chauffeur_geolocation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='geolocalisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.map'),
        ),
        migrations.AddField(
            model_name='livreur',
            name='geolocalisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.map'),
        ),
        migrations.AlterField(
            model_name='chauffeur',
            name='geolocalisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.map'),
        ),
    ]
