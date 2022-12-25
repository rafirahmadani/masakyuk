from blog.models import Artikel
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog.models import Artikel, Kategori,Resep
import requests



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

def resep(request):
    template_name =  "back/tabel_resep.html"
   
    resep = Resep.objects.all()
    context = {
        'title' :  'tabel artikel',
        'resep' : resep,
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

def sinkron_resep(request):
        url = "https://www.themealdb.com/api/json/v1/1/search.php?s=Kumpir"
        data = requests.get(url).json()
        for d in data['meals']:
            cek_berita = Resep.objects.filter(idMeal=d['idMeal'])
            if cek_berita:
                print('data sudah ada')
                c = cek_berita.first()
                c.idMeal=d['idMeal']
                c.save()
            else: 
                #jika belum ada maka tulis baru kedatabase
                b = Resep.objects.create(
                    idMeal= d['idMeal'],
                    strMeal = d['strMeal'],
                    strDrinkAlternate = d['strDrinkAlternate'],
                    strCategory = d['strCategory'],
                    strArea = d['strArea'],
                    strInstructions = d['strInstructions'],
                    strTags= d['strTags'],
                    strYoutube = d['strYoutube'],
                    strMealThumb = d['strMealThumb'],
                    strIngredient1 = d['strIngredient1'],
                    strIngredient2= d['strIngredient2'],
                    strIngredient3 = d['strIngredient3'],
                    strIngredient4 = d['strIngredient4'],
                    strIngredient5 = d['strIngredient5'],
                    strIngredient6 = d['strIngredient6'],
                    strIngredient7 = d['strIngredient7'],
                    strIngredient8 = d['strIngredient8'],
                    strIngredient9 = d['strIngredient9'],
                    strIngredient10 = d['strIngredient10'],
                    strIngredient11 = d['strIngredient11'],
                    strIngredient12 = d['strIngredient12'],
                    strIngredient13 = d['strIngredient13'],
                    strIngredient14 = d['strIngredient14'],
                    strMeasure1 = d['strMeasure1'],
                    strMeasure2 = d['strMeasure2'],
                    strMeasure3 = d['strMeasure3'],
                    strMeasure4 = d['strMeasure4'],
                    strMeasure5 = d['strMeasure5'],
                    strMeasure6 = d['strMeasure6'],
                    strMeasure7 = d['strMeasure7'],
                    strMeasure8 = d['strMeasure8'],
                    strMeasure9 = d['strMeasure9'],
                    strMeasure10 = d['strMeasure10'],
                    strMeasure11 = d['strMeasure11'],
                    strMeasure12 = d['strMeasure12'],
                    strMeasure13 = d['strMeasure13'],
                    strMeasure14 = d['strMeasure14'],
                    )  
                return redirect(resep)
# Create your views here.
