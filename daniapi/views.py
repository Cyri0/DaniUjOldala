from django.http import JsonResponse
from .models import Blogpost, Tag

def endpoints(request):
    commands = {
        'api/':'Load this page',
        'api/posts/ + GET':'Return all posts',
        'api/post/[id]/ + GET':'Return one specific post',
        'api/tags/ + GET':'Return all tag type',
        'api/tag/[id]/ + GET':'Return one specific tag',
        'api/postbytag/[tagid]/ + GET':'Return all post with the tag[id]',
    }

    return JsonResponse(commands)


def getallposts(request):
    allpost = Blogpost.objects.all()

    datas = { 'data' : [] }

    for post in allpost:
        datas['data'].append(post.serialize())

    return JsonResponse(datas)


def getpost(request, id):
    post = Blogpost.objects.get(id=id)
    return JsonResponse(post.serialize())

def getalltags(request):
    tags = Tag.objects.all()

    datas = { 'data' : [] }

    for tag in tags:
        datas['data'].append(tag.serialize())

    return JsonResponse(datas)

def gettag(request, id):
    post = Tag.objects.get(id=id)
    return JsonResponse(post.serialize())

def postbytag(request, id):
    datas = {'data':[]}
    posts = Blogpost.objects.all()

    for post in posts:
        taglist = post.tag_list()
        print(taglist)
        if int(id) in taglist:
            datas['data'].append(post.serialize())
    return JsonResponse(datas)
