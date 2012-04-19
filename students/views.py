import forms
import models
import settings
from misc.utils import clean_string, global_context, no_login, session_get

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template.context import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.core.mail import send_mail


def register_student(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = forms.RegisterUserForm(data)
        
        if form.is_valid():
            if form.cleaned_data["password"] == form.cleaned_data["password_again"]:
                user = User.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password = form.cleaned_data['password']
                )
                college=form.cleaned_data['college']

                user_profile = models.UserProfile (
                        user = user,
                        first_name = form.cleaned_data['first_name'],
                        last_name = form.cleaned_data['last_name'],
                        mobile_number = form.cleaned_data['mobile_number'],
                        gender = form.cleaned_data['gender'],
                        department = clean_string(form.cleaned_data['department']),
                        joinYear = form.cleaned_data['join_year'],
                        stream = form.cleaned_data['stream'],
                        email = form.cleaned_data['email'],
                        cgpa = form.cleaned_data['cgpa'],
                        profile_not_set = True
                    )
                user.save()
                user_profile.save()
                request.session ["registered"] = True
                
                mail_subject = "Placements 2013 - Registration Successful"
                mail_template = get_template('email/stu_regn_success.html')
                mail_body = mail_template.render(Context({'username':user.username,}))
                
                send_mail(mail_subject, mail_body, 'no-reply@placements.iitm.ac.in', [user.email,], fail_silently=False)
                return HttpResponseRedirect("%s/students/login/" % settings.SITE_URL)
    else: 
        form = forms.RegisterUserForm()

    return render_to_response('registration/register_student.html', locals(), context_instance = global_context(request))

@no_login
def login(request):
    redirected = request.session.get("from_url", False)
    registered = session_get(request, "registered")

    if request.method == 'POST':
        data = request.POST.copy()
        form = forms.StudentLoginForm (data)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data["password"])
            if user is not None:
                auth.login (request, user)
                url = session_get(request, "from_url")
                
                # Handle redirection
                if not url:
                    url = "%s/students/" % settings.SITE_URL
                    request.session['logged_in'] = True

                return HttpResponseRedirect(url)
            else:
                request.session['invalid_login'] = True
                return HttpResponseRedirect(request.path)
    else: 
        invalid_login = session_get(request, "invalid_login")
        form = forms.StudentLoginForm ()

    return render_to_response('students/login.html', locals(), context_instance= global_context(request))

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect("%s/" % settings.SITE_URL)