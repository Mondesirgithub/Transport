# Generated by Django 4.1.4 on 2022-12-16 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='chauffeur',
            name='geolocation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.map'),
        ),
    ]