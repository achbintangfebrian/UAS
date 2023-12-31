from django. http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title" : "Daftar buku",
        "all_tk" : [
            {
                
            }
        ]
    }
    return render(request,'index.html', context)