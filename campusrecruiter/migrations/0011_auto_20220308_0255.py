# Generated by Django 3.1.3 on 2022-03-07 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusrecruiter', '0010_alter_candidate_studentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='Image',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='company',
            name='CompanyLogo',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='education',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
