from django.shortcuts import render

# Create your views here.
def CreateRoom(request):
    return render(request,'index.html')

def MessageView(request,room_name,username):
    return render(request,'message.html')