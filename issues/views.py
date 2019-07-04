from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django.urls import reverse
from issues.models import Issues,Issuelists
from material.models import ResinLabel
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
def index(request):
    isssues = Issues.objects.all()
    isssuemeterials = Issuelists.objects.all()
    return render(request,'issues/index.html',{"isssues":isssues,"issumeters":isssuemeterials})



def search(request):
    search_name = request.POST.get('search')
    # isssues = Issues.objects.filter(id=search_name)
 #   isssues = get_list_or_404(Issues,id=search_name)
    isssues = Issues.objects.filter(Q(issueType__contains=search_name)|Q(issue__contains=search_name)|
                                    Q(reason__contains=search_name)|Q(solution__contains=search_name))

    return render(request, 'issues/index.html', {"isssues":isssues})

@login_required(login_url='/account/login/')
def addtion(request):
    if request.method=='POST':
        clean_data = request.POST
        issuetype = clean_data.get('issuetype')
        issue = clean_data.get('issue')
        reason = clean_data.get('reason')
        solution = clean_data.get('solution')

        Issues.objects.create(issueType=issuetype,issue=issue,reason=reason,solution=solution)
        # return render(request, 'material/addition.html')
        return redirect(reverse('issues:index', args=()))

    return render(request, 'issues/addition.html')

@login_required(login_url='/account/login/')
def modifys(request,issueid):
    issue = Issues.objects.get(id=issueid)
    if request.method=='POST':
        clean_data = request.POST
        issue = clean_data.get('issue')
        reason = clean_data.get('reason')
        solution = clean_data.get('solution')
        Issues.objects.filter(id=issueid).update(issue=issue,reason=reason,solution=solution)

        return redirect(reverse('issues:index', args=()))
    return render(request,'issues/modiftion.html',{"issue":issue})

@login_required(login_url='/account/login/')
def issuemeterial_addtion(request):
    if request.method=='POST':
        clean_data = request.POST
        pubtime = clean_data.get('pubtime')
        meterial = clean_data.get('meterial')
        ColumnID = clean_data.get('ColumnID')
        issuetype = clean_data.get('issuetype')
        Practiceissue = clean_data.get('Practiceissue')
        solutionMethod = clean_data.get('solutionMethod')
        meterial_id = ResinLabel.objects.get(resinName=meterial).id
        issue_id = Issues.objects.get(issueType=issuetype).id

        Issuelists.objects.create(pubtime=pubtime,meterial_id=meterial_id,issue_id=issue_id,ColumnID=ColumnID,Practiceissue=Practiceissue,solutionMethod=solutionMethod)
      #  Issues.objects.create(issueType=issuetype,issue=issue,reason=reason,solution=solution)
        # return render(request, 'material/addition.html')
        return redirect(reverse('issues:index', args=()))

    return render(request, 'issues/addtion_issuemeter.html')


def issuemeterial_search(request):
    search_name = request.POST.get('issue_search')
    print(search_name)
    # isssues = Issues.objects.filter(id=search_name)
    # isssuemeterials = get_list_or_404(Issuelists,id=search_name)
    isssuemeterials = []
    for resin in ResinLabel.objects.filter(resinName__contains=search_name):
        isssuemeterials.extend(resin.meterialsmete.all())
    isssuemeterials.extend(Issuelists.objects.filter(Q(Practiceissue__contains=search_name) | Q(ColumnID__contains=search_name) |
                                    Q(solutionMethod__contains=search_name)))
    # isssuemeterials = Issuelists.objects.filter(Practiceissue__contains=search_name)

    return render(request, 'issues/index.html', {"issumeters":isssuemeterials})


@login_required(login_url='/account/login/')
def issuemeterial_modify(request,issuemeterid):
    meterissues = Issuelists.objects.get(id=issuemeterid)
    if request.method == 'POST':
        clean_data = request.POST
        pubtime = clean_data.get('pubtime')
        meterial = clean_data.get('meterial')
        ColumnID = clean_data.get('ColumnID')
        issuetype = clean_data.get('issuetype')
        Practiceissue = clean_data.get('Practiceissue')
        solutionMethod = clean_data.get('solutionMethod')
        meterial_id = ResinLabel.objects.get(resinName=meterial).id
        issue_id = Issues.objects.get(issueType=issuetype).id
        #Issues.objects.filter(id=issueid).update(issue=issue, reason=reason, solution=solution)
        Issuelists.objects.filter(id=issuemeterid).update(pubtime=pubtime,meterial_id=meterial_id,issue_id=issue_id,ColumnID=ColumnID,Practiceissue=Practiceissue,solutionMethod=solutionMethod)

        return redirect(reverse('issues:index', args=()))
    return render(request, 'issues/modiftion_issuemeter.html', {"meterissues": meterissues})