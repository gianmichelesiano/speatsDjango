# Generated by Django 3.0.4 on 2020-05-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_consegne_richiesta'),
    ]

    operations = [
        migrations.AddField(
            model_name='consegne',
            name='totale_ordine',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
