from django.shortcuts import render
import json
import time

def blog_view(request, slug):
    template_path = 'blogs/'+ slug + '.html'

    with open('slug_post.json', 'r') as mj :
        slug_post_map = json.load(mj)

    tag_list = slug_post_map[slug]['tag_slugs'] 

    return render(request, template_path, context={'show_about':False,  'tag_list_section_name' : 'Tags', 'tag_list':tag_list, 'display_tags_inline':True})

def blog_list_view(request) :

    with open('manifest.json', 'r') as mj :
        manifest = json.load(mj)
        ordered_manifest = sorted(manifest, key=lambda x : time.strptime(x['date'], "%m-%d-%Y"), reverse=True)

    return render(request, 'index.html', context={'blog_list':ordered_manifest})
    

def default_view(request) :

    with open('manifest.json', 'r') as mj :
            manifest = json.load(mj)

    ordered_manifest = sorted(manifest, key=lambda x : time.strptime(x['date'], "%m-%d-%Y"), reverse=True)
    
    if len(ordered_manifest)>5 :
        ordered_manifest = ordered_manifest[:5]
     
    return render(request, 'index.html', context={'show_about':True, 'old_nav':True, 'blog_list_section_name' : "Recent Blogs",  'blog_list':ordered_manifest})


def tag_view(request, tag) : 

    with open('tag_post.json', 'r') as f : 
        tag_post_map = json.load(f)

    blog_list = tag_post_map[tag]

    print(tag)

    return render(request, 'index.html', context={'show_about':False, 'blog_list_section_name' : tag,  'blog_list':blog_list})

def tag_list_view(request) : 

    with open('tags.json', 'r') as f : 
        tag_map = json.load(f)
        tag_list = [{'tag_name': key, 'tag_slug':value} for key, value in tag_map.items()]

    return render(request, 'index.html', context={'show_about':False, 'tag_list_section_name' : 'Recent Tags',  'tag_list':tag_list})



