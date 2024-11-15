# Generated by Django 5.1.1 on 2024-11-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='blog_post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='Blog.tag'),
        ),
    ]
