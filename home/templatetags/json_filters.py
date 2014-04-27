# https://djangosnippets.org/snippets/201/

from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils import simplejson
from django.template import Library

register = Library()

@register.filter
def jsonify(obj):
    if isinstance(obj, QuerySet):
        return serialize('json', obj)
    return simplejson.dumps(obj)


@register.filter
def jsonify_expand(obj, to_expand):
    return serialize('json', obj, relations=(to_expand,))
