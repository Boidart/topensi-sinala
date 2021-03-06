# Generated by Django 3.0.6 on 2020-05-27 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lister', '0004_auto_20200527_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='lister.Client'),
        ),
        migrations.AlterField(
            model_name='info',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='lister.Type'),
        ),
    ]
