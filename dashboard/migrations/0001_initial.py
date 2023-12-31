# Generated by Django 4.1 on 2023-10-31 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=50)),
                ('intensity', models.IntegerField(null=True)),
                ('sector', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.TextField()),
                ('url', models.URLField()),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.CharField(blank=True, max_length=50)),
                ('impact', models.TextField(blank=True)),
                ('added', models.DateTimeField(null=True)),
                ('published', models.DateTimeField(null=True)),
                ('country', models.CharField(max_length=100)),
                ('relevance', models.IntegerField(null=True)),
                ('pestle', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('likelihood', models.IntegerField(null=True)),
            ],
        ),
    ]
