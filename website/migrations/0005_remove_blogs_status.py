# Generated by Django 4.2.4 on 2023-09-06 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_blogs_updated_on_alter_blogs_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='status',
        ),
    ]
