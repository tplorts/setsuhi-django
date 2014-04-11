from django.db import models
from django import forms



class SakuhinInfoForm( forms.Form ):
    dbpk = forms.IntegerField()
    title = forms.CharField( max_length=60, required=False )
    brief = forms.CharField( max_length=200, required=False )
    lengthy = forms.CharField( widget=forms.Textarea, required=False )




class SakuhinGroup( models.Model ):
    name = models.CharField( max_length=100 )

    def __unicode__( self ):
        return self.name


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
    order_index = models.IntegerField( default=0 )

    class Meta:
        unique_together = ("sakuhin", "group",)
