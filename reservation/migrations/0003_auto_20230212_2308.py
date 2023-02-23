# Generated by Django 3.2.16 on 2023-02-12 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0002_auto_20230212_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apploved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applouved', models.BooleanField(default=False)),
                ('applouved_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservation.group')),
            ],
        ),
        migrations.AddConstraint(
            model_name='apploved',
            constraint=models.UniqueConstraint(fields=('applouved_user', 'group'), name='applouved_unique'),
        ),
    ]