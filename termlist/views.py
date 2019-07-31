from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q
from django.contrib.auth.models import Group,Permission
from .models import ApplicationTable

# Create your views here.

def index(requests):
    return render(requests,'termlist/index.html')

def search(requests):
    productnumber = requests.POST.get('productnumber')
    producttime = requests.POST.get('producttime')
    applications = ApplicationTable.objects.filter(productnumber=productnumber)
    if not applications:
        applications = ApplicationTable.objects.filter(producttime=producttime)
    return render(requests,'termlist/showpages.html',{'applications':applications})

@login_required(login_url='/account/login/')
def addtion(requests):
    if requests.method == 'POST':
        clean_data = requests.POST
        productnumber = clean_data.get('productnumber')
        producttime = clean_data.get('producttime')
        editorstaff = clean_data.get('editorstaff')
        resinname = clean_data.get('resinname')
        cycletime = clean_data.get('cycletime')
        public = clean_data.get('public')
        diameter = clean_data.get('diameter')
        height = clean_data.get('height')
        volumn = clean_data.get('volumn')
        storage = clean_data.get('storage')
        hetp = clean_data.get('hetp')
        AS = clean_data.get('AS')
        nppeditorstaff = clean_data.get('nppeditorstaff')
        cat = clean_data.get('cat')
        lot = clean_data.get('lot')
        expire = clean_data.get('expire')
        resinid = clean_data.get('resinid')
        usedtime = clean_data.get('usedtime')
        feedbackeditor = clean_data.get('feedbackeditor')
        maxpressure = clean_data.get('maxpressure')
        maxvictory = clean_data.get('maxvictory')
        ApplicationTable.objects.create(productnumber=productnumber,producttime=producttime,editorstaff=editorstaff,
                                        resinname=resinname,cycletime=cycletime,public=public,diameter=diameter,height=height,
                                        volumn=volumn,storage=storage,hetp=hetp,AS=AS,nppeditorstaff=nppeditorstaff,cat=cat,
                                        lot=lot,expire=expire,resinid=resinid,usedtime=usedtime,feedbackeditor=feedbackeditor,
                                        maxpressure=maxpressure,maxvictory=maxvictory
                                        )

        return render(requests,'termlist/index.html')
    return render(requests,'termlist/addtion.html')


@login_required(login_url='/account/login/')
def modifys(requests,productid):
    application = ApplicationTable.objects.get(id=productid)
    if requests.method == 'POST':
        clean_data = requests.POST
        applicationtables = ApplicationTable.objects.filter(id=productid)
        productnumber = clean_data.get('productnumber')
        producttime = clean_data.get('producttime')
        editorstaff = clean_data.get('editorstaff')
        resinname = clean_data.get('resinname')
        cycletime = clean_data.get('cycletime')
        public = clean_data.get('public')
        diameter = clean_data.get('diameter')
        height = clean_data.get('height')
        volumn = clean_data.get('volumn')
        storage = clean_data.get('storage')
        hetp = clean_data.get('hetp')
        AS = clean_data.get('AS')
        nppeditorstaff = clean_data.get('nppeditorstaff')
        cat = clean_data.get('cat')
        lot = clean_data.get('lot')
        expire = clean_data.get('expire')
        resinid = clean_data.get('resinid')
        usedtime = clean_data.get('usedtime')
        feedbackeditor = clean_data.get('feedbackeditor')
        maxpressure = clean_data.get('maxpressure')
        maxvictory = clean_data.get('maxvictory')
        ApplicationTable.objects.filter(id=productid).update(productnumber=productnumber, producttime=producttime, editorstaff=editorstaff,
                                        resinname=resinname, cycletime=cycletime, public=public, diameter=diameter,
                                        height=height,
                                        volumn=volumn, storage=storage, hetp=hetp, AS=AS, nppeditorstaff=nppeditorstaff,
                                        cat=cat,
                                        lot=lot, expire=expire, resinid=resinid, usedtime=usedtime,
                                        feedbackeditor=feedbackeditor,
                                        maxpressure=maxpressure, maxvictory=maxvictory
                                        )
        return render(requests,'termlist/showpages.html',{'applications':applicationtables})
    return render(requests,'termlist/modify.html',{'application':application})