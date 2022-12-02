# Generated by Django 3.2.16 on 2022-11-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0015_auto_20221011_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userloginlog',
            name='type',
            field=models.CharField(choices=[('web_cli', 'Web Client'), ('web_gui', 'Web GUI'), ('db_cli', 'DB Client'), ('db_gui', 'DB GUI'), ('rdp_cli', 'RDP Client'), ('rdp_file', 'RDP File'), ('ssh_cli', 'SSH Client'), ('web_sftp', 'Web SFTP')], max_length=128, verbose_name='Login type'),
        ),
    ]
