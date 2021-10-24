from django.shortcuts import render, HttpResponse

def reddit_auth_redirect(request) : 

    return HttpResponse("<h1>You have hit reddit_auth_redirect {}</h1>".format(str))

def concordancer_base(request) : 

    return HttpResponse("<h1>You have hit concordancer_base</h1>")