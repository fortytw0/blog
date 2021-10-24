from django.shortcuts import render
import json

def blog_view(request, slug):
    template_path = 'blogs/'+ slug + '.html'
    return render(request, template_path, context={'show_about':False})

def blog_list_view(request) :

    '''
    TODO : Sort by date and consider pagination
    '''
    with open('manifest.json', 'r') as mj :
        manifest = json.load(mj)

    return render(request, 'content/blog_list.html', context={'blog_list':manifest})
    

def default_view(request) :
    return render(request, 'index.html', context={'show_about':True, 'old_nav':True})