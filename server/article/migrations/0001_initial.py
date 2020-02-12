# Generated by Django 3.0 on 2020-02-08 10:40

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('is_active', models.BooleanField(default=False)),
                ('order', models.IntegerField(blank=True, default=9999, null=True)),
                ('show_as_category', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', models.IntegerField(choices=[(1, 'Country'), (2, 'City'), (3, 'Area'), (4, 'Thana'), (5, 'Postcode'), (6, 'PostOffice'), (7, 'Division')])),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('Drafted', 'Drafted'), ('Published', 'Published'), ('Rejected', 'Rejected'), ('Trashed', 'Trashed')], default='Drafted', max_length=10)),
                ('keywords', models.TextField(blank=True, max_length=500, null=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='blog/uploads/%Y/%m/%d/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Category')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Location')),
                ('tags', models.ManyToManyField(related_name='rel_posts', to='article.Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('menu_type', models.IntegerField(choices=[(1, 'Top-Menu'), (2, 'Main-Menu'), (3, 'Widget-Menu'), (4, 'Footer-Menu')])),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='article.Menu')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('commend_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='comment_user', to=settings.AUTH_USER_MODEL)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='post_comment', to='article.Post')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
