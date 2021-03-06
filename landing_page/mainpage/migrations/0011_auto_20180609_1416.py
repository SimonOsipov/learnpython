# Generated by Django 2.0.6 on 2018-06-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0010_auto_20180609_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curator_name', models.CharField(help_text='Сначало имя, потом фамилия', max_length=50, verbose_name='Имя и фамилия куратора')),
                ('curator_bio', models.TextField(help_text='Где и кем работает, что программирует', verbose_name='Биография куратора')),
                ('curator_motto', models.CharField(blank=True, help_text='Через тернии к звездам или что-нибудь такое', max_length=150, null=True, verbose_name='Девиз куратора')),
                ('curator_photo', models.ImageField(blank=True, help_text='Фотография куратора', upload_to='courators/', verbose_name='Фото куратора')),
                ('curator_status', models.BooleanField(default=True, help_text='Куратор работает в текущем наборе?', verbose_name='Куратор для ближайшего набора?')),
                ('curator_github', models.URLField(blank=True, help_text='Ссылка на гит-хаб куратора', verbose_name='GitHub куратора')),
                ('curator_social_network', models.URLField(blank=True, help_text='Если есть, ссылка на соцсеточку', verbose_name='Соцсеточка куратора')),
            ],
            options={
                'verbose_name_plural': 'LearnPython Кураторы',
            },
        ),
        migrations.DeleteModel(
            name='Courators',
        ),
    ]
