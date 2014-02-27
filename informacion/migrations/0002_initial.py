# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'tipo'
        db.create_table(u'informacion_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'informacion', ['tipo'])

        # Adding model 'activo'
        db.create_table(u'informacion_activo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['informacion.tipo'])),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('propietario', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('responsable', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('funcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('datos_personales', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'informacion', ['activo'])


    def backwards(self, orm):
        # Deleting model 'tipo'
        db.delete_table(u'informacion_tipo')

        # Deleting model 'activo'
        db.delete_table(u'informacion_activo')


    models = {
        u'informacion.activo': {
            'Meta': {'object_name': 'activo'},
            'activo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'datos_personales': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'funcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propietario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'responsable': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['informacion.tipo']"}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'informacion.tipo': {
            'Meta': {'object_name': 'tipo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['informacion']