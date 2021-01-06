from django.shortcuts import render
from .objectrecognition import ObjectRecognition
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def index(request):

    objecthandler = ObjectRecognition()
    recognized_object = objecthandler.doRecognition()
    pagetitle = "Electreeks®"
    subtitle = "Spyagent"
    context = {'pagetitle': pagetitle, 'subtitle': subtitle, 'recognized_object': recognized_object}
    return render(request, 'electreeksspy/index.html', context)
