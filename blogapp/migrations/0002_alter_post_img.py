# Generated by Django 3.2.6 on 2021-08-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(default='post_img/Capture1.png', upload_to='post_img/'),
        ),
    ]