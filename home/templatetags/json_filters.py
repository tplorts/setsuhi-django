# https://djangosnippets.org/snippets/201/

from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.template import Library
import json


register = Library()


class DefaultJSONEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


@register.filter
def jsonify(obj):
    if isinstance(obj, QuerySet):
        return serialize('json', obj)
    return json.dumps(obj, cls=DefaultJSONEncoder)


@register.filter
def jsonify_expand(obj, to_expand):
    return serialize('json', obj, relations=(to_expand,))
