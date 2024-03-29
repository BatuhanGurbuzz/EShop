# Generated by Django 5.0.2 on 2024-02-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("storeApp", "0006_images_tag"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="condition",
            field=models.BooleanField(
                choices=[("NEW", "Yeni"), ("OLD", "Eski")], verbose_name="Durum"
            ),
        ),
    ]
