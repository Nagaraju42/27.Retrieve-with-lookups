from django.shortcuts import render
from app.models import *
# Create your views here.
from django.db.models.function import length
from django.db.models import Q

def topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',d)


def webpage(request):
    LOW=Webpage.objects.all()
    #LOW=Webpage.objects.filter(topic_name='cricket')
    #LOW=Webpage.objects.exclude(topic_name='cricket')
    #LOW=Webpage.objects.all().order_by('name')
    #LOW=Webpage.objects.all().order_by('-name')
    #LOW=Webpage.objects.all()[1:2:]
    #LOW=Webpage.objects.all().order_by(length('name'))
    #LOW=Webpage.objects.all().order_by(length('name').desc())
    #LOw=Webpage.objects.all()
    #LOW=Webpage.objects.filter(name__startswith='k')
    #LOW=Webpage.objects.filter(email__endswith='.com')
    #LOW=Webpage.objects.filter(name__contains='s')
    #LOw=Webpage.objects.filter(name__in=('Dhoni','zehra'))
    #LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{7}')
    #LOW=Webpage.objects.filter(Q(topic_name='cricket') & Q(name='dhoni'))
    #LOW=Webpage.object.filter(Q(topic_name='cricket'))
    d={'webpages':LOW}
    return render(request,'display_webpages.html',d)


def access(request):
    LOA=AccessRecord.objects.all()
    #LOA=AccessRecord.objects.filter(date__gt='2022-05-09')
    #LOA=AccessRecord.objects.filter(date__gte='2022-11-24')
    #LOA=AccessRecord.objects.filter(date__lt='2022-11-24')
    #LOA=AccessRecord.objects.filter(date__lte='2022-05-09')
    #LOA=AccessRecord.objects.filter(date__year='2023')
    #LOA=AccessRecord.objects.filter(date__day='9')
    #LOA=AccessRecord.objects.filter(date__year__gt='2022')
    #LOA=AccessRecord.objects.filter(date__month__lt='10')
    

    d={'access':LOA}
    return render(request,'display_accessrecord.html',d)
