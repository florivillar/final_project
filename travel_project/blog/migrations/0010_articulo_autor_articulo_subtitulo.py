# Generated by Django 4.2.6 on 2023-11-18 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_post_articulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='autor',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articulo',
            name='subtitulo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
