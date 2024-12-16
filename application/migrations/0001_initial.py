# Generated by Django 5.1.3 on 2024-12-15 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=11)),
                ('description', models.TextField()),
                ('fullname', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=6)),
                ('role', models.IntegerField()),
                ('is_verified', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BnbInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacity', models.IntegerField()),
                ('count_viewed', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='application.category')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='application.location')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.bnbinformation')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='application.account')),
            ],
        ),
        migrations.AddField(
            model_name='bnbinformation',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.owner'),
        ),
        migrations.AddField(
            model_name='bnbinformation',
            name='rule',
            field=models.ManyToManyField(to='application.rule'),
        ),
        migrations.AddField(
            model_name='bnbinformation',
            name='service',
            field=models.ManyToManyField(to='application.service'),
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired_at', models.DateTimeField()),
                ('verify_type', models.CharField(choices=[('phone', 'Phone'), ('email', 'Email')], max_length=5)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.account')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='application.account')),
            ],
        ),
        migrations.CreateModel(
            name='WishListItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_time', models.DateTimeField(auto_now_add=True)),
                ('bnb_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.bnbinformation')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='application.wishlist')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accept', 'Accept'), ('decline', 'Decline'), ('served', 'Served')], max_length=7)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.account')),
                ('bnb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.bnbinformation')),
            ],
            options={
                'unique_together': {('account', 'bnb', 'from_date', 'to_date')},
            },
        ),
        migrations.CreateModel(
            name='OwnerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.CharField(choices=[('none', None), ('positive', 'POS'), ('negative', 'NEG'), ('neutral', 'NEU')], max_length=8)),
                ('rating', models.IntegerField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.account')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.owner')),
            ],
            options={
                'unique_together': {('owner', 'account')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.CharField(choices=[('none', None), ('positive', 'POS'), ('negative', 'NEG'), ('neutral', 'NEU')], max_length=8)),
                ('rating', models.IntegerField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.account')),
                ('bnb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.bnbinformation')),
            ],
            options={
                'unique_together': {('bnb', 'account')},
            },
        ),
    ]
