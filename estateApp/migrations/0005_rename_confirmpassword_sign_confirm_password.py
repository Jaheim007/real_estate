# Generated by Django 4.0.4 on 2022-05-04 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estateApp', '0004_alter_sign_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sign',
            old_name='confirmPassword',
            new_name='confirm_Password',
        ),
    ]