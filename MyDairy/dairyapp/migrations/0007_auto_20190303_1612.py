# Generated by Django 2.1.7 on 2019-03-03 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0006_auto_20190303_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milkcategory',
            name='animalname',
            field=models.CharField(choices=[('Cow', 'Cow'), ('Buffaloe', 'Buffaloe'), ('Others', 'Others')], max_length=1),
        ),
    ]