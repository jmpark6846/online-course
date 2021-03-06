# Generated by Django 2.1.5 on 2019-01-14 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='수정 일시')),
                ('deleted_at', models.DateTimeField(default=None, help_text='삭제 일시', null=True)),
                ('Course', models.ForeignKey(help_text='코스 정보', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='courses', to='course.Course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='수정 일시')),
                ('deleted_at', models.DateTimeField(default=None, help_text='삭제 일시', null=True)),
                ('status', models.PositiveIntegerField(help_text='상태', null=True)),
                ('amount', models.IntegerField(help_text='결제 금액')),
                ('uid', models.CharField(help_text='주문 번호 (merchant_uid)', max_length=16, unique=True)),
                ('description', models.CharField(help_text='거래 상세 내용', max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(help_text='결제 정보', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='payment.Payment'),
        ),
    ]
