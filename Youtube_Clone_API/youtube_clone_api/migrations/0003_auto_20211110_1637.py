# Generated by Django 3.2.9 on 2021-11-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_clone_api', '0002_auto_20211110_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='comment_id',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='video_id',
            field=models.CharField(default='alkjsdf', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LikeButton',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]