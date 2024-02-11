# Generated by Django 5.0.2 on 2024-02-10 09:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("storeApp", "0003_brand_description_filter_price_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="brand",
            options={"verbose_name": "Marka", "verbose_name_plural": "Markalar"},
        ),
        migrations.AlterModelOptions(
            name="color",
            options={"verbose_name": "Renk", "verbose_name_plural": "Renkler"},
        ),
        migrations.AlterModelOptions(
            name="filter_price",
            options={
                "verbose_name": "Fiyat aralığı",
                "verbose_name_plural": "Fiyatlar",
            },
        ),
    ]