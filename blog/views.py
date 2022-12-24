from blog.models import Artikel
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog.models import Artikel, Kategori



# Create your views here.
def dashboard(request):
    template_name =  "back/dashboard.html"
    context = {
        'title' : 'dashboard'
    }
    return render(request, template_name, context)

def artikel(request):
    template_name =  "back/tabel_artikel.html"
   
    artikel = Artikel.objects.all()
    context = {
        'title' :  'tabel artikel',
        'artikel' : artikel,
    }
    return render(request, template_name, context)

def tambah_artikel(request):
    template_name =  "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kategori = request.POST.get('kategory')
        kat = Kategori.objects.get(nama=kategori)

        Artikel.objects.create(
            nama =nama,
            judul =judul,
            body =body,
            kategory = kat,   
        )
        return redirect(artikel)
    context = {
        'title' : 'tambah artikel',
        'kategory' : kategori,
    }
    return render(request, template_name, context)

def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title':'lihat artikel',
        'artikel':artikel,
    }
    return render(request, template_name, context)

def edit_artikel(request, id):
    template_name = "back/edit_artikel.html" 
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        judul = request.POST.get("judul")
        body = request.POST.get("body")
        #simpan data
        a.judul = judul
        a.body = body
        a.save()
        return redirect(artikel)
    
    context = {
        'title':'edit artikel',
        'artikel':a,
    }
    return render(request, template_name, context)

def delete_artikel(request, id):
   Artikel.objects.get(id=id).delete()
   return redirect(artikel)

def users(request):
    template_name =  "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' :  'tabel artikel',
        'list_user' : list_user,
    }
    return render(request, template_name, context)
# Create your views here.
