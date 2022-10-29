# Generated by Django 4.1.1 on 2022-10-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0006_delete_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                    "main_category",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
            ],
            options={
                "db_table": "category",
                "managed": False,
            },
        ),
    ]
