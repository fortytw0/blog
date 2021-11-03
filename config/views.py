from django.shortcuts import render
import json
import time

def blog_view(request, slug):
    template_path = 'blogs/'+ slug + '.html'
    return render(request, template_path, context={'show_about':False})

def blog_list_view(request) :

    with open('manifest.json', 'r') as mj :
        manifest = json.load(mj)
        ordered_manifest = sorted(manifest, key=lambda x : time.strptime(x['date'], "%d-%m-%Y"))

    

    return render(request, 'index.html', context={'blog_list':ordered_manifest})
    

def default_view(request) :

    with open('manifest.json', 'r') as mj :
            manifest = json.load(mj)

    ordered_manifest = sorted(manifest, key=lambda x : time.strptime(x['date'], "%d-%m-%Y"))
    
    if len(ordered_manifest)>5 :
        ordered_manifest = ordered_manifest[:5]
     
    return render(request, 'index.html', context={'show_about':True, 'old_nav':True, 'blog_list_section_name' : "Recent Blogs",  'blog_list':ordered_manifest})


def tag_view(request, tag) : 

    with open('tag_post.json', 'r') as f : 
        tag_post_map = json.load(f)

    blog_list = tag_post_map[tag]

    return render(request, 'index.html', context={'show_about':False, 'blog_list_section_name' : tag,  'blog_list':blog_list})