from Skripsi import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.signin, name="signin"),
    # admin
    path('homeadmin', views.homeAdmin, name="homeadmin"),
    path('karyawanadmin', views.karyawanAdmin, name="karyawanadmin"),
    path('inputkaryawanadmin', views.inputKaryawanAdmin, name="inputkaryawanadmin"),
    path('editkaryawanadmin/<int:id>',
         views.editKaryawanAdmin, name="editkaryawanadmin"),
    path('deletekaryawanadmin/<int:id>',
         views.deleteKaryawanAdmin, name="deletekaryawanadmin"),
    path('profiladmin', views.profilAdmin, name="profiladmin"),
    path('noteadmin/', views.noteAdmin, name="noteadmin"),
    path('notedetailadmin/<int:id>',
         views.noteDetailAdmin, name="notedetailadmin"),
    path('inputnoteadmin/', views.inputNoteAdmin, name="inputnoteadmin"),
    path('deletenoteadmin/<int:id>', views.deleteNoteAdmin, name="deletenoteadmin"),
    path('bakadmin/', views.bakAdmin, name="bakadmin"),
    path('inputbakadmin/', views.inputBakAdmin, name="inputbakadmin"),
    path('inputpekerjaanadmin', views.inputPekerjaanAdmin,
         name="inputpekerjaanadmin"),
    path('deletepekerjaanadmin/<int:id>', views.deletePekerjaanAdmin,
         name="deletepekerjaanadmin"),
    path('daftargondolaadmin/', views.daftarGondolaAdmin,
         name="daftargondolaadmin"),
    path('inputgondolaadmin/', views.inputGondolaAdmin, name="inputgondolaadmin"),
    path('daftargedungadmin/', views.daftarGedungAdmin, name="daftargedungadmin"),
    path('inputgedungadmin/', views.inputGedungAdmin, name="inputgedungadmin"),
    # teknisi
    path('home', views.home, name="home"),
    path('profil', views.profil, name="profil"),
    path('note/', views.note, name="note"),
    path('notedetail/<int:id>', views.noteDetail, name="notedetail"),
    path('bak/', views.bak, name="bak"),
    path('inputbak/', views.inputbak, name="inputbak"),
    path('updatepekerjaan', views.updatePekerjaan, name="updatepekerjaan"),
    path('daftargondola/', views.daftarGondola, name="daftargondola"),
    path('daftargedung/', views.daftarGedung, name="daftargedung"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
