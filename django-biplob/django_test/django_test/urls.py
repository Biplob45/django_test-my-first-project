from django.conf.urls import patterns, include, url  #5th video teo hobe
from django.conf import settings  #7th video
from django.conf.urls.static import static #7th video
from article.views import HelloTemplate
from django.contrib import admin
admin.autodiscover()  #5th video
urlpatterns = patterns('',
    url(r'^articles/',include('article.urls')), #4th video ar jonno
    # Examples:
    url(r'^hello/$', 'article.views.hello'),   
    #(hello holo just name ta,,,,  '  ' aita holo kotai ace;;)
    url(r'^hello_template/$','article.views.hello_template'),  
    url(r'^hello_class_view/$',HelloTemplate.as_view()),
    # url(r'^$', 'django_test.views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),   #test...calacci

    url(r'^admin/', include(admin.site.urls)),  #5th video teo hobe
    
    url(r'^accounts/login/$', 'django_test.views.login'), #9th video
    url(r'^accounts/auth/$', 'django_test.views.auth_view'), #9th video
    url(r'^accounts/logout/$', 'django_test.views.logout'),  #9th video
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),  #9th video
    url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),  #9th video
    url(r'^accounts/register/$', 'django_test.views.register_user'),  #10th video
    url(r'^accounts/register_success/$', 'django_test.views.register_success'),  
    #10th video
    
)+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)  #7th video

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root':settings.MEDIA_ROOT},)
         )