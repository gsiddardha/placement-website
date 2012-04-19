from django.conf.urls.defaults import patterns

handler404 = "userportal.misc.util.not_found"
handler500 = "userportal.misc.util.server_error"

urlpatterns = patterns('placement.students.views',
                       (r'^register/$', 'register_student'),
                       (r'^login/$', 'login'),
                       (r'^logout/$', 'logout'),
)