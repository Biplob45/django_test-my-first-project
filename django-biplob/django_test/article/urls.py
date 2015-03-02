from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
      url(r'^all/$','article.views.articles'),                       
      url(r'^get/(?P<article_id>\d+)/$','article.views.article'),
      url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),
      url(r'^create/$', 'article.views.create'),  #12th video;;
      #uporer line ta 8th video ar jonno
      url(r'^like/(?P<article_id>\d+)/$','article.views.like_article'), #13th video
      url(r'^add_comment/(?P<article_id>\d+)/$','article.views.add_comment'), #14th video
      
      url(r'^search/$', 'article.views.search_titles'),  #16th video
)
