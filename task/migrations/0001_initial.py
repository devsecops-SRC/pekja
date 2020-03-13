# Generated by Django 3.0.4 on 2020-03-13 12:19

from django.db import migrations, models
import django.db.models.deletion
import task.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='工具名')),
                ('link', models.URLField(blank=True, null=True, verbose_name='项目地址')),
                ('type', models.CharField(max_length=50, verbose_name='记录类型')),
                ('parse_class_name', models.CharField(max_length=50, verbose_name='输出解析类')),
                ('command', models.CharField(max_length=500, validators=[task.validators.command_validator], verbose_name='调用命令')),
                ('input_type', models.CharField(choices=[('file', '文件'), ('parameter', '参数')], default='file', max_length=50, verbose_name='输入参数类型')),
                ('version', models.CharField(blank=True, max_length=50, null=True, verbose_name='版本')),
                ('comment', models.CharField(blank=True, max_length=100, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '工具表',
                'verbose_name_plural': '工具表',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='任务名')),
                ('input', models.TextField(verbose_name='输入')),
                ('input_file_type', models.CharField(choices=[('static_file', '静态'), ('dynamic_file', '动态')], default='static_file', max_length=50, verbose_name='输入文件类型')),
                ('dispatch', models.CharField(max_length=100, validators=[task.validators.cron_validator], verbose_name='调度')),
                ('active', models.BooleanField(default=True, verbose_name='是否生效')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Project', verbose_name='所属项目')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Tool', verbose_name='工具')),
            ],
            options={
                'verbose_name': '任务表',
                'verbose_name_plural': '任务表',
            },
        ),
    ]
