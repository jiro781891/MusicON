# Generated by Django 2.0 on 2018-02-03 13:18

import audiotracks.models
import audiotracks.thumbs
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('audio_file', models.FileField(upload_to=audiotracks.models.get_audio_upload_path, verbose_name='Audio file')),
                ('image', audiotracks.thumbs.ImageWithThumbsField(blank=True, null=True, upload_to=audiotracks.models.get_images_upload_path)),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('artist', models.CharField(blank=True, max_length=200, null=True, verbose_name='Artist')),
                ('genre', models.CharField(blank=True, max_length=200, null=True, verbose_name='Genre')),
                ('date', models.CharField(blank=True, max_length=200, null=True, verbose_name='Date')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('slug', models.SlugField(verbose_name='Slug (last part of the url)')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'swappable': 'AUDIOTRACKS_MODEL',
            },
        ),
    ]