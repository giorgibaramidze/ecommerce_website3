# Generated by Django 4.2 on 2023-07-14 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model_pn',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterModelTable(
            name='productgallery',
            table='product_gallery',
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('construction_type', models.CharField(blank=True, max_length=30, null=True)),
                ('type_of_control', models.CharField(blank=True, max_length=30, null=True)),
                ('display', models.CharField(blank=True, max_length=30, null=True)),
                ('engine_type', models.CharField(blank=True, max_length=30, null=True)),
                ('special_features', models.CharField(blank=True, max_length=30, null=True)),
                ('loading_type', models.CharField(blank=True, max_length=30, null=True)),
                ('washing_capacity', models.CharField(blank=True, max_length=30, null=True)),
                ('add_wash', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=30, null=True)),
                ('eco_bubble', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=30, null=True)),
                ('steam_wash', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=30, null=True)),
                ('spin_speed', models.IntegerField(blank=True, null=True)),
                ('speed_adjustment', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=30, null=True)),
                ('water_consumption_per_cycle', models.IntegerField(blank=True, null=True)),
                ('noise_level_wash', models.IntegerField(blank=True, null=True)),
                ('noise_level_spin', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('dimensions', models.CharField(blank=True, help_text='Height x Width x Depth', max_length=30, null=True)),
                ('weight', models.IntegerField(blank=True, help_text='kg', null=True)),
                ('varianty_month', models.IntegerField(blank=True, null=True)),
                ('automatic_cold_reservation_hours', models.IntegerField(blank=True, null=True)),
                ('number_of_shelf', models.IntegerField(blank=True, null=True)),
                ('door_pocket', models.IntegerField(blank=True, null=True)),
                ('freezer_location', models.CharField(blank=True, max_length=30, null=True)),
                ('egg_container', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=30, null=True)),
                ('freezer_net_capacity', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'db_table': 'product_feature',
            },
        ),
    ]
