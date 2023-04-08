# Generated by Django 4.2 on 2023-04-08 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_item_featured_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='featured_student',
        ),
        migrations.AddField(
            model_name='student',
            name='featured_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.item'),
        ),
    ]