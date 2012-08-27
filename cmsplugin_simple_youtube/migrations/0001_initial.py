# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SimpleYouTube'
        db.create_table('cmsplugin_simple_youtube_simpleyoutube', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('autoplay', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('custom_thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('cmsplugin_simple_youtube', ['SimpleYouTube'])

        # Adding model 'SimpleYoutubePointer'
        db.create_table('cmsplugin_simpleyoutubepointer', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('youtube', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_simple_youtube.SimpleYouTube'])),
        ))
        db.send_create_signal('cmsplugin_simple_youtube', ['SimpleYoutubePointer'])


    def backwards(self, orm):
        
        # Deleting model 'SimpleYouTube'
        db.delete_table('cmsplugin_simple_youtube_simpleyoutube')

        # Deleting model 'SimpleYoutubePointer'
        db.delete_table('cmsplugin_simpleyoutubepointer')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_simple_youtube.simpleyoutube': {
            'Meta': {'object_name': 'SimpleYouTube'},
            'autoplay': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'custom_thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'cmsplugin_simple_youtube.simpleyoutubepointer': {
            'Meta': {'object_name': 'SimpleYoutubePointer', 'db_table': "'cmsplugin_simpleyoutubepointer'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'youtube': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_simple_youtube.SimpleYouTube']"})
        }
    }

    complete_apps = ['cmsplugin_simple_youtube']
