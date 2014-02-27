# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'area'
        db.create_table(u'procesos_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'procesos', ['area'])

        # Adding model 'persona'
        db.create_table(u'procesos_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.area'])),
        ))
        db.send_create_signal(u'procesos', ['persona'])

        # Adding model 'proceso'
        db.create_table(u'procesos_proceso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('responsable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.persona'])),
        ))
        db.send_create_signal(u'procesos', ['proceso'])

        # Adding model 'tipo'
        db.create_table(u'procesos_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'procesos', ['tipo'])

        # Adding model 'entrada'
        db.create_table(u'procesos_entrada', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.tipo'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('proceso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.proceso'])),
            ('es_salida', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'procesos', ['entrada'])

        # Adding model 'salida'
        db.create_table(u'procesos_salida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.tipo'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('proceso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.proceso'])),
            ('es_entrada', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'procesos', ['salida'])

        # Adding model 'procedimiento'
        db.create_table(u'procesos_procedimiento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proceso', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.proceso'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('entrada', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.entrada'])),
            ('salida', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.salida'])),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.area'])),
        ))
        db.send_create_signal(u'procesos', ['procedimiento'])

        # Adding model 'actividad'
        db.create_table(u'procesos_actividad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('procedimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['procesos.procedimiento'])),
        ))
        db.send_create_signal(u'procesos', ['actividad'])


    def backwards(self, orm):
        # Deleting model 'area'
        db.delete_table(u'procesos_area')

        # Deleting model 'persona'
        db.delete_table(u'procesos_persona')

        # Deleting model 'proceso'
        db.delete_table(u'procesos_proceso')

        # Deleting model 'tipo'
        db.delete_table(u'procesos_tipo')

        # Deleting model 'entrada'
        db.delete_table(u'procesos_entrada')

        # Deleting model 'salida'
        db.delete_table(u'procesos_salida')

        # Deleting model 'procedimiento'
        db.delete_table(u'procesos_procedimiento')

        # Deleting model 'actividad'
        db.delete_table(u'procesos_actividad')


    models = {
        u'procesos.actividad': {
            'Meta': {'object_name': 'actividad'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'procedimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.procedimiento']"})
        },
        u'procesos.area': {
            'Meta': {'object_name': 'area'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'procesos.entrada': {
            'Meta': {'object_name': 'entrada'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'es_salida': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proceso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.proceso']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.tipo']"})
        },
        u'procesos.persona': {
            'Meta': {'object_name': 'persona'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.area']"}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'procesos.procedimiento': {
            'Meta': {'object_name': 'procedimiento'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.area']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'entrada': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.entrada']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'proceso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.proceso']"}),
            'salida': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.salida']"})
        },
        u'procesos.proceso': {
            'Meta': {'object_name': 'proceso'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'responsable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.persona']"})
        },
        u'procesos.salida': {
            'Meta': {'object_name': 'salida'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'es_entrada': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proceso': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.proceso']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['procesos.tipo']"})
        },
        u'procesos.tipo': {
            'Meta': {'object_name': 'tipo'},
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['procesos']