from django.db import models



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
    is_for_sale = models.BooleanField( default=False )

    groups = models.ManyToManyField( SakuhinGroup )

    def __unicode__( self ):
        return self.title

