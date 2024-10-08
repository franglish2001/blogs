# Generated by Django 4.2 on 2024-08-29 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(verbose_name='contenu'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='date_pub',
            field=models.DateField(verbose_name='date de publication'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='sumary',
            field=models.CharField(blank=True, max_length=250, verbose_name='resumer'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=100, verbose_name='titre'),
        ),
    ]
