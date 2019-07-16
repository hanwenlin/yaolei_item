from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import ResinLabel
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
    materials = ResinLabel.objects.all()
    return render(request,'material/index.html',{"materials":materials})


@login_required(login_url='/account/login/')
def delete(request,meterid):
    user = request.user
    print(user)
    print(user.user_permissions.all())
    if user.has_perm('material.delete_resinlabel'):
        ResinLabel.objects.get(id=meterid).delete()
        return redirect(reverse('material:index',args=()))
    else:
        return HttpResponse('Forbidden')

def search(request):
    search_name = request.POST.get('search')
    materials = ResinLabel.objects.filter(Q(resinaType__contains=search_name)|Q(resinName__contains=search_name)|
                                          Q(brand__contains=search_name)|Q(matrix__contains=search_name)|Q(ligand__contains=search_name)|
                                          Q(diameter__contains=search_name)|Q(Pmax__contains=search_name)|Q(phRange__contains=search_name)|
                                          Q(storageMethod__contains=search_name)|Q(compactFactor__contains=search_name)|Q(dbc__contains=search_name)|
                                          Q(LoadingRangeinProject__contains=search_name)|Q(PackingVmaxandPmax__contains=search_name)|Q(expiry__contains=search_name)|
                                          Q(TypeofColomuPackingMethod__contains=search_name)|Q(ColomuPackingMethod__contains=search_name)
                                          )
    return render(request,'material/index.html',{"materials":materials})


@login_required(login_url='/account/login/')
def addtion(request):
    if request.method=='POST':
        clean_data = request.POST

        resinName = clean_data.get('resinName')
        resinaType = clean_data.get('resinaType')
        brand = clean_data.get('brand')
        matrix = clean_data.get('matrix')
        ligand = clean_data.get('ligand')
        diameter = clean_data.get('diameter')
        Pmax = clean_data.get('Pmax')
        phRange = clean_data.get('phRange')
        storageMethod = clean_data.get('storageMethod')
        compactFactor = clean_data.get('compactFactor')
        dbc = clean_data.get('dbc')
        LoadingRangeinProject = clean_data.get('LoadingRangeinProject')
        PackingVmaxandPmax = clean_data.get('PackingVmaxandPmax')
        expiry = clean_data.get('expiry')
        TypeofColomuPackingMethod = clean_data.get('TypeofColomuPackingMethod')
        # print(TypeofColomuPackingMethod)
        ColomuPackingMethod = clean_data.get('ColomuPackingMethod')
        ResinLabel.objects.create(resinName=resinName,resinaType=resinaType,brand=brand,
                                 matrix=matrix,ligand=ligand,diameter=diameter,Pmax=Pmax,
                                  phRange=phRange,storageMethod=storageMethod,compactFactor=compactFactor,dbc=dbc,
                                  LoadingRangeinProject=LoadingRangeinProject,PackingVmaxandPmax=PackingVmaxandPmax,expiry=expiry,
                                  TypeofColomuPackingMethod=TypeofColomuPackingMethod,ColomuPackingMethod=ColomuPackingMethod)
        # return render(request, 'material/addition.html')

        return redirect(reverse('material:index', args=()))

    return render(request, 'material/addition.html')


@login_required(login_url='/account/login/')
def modifys(request,meterid):
    material = ResinLabel.objects.get(id=meterid)
    if request.method=='POST':
        clean_data = request.POST
        # clean_data = request.POST
        resinName = clean_data.get('resinName')
        resinaType = clean_data.get('resinaType')
        brand = clean_data.get('brand')
        matrix = clean_data.get('matrix')
        ligand = clean_data.get('ligand')
        diameter = clean_data.get('diameter')
        Pmax = clean_data.get('Pmax')
        phRange = clean_data.get('phRange')
        storageMethod = clean_data.get('storageMethod')
        compactFactor = clean_data.get('compactFactor')
        dbc = clean_data.get('dbc')
        LoadingRangeinProject = clean_data.get('LoadingRangeinProject')
        PackingVmaxandPmax = clean_data.get('PackingVmaxandPmax')
        expiry = clean_data.get('expiry')
        TypeofColomuPackingMethod = clean_data.get('TypeofColomuPackingMethod')
        print(TypeofColomuPackingMethod)

        ColomuPackingMethod = clean_data.get('ColomuPackingMethod')
        ResinLabel.objects.filter(id=meterid).update(resinName=resinName,resinaType=resinaType,brand=brand,
                                 matrix=matrix,ligand=ligand,diameter=diameter,Pmax=Pmax,
                                  phRange=phRange,storageMethod=storageMethod,compactFactor=compactFactor,dbc=dbc,
                                  LoadingRangeinProject=LoadingRangeinProject,PackingVmaxandPmax=PackingVmaxandPmax,
                                 expiry=expiry,TypeofColomuPackingMethod=TypeofColomuPackingMethod,ColomuPackingMethod=ColomuPackingMethod)
        return redirect(reverse('material:index', args=()))
    return render(request,'material/modiftion.html',{"material":material})