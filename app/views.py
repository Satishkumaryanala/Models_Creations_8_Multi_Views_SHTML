from django.shortcuts import render
from app.models import *
# Create your views here.

def display_topic(request):
    QSTO = Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO = webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_Access(request):
    QSAO = AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_Access.html',d)

def insert_topic(request):
    topic_name=input('Enter a topic_name : ')
    to = Topic.objects.get_or_create(topic_name=topic_name)[0]
    to.save()
    QSTO = Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    tn = input('Enter topic_name : ')
    to = Topic.objects.get(topic_name=tn)
    name=input('Enter a name : ')
    url=input('Enter url : ')
    wo = webpage.objects.get_or_create(topic_name=to,name=name,url=url)[0]
    wo.save()
    QSWO = webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def insert_Access(request):
    pk=input('Enter PK value : ')
    wo = webpage.objects.get(pk=pk)
    date = input('Enter a date in format yyyy-mm-dd : ')
    author = input('Enter author name : ')
    email = input('Enter email : ')
    AO = AccessRecord.objects.get_or_create(name=wo,date=date,author=author,email=email)[0]
    AO.save()
    QSAO = AccessRecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_Access.html',d)