# Generated by Django 4.1.1 on 2022-10-23 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0004_user_delete_userinfo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
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
                ("image", models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                "db_table": "photo",
                "managed": False,
            },
        ),
    ]
