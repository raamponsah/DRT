# Generated by Django 4.0.1 on 2022-01-07 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=None, max_length=255)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=255, null=True, unique=True)),
                ('date_of_birth', models.DateField()),
                ('primary_phone', models.CharField(max_length=255)),
                ('secondary_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('residential_address', models.CharField(blank=True, max_length=255, null=True)),
                ('city_or_town', models.CharField(blank=True, max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('occupation', models.CharField(choices=[('teacher', 'Teacher'), ('lecturer', 'Lecturer'), ('nurse', 'Nurse'), ('doctor', 'Doctor')], max_length=255)),
                ('sector', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], max_length=255)),
                ('education_level', models.CharField(choices=[('no-school', 'Not Applicable'), ('primary', 'Primary'), ('jhs', 'JHS'), ('shs', 'SHS'), ('vocational', 'Vocational'), ('certificate', 'Certificate'), ('diploma', 'Diploma'), ('diploma', 'Diploma'), ('hnd', 'HND'), ('degree', 'Degree'), ('masters', 'masters'), ('phd', 'PHD')], max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('father_hometown', models.CharField(max_length=255)),
                ('father_living_status', models.BooleanField(choices=[(0, 'Deceased'), (1, 'Alive')], default=True)),
                ('mother_name', models.CharField(max_length=255)),
                ('mother_hometown', models.CharField(max_length=255)),
                ('mother_living_status', models.BooleanField(choices=[(0, 'Deceased'), (1, 'Alive')], default=True)),
                ('next_of_kin_name', models.CharField(max_length=255)),
                ('next_of_kin_relationship', models.CharField(choices=[('brother', 'Brother'), ('sister', 'Sister'), ('father', 'Father'), ('mother', 'Mother'), ('son', 'Son'), ('cousin', 'Cousin'), ('friend', 'Friend')], max_length=255)),
                ('next_of_kin_primary_phone', models.CharField(max_length=255)),
                ('next_of_kin_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('next_of_kin_location', models.CharField(blank=True, max_length=255)),
                ('emergency_name', models.CharField(max_length=255)),
                ('emergency_primary_phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NonFinancialDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Levy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, null=True)),
                ('january_payment', models.FloatField(blank=True, null=True)),
                ('february_payment', models.FloatField(blank=True, null=True)),
                ('march_payment', models.FloatField(blank=True, null=True)),
                ('april_payment', models.FloatField(blank=True, null=True)),
                ('may_payment', models.FloatField(blank=True, null=True)),
                ('june_payment', models.FloatField(blank=True, null=True)),
                ('july_payment', models.FloatField(blank=True, null=True)),
                ('august_payment', models.FloatField(blank=True, null=True)),
                ('september_payment', models.FloatField(blank=True, null=True)),
                ('october_payment', models.FloatField(blank=True, null=True)),
                ('november_payment', models.FloatField(blank=True, null=True)),
                ('december_payment', models.FloatField(blank=True, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='membership.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberReligiousCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baptism_status', models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=True)),
                ('baptism_date', models.DateField(blank=True, null=True)),
                ('baptism_location', models.CharField(blank=True, max_length=255, null=True)),
                ('baptised_by', models.CharField(blank=True, max_length=255, null=True)),
                ('holy_communion_status', models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=True)),
                ('holy_communion_date', models.DateField(blank=True, null=True)),
                ('holy_communion_location', models.CharField(blank=True, max_length=255, null=True)),
                ('holy_communion_given_by', models.CharField(blank=True, max_length=255, null=True)),
                ('confirmation_status', models.BooleanField(choices=[(0, 'No'), (1, 'Yes')], default=True)),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('confirmation_location', models.CharField(blank=True, max_length=255, null=True)),
                ('confirmed_by', models.CharField(blank=True, max_length=255, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='membership.member')),
            ],
        ),
    ]