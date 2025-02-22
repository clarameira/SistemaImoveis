# Generated by Django 4.2.3 on 2025-02-20 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.usuario')),
                ('cpf', models.CharField(max_length=14, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.usuario',),
        ),
        migrations.CreateModel(
            name='Locador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.usuario')),
                ('cnpj', models.CharField(max_length=18, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('users.usuario',),
        ),
        migrations.DeleteModel(
            name='UserProfileExample',
        ),
    ]
