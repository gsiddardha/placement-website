from django.conf.urls.defaults import patterns

handler404 = "userportal.misc.util.not_found"
handler500 = "userportal.misc.util.server_error"

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^placement/', include('placement.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include('placement.admin')),
    (r'^students/', include('placement.students.urls')),
    (r'^company/', include('placement.companies.urls')),
)
