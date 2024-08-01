from django.shortcuts import render

# Create your views here.
def slayt(request):
    slaytdata = slayt.objects.all()
    context = {
        'slayt' : slaytdata
    }
    return render (request, 'slayt.html', context)
    
def index(request):
    return render(request, 'koliListeleme/list.html')

def detay(request, koliListeleme_id):
    return render(request, 'koliListeleme/detay.html')