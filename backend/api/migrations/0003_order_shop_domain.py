# Generated by Django 5.1.2 on 2024-10-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shop_domain',
            field=models.CharField(default='quickstart-719550ac.myshopify.com', max_length=255),
            preserve_default=False,
        ),
    ]
