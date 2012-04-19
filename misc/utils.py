import settings

from django.template.context import RequestContext
from django.http import HttpResponseRedirect

def clean_string( dirty_string ):
    word_list = dirty_string.split(" ")
    word_list = (s.title().replace('\'S','\'s') for s in word_list)
    cleaned_string =" ".join(word_list)
    return cleaned_string

# Generates a context with the most used variables
def global_context(request):
    user_type = 'Anon'
    if request.user.is_authenticated():
        if request.user.groups.filter(name="Students"):
            user_type = 'Student'
        elif request.user.groups.filter(name="Companies"):
            user_type = 'Company'
        elif request.user.groups.filter(name="Admin"):
            user_type = 'Admin'
    context =  RequestContext (request,
                               {'user':request.user,
                                'SITE_URL':settings.SITE_URL,
                                'MEDIA_URL':settings.MEDIA_URL,
                                'SITE_NAME':settings.SITE_NAME,
                                'user_type': user_type
                                }
                               )
    return context

# Take care of session variable
def session_get(request, key, default = False):
    value = request.session.get(key, False)
    if value:
        pass
        del request.session[key]
    else: 
        value = default
    return value

# Decorators

# For urls that can't be accessed once logged in.
def no_login (func):
    def wrapper (*__args, **__kwargs):
        request = __args[0]
        if request.user.is_authenticated():
            # Return here after logging in
            request.session['already_logged'] = True
            return HttpResponseRedirect("%s/students/" % settings.SITE_URL)
        else:
            return func (*__args, **__kwargs)
    return wrapper
