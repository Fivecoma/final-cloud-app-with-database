# Generated by Django 3.1.3 on 2020-11-26 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20201016_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=200)),
                ('content', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.course')),
            ],
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.course'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='learner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.learner'),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]