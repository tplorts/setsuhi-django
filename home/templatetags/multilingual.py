from django import template

register = template.Library()

ML_CONTEXT_KEY = "ml_active_language"

@register.inclusion_tag('multilingual.html', takes_context=True)
def ml(context, *args, **kwargs):
    return {
        'multilingual_text': kwargs,
        'selected_language': context[ML_CONTEXT_KEY]
    }


@register.tag
def multilingual(parser, token):
    nodes = parser.parse(('endmultilingual',))
    parser.delete_first_token()
    return MultilingualNode(nodes)


@register.tag(name='mlpart')
def multilingual_part(parser, token):
    try:
        tag_name, lang_code = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("The %r tag requires a single argument: the language code representing the language of the contained content.  How many times do we have to have this conversation?" % token.contents.split()[0])
    if not (lang_code[0] == lang_code[-1] and lang_code[0] in ('"', "'")):
        raise template.TemplateSyntaxError("The language code argument, %r, should be in quotes" % lang_code)
    lang_code = lang_code[1:-1]
    nodes = parser.parse(('endmlpart',))
    parser.delete_first_token()
    return MultilingualPartNode(nodes, lang_code)




class MultilingualNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return '<span class="ml">' + output + '</span>'



class MultilingualPartNode(template.Node):
    def __init__(self, nodelist, language_code):
        self.nodelist = nodelist
        self.language_code = language_code

    def render(self, context):
        output = self.nodelist.render(context)
        l = self.language_code
        if l == context[ML_CONTEXT_KEY]:
            c = "ml-on"
        else:
            c = "ml-off"
        return '<div lang="'+l+'" class="'+c+'">' + output + '</div>'
