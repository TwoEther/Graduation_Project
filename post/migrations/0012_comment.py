# Generated by Django 4.1.1 on 2022-11-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0011_alter_category1_table_alter_category2_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "db_table": "comment",
                "managed": False,
            },
        ),
    ]