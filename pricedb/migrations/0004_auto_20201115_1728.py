# Generated by Django 3.1.3 on 2020-11-15 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricedb', '0003_auto_20201115_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestateproperty',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='pricedb.searchhistory'),
        ),
    ]