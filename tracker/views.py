from django.http import HttpResponse
from django.conf import settings
from .models import TrackRecord
from django.db.models import F
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from .decode_and_encoder import decode_data,encode_data
import os

@login_required
def index(request):
    if request.method == 'GET':
        context = {
            'data': TrackRecord.objects.filter(user=request.user)
        }
        return render(request,'index.html',context)
    elif request.method == 'POST':
        recipient = request.POST.get('recipient').strip()

        if recipient !='':
            new_record = TrackRecord.objects.create(user=request.user,email_recipient=recipient)
            data = {
                'tracker_id':str(new_record.pk),
                'user':new_record.user.username,
            }

            image_url = f"{settings.DOMAIN_NAME}/image/?params={encode_data(data)}"
            context = {
                'data': TrackRecord.objects.filter(user=request.user),
                'image_url':image_url
            }
            return render(request,'index.html',context)
        else:
            return redirect(index)
    else:
        return HttpResponse('Not allowed',status=405)

def login(request):
    if request.user.is_authenticated:
        return redirect(index)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth_login(request,user)
            return redirect(index)
        else:
            return render(request,'login.html',{
                'username':username, 
                'error': 'Invalid username or password.'
                })
    return render(request,'login.html')

def logout(request):
    auth_logout(request)
    return redirect(login)

def serve_image(req):
    if req.method == 'GET':

        encoded = req.GET.get('params')

        if encoded:

            try:
                data = decode_data(encoded)
                is_exist_data = TrackRecord.objects.filter(pk=data.get('tracker_id'))
            except:
                return HttpResponse('Error: Enter valid URL',status=403)
            
            if is_exist_data:
                try:
                    absolute_url = os.path.join(settings.BASE_DIR,'static','image.png')
                    image = open(absolute_url,'rb').read()
                    response = HttpResponse(image,content_type='image/png')
                    response['Content-Disposition'] = 'attachment; filename="img.jpg"'
                    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
                    response['Pragma'] = 'no-cache'
                    response['Expires'] = '0'
                    TrackRecord.objects.filter(pk=data.get('tracker_id')).update(visit_count=F('visit_count')+1)
                except:
                    return HttpResponse('Something went wrong',500)

                return response
            
            else:
                return HttpResponse("Track history don't exist",404)
        else:
            return HttpResponse('Bad Request',status=403)
    else:
        return HttpResponse(f"Method `{req.method}` is not allowed",status=405)
    