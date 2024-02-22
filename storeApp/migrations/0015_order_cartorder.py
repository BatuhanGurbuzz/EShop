# Generated by Django 5.0.2 on 2024-02-17 11:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("storeApp", "0014_contact"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=200, verbose_name="Ad")),
                ("lastname", models.CharField(max_length=200, verbose_name="Soyad")),
                ("country", models.CharField(max_length=200, verbose_name="Ülke")),
                ("address", models.TextField(verbose_name="Adres")),
                ("city", models.CharField(max_length=200, verbose_name="Şehir")),
                ("state", models.CharField(max_length=200, verbose_name="İlçe")),
                ("postcode", models.IntegerField(verbose_name="Posta Kodu")),
                ("phone", models.IntegerField(verbose_name="Telefon")),
                ("email", models.EmailField(max_length=200, verbose_name="E-Posta")),
                (
                    "additional_information",
                    models.TextField(blank=True, null=True, verbose_name="Ek Bilgi"),
                ),
                ("amount", models.IntegerField(verbose_name="Tutar")),
                ("date", models.DateTimeField(auto_now_add=True, verbose_name="Tarih")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Kullanıcı",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sipariş",
                "verbose_name_plural": "Siparişler",
            },
        ),
        migrations.CreateModel(
            name="CartOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="products/", verbose_name="Ürün Resmi"),
                ),
                ("quantity", models.CharField(max_length=200, verbose_name="Miktar")),
                ("price", models.CharField(max_length=200, verbose_name="Fiyat")),
                ("total", models.CharField(max_length=200, verbose_name="Toplam")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("New", "Sipariş Alındı"),
                            ("Accepted", "Hazırlanıyor"),
                            ("Cancelled", "İptal Edildi"),
                            ("Completed", "Tamamlandı"),
                            ("Returned", "İade Edildi"),
                            ("Shipped", "Kargoya Verildi"),
                        ],
                        default="New",
                        max_length=200,
                        verbose_name="Durum",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="storeApp.product",
                        verbose_name="Ürün",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="storeApp.order",
                        verbose_name="Sipariş",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sipariş Ürün",
                "verbose_name_plural": "Sipariş Ürünler",
            },
        ),
    ]