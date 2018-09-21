# Generated by Django 2.1.1 on 2018-09-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('designation', models.CharField(max_length=250, null=True)),
                ('joining_date', models.DateField()),
                ('experience', models.FloatField(default=0)),
                ('photo_url', models.CharField(max_length=500, null=True)),
                ('status', models.BooleanField(default=True)),
                ('dob', models.DateField()),
                ('contact', models.OneToOneField(on_delete=None, to='people.ContactDetails')),
                ('referred_by', models.ForeignKey(null=True, on_delete=None, to='people.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=None, to='people.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeTeams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=None, to='people.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='employeeteams',
            name='team',
            field=models.ForeignKey(on_delete=None, to='people.Team'),
        ),
        migrations.AddField(
            model_name='employeeproduct',
            name='project',
            field=models.ForeignKey(on_delete=None, to='people.Product'),
        ),
    ]
