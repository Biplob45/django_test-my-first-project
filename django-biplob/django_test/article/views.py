from django.shortcuts import render
from django.http import HttpResponse    
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.template import Context
from article.models import Article, Comment  #4th viodeo ar jonno; 
#13th video ar jonno hobe
#14th video te Comment ta jog hobe
from forms import ArticleForm, CommentForm #12th video  #14th video te Comment hobe
from django.http import HttpResponseRedirect  #12th video  ##13th video ar jonno hobe
from django.core.context_processors import csrf  #12th video
from django.utils import timezone   #14th video

# Create your views here.

def articles(request):
    language = 'en-gb'   #4 line 8th video ata soho ar porer
    session_language = 'en-gb'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']
        
    #return render_to_response('articles.html',
                              #{'articles': Article.objects.all(),
                               # 'language' : language, 
                                #'session_language' : session_language})
    args = {}
    args.update(csrf(request))
    
    args['articles'] = Article.objects.all()
    args['language']  = language
    args['session_language'] = session_language
    
    return render_to_response('articles.html', args)

#8th video te akane uporer line ta jog hobe
#4th videoarjonnuporer dui line.

def article(request,article_id=1):
    return render_to_response('article.html',
                              {'article':Article.objects.get(id=article_id) }) 
#4th video ar jonno,

def language(request,language = 'en-gb'): #8th video te ai para ta hobe 
    response = HttpResponse("setting language to %s " % language)
    response.set_cookie('lang',language)
    request.session['lang'] = language    
    
    return response


def hello(request):
    name = "biplob"
    html = "<html><body>Hi %s,this seems to have worked!</body></html>" %name
    return HttpResponse(html)

def hello_template(request):
    name = "biplob"
    t = get_template('hello.html')
    html= t.render(Context({'name':name}))
    return HttpResponse(html)

def hello_template_simple(request):    #(uporer kajtake shortkate dekaice,,,,uporere ta #otoba aita jekono akta leklei hobe;
    name='biplob'
    return render_to_response('hello.html',{'name':name})


class HelloTemplate(TemplateView):
    
    template_name = 'hello_class.html'
    
    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name']='biplob'
        return context
    

def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)    #15th video te (request.FILES)8
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
    args = {}
    args.update(csrf(request))
        
    args['form'] = form
        
    return render_to_response('create_article.html', args)

def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    return HttpResponseRedirect('/articles/get/%s' %article_id)

def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()
            
            return HttpResponseRedirect('/articles/get/%s' % article_id)
        
    else:
        f = CommentForm()
    args = {}
    args.update(csrf(request))
    
    args['article'] = a
    args['form'] = f
    
    return render_to_response('add_comment.html', args)

def search_titles(request):   #16th video ar pera
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text= ''
        
    articles = Article.objects.filter(title__contains=search_text)
    
    return render_to_response('ajax_search.html', {'articles' : articles})

        