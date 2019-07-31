from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import PressureandVelocity
from material.models import  ResinLabel
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def index(request):
    columns = PressureandVelocity.objects.all()
    return render(request,'columnstatictis/index.html',{"columns":columns})

@login_required(login_url='/account/login/')
def delete(request,column_id):
    user = request.user
    if user.has_perm('columnstatictis.delete_columnstatictis'):
        PressureandVelocity.objects.get(id=column_id).delete()
        return redirect(reverse('columnstatictis:index',args=()))
    else:
        message = '你没有删除该内容的权限'
        return render(request,'index/prompt_message.html',{"message":message})

def search(request):
    search_name = request.POST.get('search_column')
    # resinid = Meterials.objects.get(meterialName=search_name).id
    # columns = Columnstatictis.objects.filter(resin_id=resinid)
    columns = []
    if search_name == '':
        pass
        # return render(request, 'columnstatictis/index.html', {"columns": columns})
    else:
        for resin in ResinLabel.objects.filter(resinName__contains=search_name):
            columns.extend(resin.materisesin.all())
        columns.extend(PressureandVelocity.objects.filter(Q(columnid__contains=search_name)|Q(packingproject__contains=search_name)|
                                                     Q(resinid__contains=search_name)|Q(minipackingvelocity__contains=search_name)|
                                                     Q(maxpackingvelocity__contains=search_name)|Q(packingpressure__contains=search_name)|
                                                     Q(productionvelocity__contains=search_name)|Q(columnheight__contains=search_name)|Q(columndimeter__contains=search_name)|
                                                     Q(symmetry__contains=search_name)|Q(hetp__contains=search_name)|Q(comment__contains=search_name))
                       )
    return render(request,'columnstatictis/index.html',{"columns":columns})

@login_required(login_url='/account/login/')
def addtion(request):
    if request.method=='POST':
        clean_data = request.POST
        # clean_data = request.POST
        resin = clean_data.get('resin')
        packingproject = clean_data.get('packingproject')
        columnid = clean_data.get('columnid')
        resinid = clean_data.get('resinid')
        minipackingvelocity = clean_data.get('minipackingvelocity')
        maxpackingvelocity = clean_data.get('maxpackingvelocity')
        packingpressure = clean_data.get('packingpressure')
        productionvelocity = clean_data.get('productionvelocity')
        columnheight = clean_data.get('columnheight')
        columndimeter = clean_data.get('columndimeter')
        symmetry = clean_data.get('symmetry')
        hetp = clean_data.get('hetp')
        comment = clean_data.get('comment')
        resin_id = ResinLabel.objects.get(resinName=resin).id
        PressureandVelocity.objects.create(packingproject=packingproject,columnid=columnid,resinid=resinid,minipackingvelocity=minipackingvelocity,
                                       maxpackingvelocity=maxpackingvelocity,packingpressure=packingpressure,productionvelocity=productionvelocity,columnheight=columnheight,
                                       columndimeter=columndimeter,symmetry=symmetry,hetp=hetp,comment=comment,resin_id=resin_id)
        return redirect(reverse('columnstatictis:index', args=()))

    return render(request, 'columnstatictis/addition.html')

@login_required(login_url='/account/login/')
def modifys(request,column_id):
    user = request.user
    print(column_id)
    column = PressureandVelocity.objects.get(id=column_id)
    if request.method=='POST':
        clean_data = request.POST
        print(clean_data)
        # clean_data = request.POST
        resin = clean_data.get('resin')
        packingproject = clean_data.get('packingproject')
        columnid = clean_data.get('columnid')
        resinid = clean_data.get('resinid')
        minipackingvelocity = clean_data.get('minipackingvelocity')
        maxpackingvelocity = clean_data.get('maxpackingvelocity')
        packingpressure = clean_data.get('packingpressure')
        productionvelocity = clean_data.get('productionvelocity')
        columnheight = clean_data.get('columnheight')
        columndimeter = clean_data.get('columndimeter')
        symmetry = clean_data.get('symmetry')
        hetp = clean_data.get('hetp')
        comment = clean_data.get('comment')
        resin_id = ResinLabel.objects.get(resinName=resin).id
        print(columnid)
        # PressureandVelocity.objects.filter(id=columnid).update(clean_data)
        if user.has_perm('columnstatictis.change_columnstatictis'):
            PressureandVelocity.objects.filter(id=column_id).update(packingproject=packingproject,columnid=columnid,resinid=resinid,minipackingvelocity=minipackingvelocity,
                                           maxpackingvelocity=maxpackingvelocity,packingpressure=packingpressure,productionvelocity=productionvelocity,columnheight=columnheight,
                                           columndimeter=columndimeter,symmetry=symmetry,hetp=hetp,comment=comment, resin_id=resin_id)
        # PressureandVelocity.objects.filter(id=columnid).update(packingproject=packingproject, columnid=columnid,
        #                                                        resinid=resinid, minipackingvelocity=minipackingvelocity,
        #                                                        maxpackingvelocity=maxpackingvelocity,
        #                                                        packingpressure=packingpressure,
        #                                                        productionvelocity=productionvelocity,
        #                                                        columnheight=columnheight,
        #                                                        columndimeter=columndimeter, symmetry=symmetry,
        #                                                        hetp=hetp, comment=comment, resin_id=resin_id)
        else:
            message = '你没有修改的权限'
            return render(request, 'index/prompt_message.html', {"message": message})
        return redirect(reverse('columnstatictis:index', args=()))
    return render(request,'columnstatictis/modiftion.html',{"column":column})