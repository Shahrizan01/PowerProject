from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Project, Room


# Create your views here.

def index(request):
    return render(request, 'display.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('userindex')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')

    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')

        # Check if passwords match
        if password != confirm_password:
            # Handle password mismatch error
            messages.error(request, 'Password do not match!')
            return redirect('signup')

        # Create user
        User.objects.create_user(
            email=email,
            password=password,
            username=username,
        )
        return redirect('login')

    return render(request, 'signup.html')


@login_required
def userindex_views(request):
    first_name = request.user.first_name
    last_name = request.user.last_name

    data = {
        'user': request.user,
        'name': first_name + ' ' + last_name,
    }

    return render(request, 'index.html', data)


@login_required
def homepage_view(request):
    return render(request, 'homepage.html')


@login_required
def logout_action(request):
    logout(request)
    return redirect('index')


@login_required
def dashboard_view(request):
    first_name = request.user.first_name
    last_name = request.user.last_name

    data = {
        'user': request.user,
        'name': first_name + ' ' + last_name,
    }
    return render(request, 'dashboard.html', data)


@login_required
def roomdetails_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    user = request.user

    if request.method == 'POST':
        for i in range(project.numroom):
            name = request.POST.get(f'nameroom_{i}')
            desc = request.POST.get(f'description_{i}')
            app = request.POST.get(f'apps_{i}')
            length = request.POST.get(f'length_{i}')
            width = request.POST.get(f'width_{i}')
            height = request.POST.get(f'height_{i}')
            color = request.POST.get(f'color_{i}')
            occupants = request.POST.get(f'occupants_{i}')
            window_num = request.POST.get(f'window_num_{i}')
            window_orientation = request.POST.get(f'window_orientation_{i}')
            window_size = request.POST.get(f'window_size_{i}')
            # illumination_req = request.POST.get(f'illumination_req_{i}')
            lamp_specs = request.POST.get(f'lamp_specs_{i}')
            aircond_type = request.POST.get(f'aircond_type_{i}')

            Room.objects.create(
                name=name,
                desc=desc,
                app=app,
                length=length,
                width=width,
                height=height,
                color=color,
                occupants=occupants,
                window_num=window_num,
                window_orientation=window_orientation,
                window_size = window_size,
                lamp_specs = lamp_specs,
                aircond_type = aircond_type,
                # illumination_req = illumination_req,
                project=project,
                created_by=user
            )

            # print(name, desc, app, length, width, height,
            #       color, occupants, window_num, window_orientation,
            #       window_size, lamp_specs, aircond_type)

        return redirect('project')

    data = {
        'user': user,
        'range': range(project.numroom),
        'project': project,
    }
    return render(request, 'mainpage2.html', data)


@login_required
def createproject_view(request):
    user = request.user
    if request.method == 'POST':
        projectname = request.POST.get('projectname')
        numroom = request.POST.get('numroom')
        project = Project.objects.create(
            name=projectname,
            numroom=numroom,
            created_by=user,
        )
        return redirect('rooms/'+str(project.id))

    data = {
        'user': user,
    }

    return render(request, 'newproject.html', data)


@login_required
def existproject_view(request):
    user = request.user
    projects = Project.objects.filter(created_by=user)

    data = {
        'user': user,
        'projects': projects,
    }
    return render(request, 'existproject.html', data)


@login_required
def projectdetails_view(request, project_id):
    user = request.user
    project = get_object_or_404(Project, id=project_id)
    rooms = Room.objects.filter(project=project)

    data = {
        'user': user,
        'project': project,
        'rooms': rooms,
    }
    return render(request, 'projectdetails.html', data)


@login_required
def movetorooms_view(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        rooms = Room.objects.filter(project=project)

        data = {
            'range': range(project.numroom),
            'project': project,
            'rooms': rooms,
        }
        return render(request, 'mainpage3.html', data)


@login_required
def editrooms_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    rooms = Room.objects.filter(project=project)

    if request.method == 'POST':
        for i, room in enumerate(rooms, start=1):
            # Update room details
            room.name = request.POST.get(f'nameroom_{i}')
            room.desc = request.POST.get(f'description_{i}')
            room.app = request.POST.get(f'apps_{i}')
            room.length = request.POST.get(f'length_{i}')
            room.width = request.POST.get(f'width_{i}')
            room.height = request.POST.get(f'height_{i}')
            room.color = request.POST.get(f'color_{i}')
            room.occupants = request.POST.get(f'occupants_{i}')
            room.window_num = request.POST.get(f'window_num_{i}')
            room.window_size = request.POST.get(f'window_size_{i}')
            room.window_orientation = request.POST.get(f'window_orientation_{i}')
            room.lamp_specs = request.POST.get(f'lamp_specs_{i}')
            room.aircond_type = request.POST.get(f'aircond_type_{i}')

            room.save()

        return redirect('projectdetails', project_id=project_id)

    else:
        context = {
            'project': project,
            'rooms': rooms,
        }
        return render(request, 'mainpage3.html', context)


@login_required
def deleteproject_view(request, project_id):
    if request.method == 'POST':
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return redirect('project')


@login_required
def deleteroom_view(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    project_id = room.project.id
    room.delete()
    return redirect('projectdetails', project_id=project_id)
