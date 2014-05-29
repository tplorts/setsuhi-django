from django.contrib import admin
from django import forms
import json
import math
from chosen import forms as chzn
from home import models
from setsuhi import settings

import logging
logger = logging.getLogger(__name__)


admin.site.register( models.Sakuhin )
admin.site.register( models.SakuhinGroup )


class LingualInput( forms.TextInput ):
    def __init__( self, lang, attrs=None ):
        self.language = lang
        super(LingualInput, self).__init__( attrs )

    def render( self, name, value, attrs=None ):
        html = super(LingualInput, self).render( name, value, attrs )
        d0 = '<div class="lingual-input">'
        dl = '<div class="language-label">'+self.language+'</div>'
        de = '</div>'
        return d0+dl+html+de


class MultilingualWidget( forms.MultiWidget ):
    def __init__( self, attrs=None ):
        widgets = [LingualInput(lang, attrs) for lang in settings.languages]
        super( MultilingualWidget, self ).__init__( widgets, attrs )

    def decompress( self, value ):
        if value:
            try:
                ml = json.loads( value )
                return [ml[lang] if lang in ml else None for lang in settings.languages]
            except ValueError:
                return [value] + [None]*(len(settings.languages) - 1)
        else:
            return [None] * len(settings.languages)


maxl = 200
langn = len(settings.languages)
overhead = 10*langn + 1
maxperl = math.floor( (maxl - overhead)/langn )

class MultilingualField( forms.MultiValueField ):
    widget = MultilingualWidget()

    def __init__( self, *args, **kwargs ):
        fields = (forms.CharField(max_length=maxperl),)*len(settings.languages)
        super(MultilingualField, self).__init__(fields, *args, **kwargs)

    def compress( self, data_list ):
        if len(data_list) == len(settings.languages):
            d = {}
            for i in range(len(settings.languages)):
                d.update({ settings.languages[i]: data_list[i] })
            store = json.dumps(d)
            return store
        else:
            return '/'.join( data_list )



eventFields = (
    'title','brief','lengthy','start_time','end_time',
    'set_times','place','place_website','address',
    'directions','category','members','email',
    'telephone','reservation_url','picture',
)
dummyEvent = models.Event()
def efname( f ):
    return models.Event._meta.get_field_by_name(f)[0].verbose_name
fieldChoices = [(f, efname(f)) for f in eventFields]

class CategoryForm( forms.ModelForm ):
    name = MultilingualField()
    fields_recommended = chzn.ChosenMultipleChoiceField(choices=fieldChoices)
    fields_not_applicable = chzn.ChosenMultipleChoiceField(choices=fieldChoices)
    class Meta:
        model = models.EventCategory
        fields = '__all__'

class EventCategoryAdmin( admin.ModelAdmin ):
    form = CategoryForm


class EventPriceInline( admin.TabularInline ):
    model = models.EventPrice

class EventAdmin( admin.ModelAdmin ):
    inlines = [
        EventPriceInline,
    ]


admin.site.register( models.EventCategory, EventCategoryAdmin )
admin.site.register( models.EventPrice )
admin.site.register( models.Event, EventAdmin )
