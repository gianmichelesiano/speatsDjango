# Generated by Django 3.0.4 on 2020-03-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordini', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordine',
            name='id',
        ),
        migrations.AddField(
            model_name='ordine',
            name='payment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ordine',
            name='order_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
