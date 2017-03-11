# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RegistrationForm', '0032_auto_20161003_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionpaper',
            name='Name_of_School',
            field=models.CharField(help_text=b'<em><small><small>Please enter the name of your institution. Make sure it is spelt exactly how it is specified on the dashboard. Do not put accents in the name or the submission will not work.</small></small></em>', max_length=120, null=True),
        ),
    ]
