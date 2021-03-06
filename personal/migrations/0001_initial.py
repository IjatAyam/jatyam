# Generated by Django 2.2 on 2020-03-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('banner', models.ImageField(upload_to='home/slider/banner/%Y/%m/%d/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('desc', models.TextField(blank=True)),
                ('button_label', models.CharField(blank=True, max_length=50)),
                ('button_to', models.CharField(blank=True, max_length=75)),
                ('align', models.CharField(choices=[('left', 'left'), ('center', 'center'), ('right', 'right')], default='left', max_length=5)),
                ('order', models.IntegerField(blank=True, default=1)),
            ],
        ),
    ]
