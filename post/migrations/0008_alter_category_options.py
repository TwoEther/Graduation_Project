# Generated by Django 4.1.1 on 2022-10-27 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0007_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"managed": False, "verbose_name_plural": "Categories"},
        ),
    ]
