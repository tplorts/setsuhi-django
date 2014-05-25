from django.db import models
from django import forms
import json


def to_dict( str_or_json ):
    try:
        data = json.loads( str_or_json )
    except ValueError:
        data = str_or_json
    return data



class SakuhinInfoForm( forms.Form ):
    dbpk = forms.IntegerField()
    title = forms.CharField( max_length=60, required=False )
    brief = forms.CharField( max_length=200, required=False )
    lengthy = forms.CharField( widget=forms.Textarea, required=False )




class SakuhinGroup( models.Model ):
    name = models.CharField( max_length=100 )
    title = models.CharField( max_length=100 )
    is_shown = models.BooleanField( default=False )
    rank = models.FloatField( default=0 )

    def __unicode__( self ):
        return self.name

    def ml_title( self ):
        return to_dict( self.title )


class Sakuhin( models.Model ):
    main_image_url = models.URLField()
    thumb_image_url = models.URLField( blank=True )
    large_image_url = models.URLField( blank=True )

    title = models.CharField( max_length=60, blank=True )
    brief = models.CharField( max_length=200, blank=True )
    lengthy = models.TextField( blank=True )

    price = models.CharField( max_length=30, blank=True )
    is_for_sale = models.BooleanField( default=False )
    has_sold = models.BooleanField( default=False )

    def __unicode__( self ):
        if self.title and len(self.title) > 0:
            return self.title
        return self.main_image_url.split('/')[-1]

    def ml_title( self ):
        return to_dict( self.title )

    def ml_brief( self ):
        return to_dict( self.brief )
    
    def ml_lengthy( self ):
        return to_dict( self.lengthy )

    def updateInfo( self, infoForm ):
        if self.id != infoForm.cleaned_data["dbpk"]:
            return False
        self.title = infoForm.cleaned_data["title"]
        self.brief = infoForm.cleaned_data["brief"]
        self.lengthy = infoForm.cleaned_data["lengthy"]
        self.save()
        return True


class SakuhinEntry( models.Model ):
    sakuhin = models.ForeignKey( Sakuhin )
    group = models.ForeignKey( SakuhinGroup )
    rank = models.FloatField( default=0 )

    class Meta:
        unique_together = ("sakuhin", "group",)



################################################################



class EventCategory( models.Model ):
    name = models.CharField( max_length=100 )

    # Aside from the enfored requirements, what fields are
    # generally needed for this type of event?
    fields_recommended = models.CharField( max_length=200, blank=True )
    
    # Anything is not relevant to this type
    fields_not_applicable = models.CharField( max_length=200, blank=True )

    def __unicode__( self ):
        try:
            names = json.loads( self.name )
            if 'ja' in names:
                return names['ja']
            elif 'en' in names:
                return names['en']
            elif len(names) > 0:
                return names.items()[0]
            else:
                return "without name"
        except ValueError:
            return self.name


class EventPrice( models.Model ):
    # The 'door' price is to be used as the default
    # if there are no other price categories.
    door = models.DecimalField( max_digits=12, decimal_places=4 )
    ahead = models.DecimalField( max_digits=12, decimal_places=4, null=True )
    student = models.DecimalField( max_digits=12, decimal_places=4, null=True )
    senior = models.DecimalField( max_digits=12, decimal_places=4, null=True )
    child = models.DecimalField( max_digits=12, decimal_places=4, null=True )



class Event( models.Model ):
    # Verbal descriptions
    title = models.CharField( max_length=200 )
    brief = models.CharField( max_length=300, blank=True )
    lengthy = models.TextField( blank=True )
    
    # Temporal information
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    set_times = models.CharField( max_length=300, blank=True )

    # Location
    place = models.CharField( max_length=200 )
    place_website = models.URLField( blank=True )
    address = models.CharField( max_length=300, blank=True )
    directions = models.TextField( blank=True )

    # Type (category) live, workshop, etc.
    category = models.ForeignKey( EventCategory )

    # Price
    price = models.ForeignKey( EventPrice, null=True )

    # Other people
    members = models.TextField( blank=True )
    
    # Contact info for reservations etc.
    email = models.EmailField( max_length=254, blank=True )
    telephone = models.CharField( max_length=20, blank=True )
    reservation_url = models.URLField( blank=True )

    # Picture, just one for now
    picture = models.URLField( blank=True )

