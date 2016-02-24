# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Menu'
        db.create_table(u'init_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=144)),
        ))
        db.send_create_signal(u'init', ['Menu'])


    def backwards(self, orm):
        # Deleting model 'Menu'
        db.delete_table(u'init_menu')


    models = {
        u'init.inicio': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '144'})
        }
    }

    complete_apps = ['init']