# Generated by Django 4.1.3 on 2022-12-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_rename_adddress_emp_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testimonial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonials/')),
                ('rating', models.IntegerField(max_length=1)),
            ],
        ),
    ]
