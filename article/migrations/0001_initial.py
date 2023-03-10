# Generated by Django 4.1.3 on 2023-01-11 03:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='分类名')),
                ('alias', models.CharField(db_index=True, max_length=128, verbose_name='别名')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('display', models.BooleanField(db_index=True, default=True, verbose_name='显示')),
                ('sort', models.IntegerField(db_index=True, default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类管理',
            },
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('x', models.IntegerField(verbose_name='X坐标')),
                ('y', models.IntegerField(verbose_name='Y坐标')),
                ('font_size', models.IntegerField(blank=True, default=24, null=True, verbose_name='字体大小')),
                ('color', models.CharField(blank=True, default='#FFF', max_length=12, null=True, verbose_name='颜色')),
                ('image', models.ImageField(upload_to='', verbose_name='图片')),
            ],
            options={
                'verbose_name': '封面',
                'verbose_name_plural': '封面管理',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='no_name', max_length=128, verbose_name='昵称')),
                ('email', models.CharField(blank=True, max_length=256, null=True, verbose_name='邮箱')),
                ('nodeId', models.CharField(max_length=256, verbose_name='OAuth ID')),
                ('avatar', models.CharField(max_length=256, verbose_name='头像')),
                ('url', models.CharField(blank=True, max_length=256, null=True, verbose_name='主页')),
                ('blog', models.CharField(blank=True, max_length=256, null=True, verbose_name='博客')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('updateDate', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('type', models.IntegerField(choices=[(0, 'Github'), (1, 'QQ'), (2, '代码集市')], db_index=True, verbose_name='用户类型')),
            ],
            options={
                'verbose_name': '会员',
                'verbose_name_plural': '会员管理',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, verbose_name='内容')),
                ('parentId', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='父ID')),
                ('targetId', models.CharField(blank=True, db_index=True, max_length=128, null=True, verbose_name='目标ID')),
                ('type', models.IntegerField(choices=[(0, '文章'), (1, '留言'), (2, '页面'), (3, '项目')], db_index=True, verbose_name='类型')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('atMember', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='at_member_id', to='article.member', verbose_name='回复用户')),
                ('member', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.member', verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论管理',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sid', models.CharField(blank=True, db_index=True, editable=False, max_length=8, null=True, verbose_name='短ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('markdown', models.BooleanField(default=True, editable=False, verbose_name='markdown格式')),
                ('hits', models.IntegerField(default=0, editable=False, verbose_name='点击量')),
                ('content', mdeditor.fields.MDTextField(verbose_name='内容')),
                ('subject', models.TextField(editable=False, verbose_name='简介')),
                ('image', models.ImageField(blank=True, db_index=True, null=True, upload_to='static/images/', verbose_name='封面')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('tags', models.CharField(blank=True, max_length=256, null=True, verbose_name='标签')),
                ('top', models.IntegerField(choices=[(0, '否'), (1, '是')], db_index=True, default=0, verbose_name='置顶')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.category', verbose_name='分类')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='发布者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章管理',
            },
        ),
    ]
