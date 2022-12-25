from django.urls import path ,include
from . views import *



urlpatterns = [
        path('',dashboard, name='dashboard'),
        path('artikel/',artikel, name='tabel_artikel'),
        path('resep/',resep, name='tabel_resep'),
        path('tambah-artikel/',tambah_artikel, name='tambah_artikel'),
        path('artikel/lihat/<str:id>',lihat_artikel, name='lihat_artikel'),
        path('artikel/edit/<str:id>',edit_artikel, name='edit_artikel'),
        path('artikel/delete/<str:id>',delete_artikel, name='delete_artikel'),

        path('users/',users, name='tabel_users'),
        path('sinkron_resep',sinkron_resep, name='sinkron_resep'),
]
