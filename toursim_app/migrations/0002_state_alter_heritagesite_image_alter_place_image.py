# Generated by Django 4.1.7 on 2023-12-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toursim_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/States/')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='heritagesite',
            name='image',
            field=models.ImageField(upload_to='images/HeritageSites/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to='images/places/'),
        ),
    ]