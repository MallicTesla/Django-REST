# Generated by Django 4.2.5 on 2023-10-20 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0004_historicalunidadmedida_historicalproducto_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaGasto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(auto_now=True, verbose_name='Fecha de borrado')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Categoría de Gasto')),
            ],
            options={
                'verbose_name': 'Categoria de Gasto',
                'verbose_name_plural': 'Categorias de Gastos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Comprobante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(auto_now=True, verbose_name='Fecha de borrado')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de comprobante de Pago')),
            ],
            options={
                'verbose_name': 'Comprobante',
                'verbose_name_plural': 'Comprobantes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MedioDePago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(auto_now=True, verbose_name='Fecha de borrado')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Medio de Pago')),
            ],
            options={
                'verbose_name': 'Medio de Pago',
                'verbose_name_plural': 'Medio de Pagos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Provedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(auto_now=True, verbose_name='Fecha de borrado')),
                ('ruc', models.CharField(max_length=11, unique=True)),
                ('business_name', models.CharField(max_length=150, unique=True, verbose_name='Razón Social')),
                ('direcsion', models.CharField(max_length=200)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Merma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(auto_now=True, verbose_name='Fecha de borrado')),
                ('fecha_merma', models.DateField(verbose_name='Fecha de emisión de Merma')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Cantidad')),
                ('perdida', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Dinero perdido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
            options={
                'verbose_name': 'Merma',
                'verbose_name_plural': 'Mermas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='HistoricalProvedor',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(blank=True, editable=False, verbose_name='Fecha de borrado')),
                ('ruc', models.CharField(db_index=True, max_length=11)),
                ('business_name', models.CharField(db_index=True, max_length=150, verbose_name='Razón Social')),
                ('direcsion', models.CharField(max_length=200)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Proveedor',
                'verbose_name_plural': 'historical Proveedores',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMerma',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(blank=True, editable=False, verbose_name='Fecha de borrado')),
                ('fecha_merma', models.DateField(verbose_name='Fecha de emisión de Merma')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Cantidad')),
                ('perdida', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Dinero perdido')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='productos.producto')),
            ],
            options={
                'verbose_name': 'historical Merma',
                'verbose_name_plural': 'historical Mermas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMedioDePago',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(blank=True, editable=False, verbose_name='Fecha de borrado')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Medio de Pago')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Medio de Pago',
                'verbose_name_plural': 'historical Medio de Pagos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalGasto',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(blank=True, editable=False, verbose_name='Fecha de borrado')),
                ('frcha_factura', models.DateField(verbose_name='Fecha de emisión de factura')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio Unitario')),
                ('numero_comprobante', models.CharField(max_length=50, verbose_name='Número de comprobante')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('comprobante', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gestion_gastos.comprobante')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('medio_de_pago', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gestion_gastos.mediodepago')),
                ('producto', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='productos.producto')),
                ('provedor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gestion_gastos.provedor')),
                ('usuario', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Gasto',
                'verbose_name_plural': 'historical Gastos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalComprobante',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(blank=True, editable=False, verbose_name='Fecha de borrado')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de comprobante de Pago')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Comprobante',
                'verbose_name_plural': 'historical Comprobantes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategoriaGasto',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(blank=True, editable=False, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(blank=True, editable=False, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(blank=True, editable=False, verbose_name='Fecha de borrado')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de Categoría de Gasto')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Categoria de Gasto',
                'verbose_name_plural': 'historical Categorias de Gastos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('frcha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('fecha_modificado', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_borrado', models.DateField(auto_now=True, verbose_name='Fecha de borrado')),
                ('frcha_factura', models.DateField(verbose_name='Fecha de emisión de factura')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio Unitario')),
                ('numero_comprobante', models.CharField(max_length=50, verbose_name='Número de comprobante')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total')),
                ('comprobante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_gastos.comprobante')),
                ('medio_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_gastos.mediodepago')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('provedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_gastos.provedor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Gasto',
                'verbose_name_plural': 'Gastos',
                'ordering': ['id'],
            },
        ),
    ]
