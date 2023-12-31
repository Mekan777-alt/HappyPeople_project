# Generated by Django 3.2.15 on 2023-09-02 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='sales_product')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
            options={
                'verbose_name': 'Особое предложение',
                'verbose_name_plural': 'Особое предложение',
            },
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='Products',
        ),
    ]
