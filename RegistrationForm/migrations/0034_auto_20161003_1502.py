# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0033_auto_20161003_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegateinput',
            name='Name_of_School',
            field=models.CharField(help_text=b'<em><small><small>Please enter the name of your institution. Make sure the name is spelt the exact same as specified on the dashboard. Do not put accents in the name, or the submission will not work.</small></small></em>', max_length=120, null=True),
        ),
    ]
