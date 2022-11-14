# Generated by Django 4.1.3 on 2022-11-14 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_alter_book_options_book_author_name_alter_book_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id'], 'verbose_name': 'Книгу', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
    ]
