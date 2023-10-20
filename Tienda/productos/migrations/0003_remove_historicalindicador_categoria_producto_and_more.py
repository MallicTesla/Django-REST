# Generated by Django 4.2.5 on 2023-10-20 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_historicalproducto_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalindicador',
            name='categoria_producto',
        ),
        migrations.RemoveField(
            model_name='historicalindicador',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalproducto',
            name='categoria_producto',
        ),
        migrations.RemoveField(
            model_name='historicalproducto',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalproducto',
            name='unidad_medida',
        ),
        migrations.RemoveField(
            model_name='historicalunidadmedida',
            name='history_user',
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen_producto',
            field=models.ImageField(blank=True, null=True, upload_to='productos_imagen/', verbose_name='Imagen del producto'),
        ),
        migrations.DeleteModel(
            name='HistoricalCategoriaProducto',
        ),
        migrations.DeleteModel(
            name='HistoricalIndicador',
        ),
        migrations.DeleteModel(
            name='HistoricalProducto',
        ),
        migrations.DeleteModel(
            name='HistoricalUnidadMedida',
        ),
    ]
