# Generated by Django 3.2 on 2022-08-18 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_buildcnpjmodel_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buildcnpjmodel',
            options={'verbose_name': ' BUILD CNPJ', 'verbose_name_plural': ' BUILDS CNPJ'},
        ),
        migrations.AlterModelOptions(
            name='buildmodel',
            options={'verbose_name': ' BUILD INFO', 'verbose_name_plural': ' BUILDS INFO'},
        ),
        migrations.AlterModelOptions(
            name='buildnamemodel',
            options={'verbose_name': ' BUILD NAME', 'verbose_name_plural': ' BUILDS NAME'},
        ),
    ]