from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def class_for_language(context, lang):
    if context["ml_active_language"] == lang:
        return "ml-on"
    else:
        return "ml-off"



@register.inclusion_tag('tags/multilingual.html', takes_context=True)
def ml(context, *args, **kwargs):
    context["multilingual_text"] = kwargs
    return context


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
        c = class_for_language( context, l )
        return '<div lang="'+l+'" class="'+c+'">' + output + '</div>'
