from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from applicantform. models import*

from django.contrib import messages

from django.http import FileResponse

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime

# from .forms import TeamForm

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    leader = Team.objects.all()
    context = {
        'leader':leader,
    }
    return render(request, 'dashboard/admin.html',context)

@login_required(login_url='login')
def leader_member(request,team_id):
    team = get_object_or_404(Team, id=team_id)
    team_members = TeamMember.objects.filter(team=team)
    context = {
        'team': team,
        'team_members': team_members,
    }
    return render(request, 'dashboard/applicantprofile.html',context)

@login_required(login_url='login')
def leader_all_data(request):
    alldata = Team.objects.all()
    context = {'alldata':alldata}
    return render(request,'dashboard/leader_all_data.html',context)


@login_required(login_url='login')
def adminstatus(request,pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status != team.status:
            if Team.objects.filter(status=status):
                team.status = status
                team.save()
            messages.success(request, 'You have updated the status ')
    context = {'team': team}
    return render(request, 'dashboard/applicantprofile.html',context)




@login_required(login_url='login')
# File Download
def download_file(request, team_id, field_name):
    team = get_object_or_404(Team, id=team_id)
    file_field = getattr(team, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')

@login_required(login_url='login')
def download_member_file(request, team_id, member_id, field_name):
    team_member = get_object_or_404(TeamMember, id=member_id, team__id=team_id)
    file_field = getattr(team_member, field_name)
    if file_field:
        response = FileResponse(file_field)
        response['Content-Disposition'] = f'attachment; filename="{file_field.name}"'
        return response
    else:
        messages.warning(request, f"No file found for {field_name}.")
    return redirect('/')
# End file Donload


# Accounts
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,"You are Login")
            return redirect('dashboard')
        else:
            error_message = "!!Username Or Password Incorrect"
            return redirect('login')
    else:
        return render(request,'dashboard/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                error_message="username taken"
            elif User.objects.filter(password=confirm_password).exists():
                error_message="Passwored taken"
            else:
                user = User.objects.create_user(username=username, password=confirm_password)
                user.save()
                return redirect('dashboard') 
        else:
            error_message = "Opps!!! Passwords Do Not Match.."
    else:
        error_message = ""
    return render(request,'dashboard/register.html',{'error_message':error_message})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
# End Accounts

# Search 
@csrf_exempt
def search_leaders(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        leaders = Leader.objects.filter(name__icontains=search_query)
        leaders_list = []
        for leader in leaders:
            leaders_list.append({
                'id': leader.id,
                'name': leader.name,
                'contact': leader.contact,
                'package': leader.package,
                'status': leader.status,
                'details_url': f"/leader/{leader.id}"
            })
        return JsonResponse({'leaders': leaders_list})
    else:
        return render(request, 'dashboard/admin.html')
# End Search


# Addmin Room Edit Function 
@login_required(login_url='login')
def team_edit(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        team.admin_checkin = request.POST['admin_checkin']
        team.admin_checkout = request.POST['admin_checkout']
        team.room_name = request.POST['room_name']
        team.admin_number_of_rooms = request.POST['admin_number_of_rooms']
        team.permit = request.POST['permit']
        team.save()
        messages.success(request, "Room  Updated")
        # return render(request, 'dashboard/applicantprofile.html',  team_id=team_id)
        # return redirect('/', team_id=team_id)
    return render(request, 'dashboard/applicantprofile.html', {'team': team})

