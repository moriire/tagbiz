# Generated by Django 5.0 on 2023-12-27 12:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='selected',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_item_buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='selected',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selected_item', to='items.itemwiththumbs'),
        ),
        migrations.AddField(
            model_name='itemwiththumbs',
            name='thumbs',
            field=models.ManyToManyField(related_name='item_images', to='items.upload'),
        ),
    ]