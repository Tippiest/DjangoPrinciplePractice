# Generated by Django 4.1.6 on 2023-02-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0002_rename_person_name_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
