from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}

    return render(request, 'ruiyang_website/index.html', context)

def blog_index(request):
    context = {}

    return render(request, 'ruiyang_website/blog_index.html', context)

def blog_content(request, blog_id):
    context = {}

    return render(request, 'ruiyang_website/blog/%d.html' % (blog_id), context)