from django.shortcuts import redirect, render
from work.forms import BakForm, GedungForm, GondolaForm, InputNoteForm, JadwalForm, KaryawanChangeForm, KaryawanCreateForm, UpdateForm, loginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from work.models import BAK, Gedung, Jadwal, Karyawan, Note, TipeGondola
from .decoratorakses import (akses_admin)

# Create your views here.


def signin(request):
    form = loginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.is_admin:
                    login(request, user)
                    messages.success(
                        request, "Login Admin Sukses ")
                    return redirect('homeadmin')
                if user.is_teknisi:
                    login(request, user)
                    messages.success(request, "Login Teknisi Sukses")
                    return redirect('home')
            else:
                messages.error(
                    request, "Akun tidak tersedia, Silakan masukan kembali")
        else:
            messages.error(request, "Tidak dikenal")
    return render(request, "login.html", {'form': form, })


@login_required
def signout(request):
    logout(request)
    messages.info(request, "Logout Berhasil")
    return redirect('signin')

# -------------------------ADMIN----------------------------------

# ======= Dashboard =====================================================================


@login_required
@akses_admin()
def homeAdmin(request):
    a = Jadwal.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "admin/dashboard.html", konteks)

# ======= Karyawan =======================================================================


@login_required
@akses_admin()
def karyawanAdmin(request):
    a = Karyawan.objects.all()
    konteks = {
        'page1': a
    }
    return render(request, "admin/karyawan.html", konteks)


@login_required
@akses_admin()
def inputKaryawanAdmin(request):
    if request.method == 'POST':
        form = KaryawanCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='karyawanadmin')
    else:
        form = KaryawanCreateForm()
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputKaryawan.html", konteks)


@login_required
@akses_admin()
def editKaryawanAdmin(request, id):
    a = Karyawan.objects.get(id=id)
    if request.method == 'POST':
        form = KaryawanChangeForm(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()
            return redirect(to='karyawanadmin')
    else:
        form = KaryawanChangeForm(instance=a)
    konteks = {
        'form': form,
        'a': a
    }
    return render(request, "admin/editKaryawan.html", konteks)


@login_required
@akses_admin()
def deleteKaryawanAdmin(request, id):
    d = Karyawan.objects.get(id=id)
    d.delete()
    return redirect(to='karyawanadmin')
# ======= Profil ==============================================================


@login_required
@akses_admin()
def profilAdmin(request):
    if request.method == 'POST':
        form = KaryawanChangeForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(to='profiladmin')
    else:
        form = KaryawanChangeForm(instance=request.user)
    konteks = {
        'form': form,
    }
    return render(request, "admin/profilAdmin.html", konteks)

# ======= Pekerjaan ===========================================================


@login_required
@akses_admin()
def inputPekerjaanAdmin(request):
    if request.method == 'POST':
        form_update = JadwalForm(request.POST)
        if form_update.is_valid():
            form_update.save()
            return redirect(to='homeadmin')
    else:
        form_update = JadwalForm()
    konteks = {
        'form_update': form_update,
    }
    return render(request, "admin/inputJadwal.html", konteks)


@login_required
@akses_admin()
def deletePekerjaanAdmin(request, id):
    d = Jadwal.objects.get(id=id)
    d.delete()
    return redirect(to='homeadmin')
# ======= Catatan ===============================================================


@login_required
@akses_admin()
def noteAdmin(request):
    a = Gedung.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "admin/note.html", konteks)


@login_required
@akses_admin()
def noteDetailAdmin(request, id):
    try:
        a = Note.objects.get(gedung=id)
    except Note.DoesNotExist:
        a = None
    konteks = {
        'a': a
    }
    return render(request, "admin/noteDetail.html", konteks)


@login_required
@akses_admin()
def inputNoteAdmin(request):
    if request.method == 'POST':
        form = InputNoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='noteadmin')
    else:
        form = InputNoteForm()
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputNote.html", konteks)


@login_required
@akses_admin()
def deleteNoteAdmin(request, id):
    d = Note.objects.get(id=id)
    d.delete()
    return redirect(to='noteadmin')

# ===== Berita Acara Kerusakan ================================================


@login_required
@akses_admin()
def bakAdmin(request):
    a = BAK.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "admin/bak.html", konteks)


@login_required
@akses_admin()
def inputBakAdmin(request):
    if request.method == 'POST':
        form = BakForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to='bakadmin')
    else:
        form = BakForm()
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputBak.html", konteks)

# ======= Gondola ==============================================================


@login_required
@akses_admin()
def daftarGondolaAdmin(request):
    a = TipeGondola.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "admin/daftarGondola.html", konteks)


@login_required
@akses_admin()
def inputGondolaAdmin(request):
    if request.method == 'POST':
        form = GondolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='daftargondolaadmin')
    else:
        form = GondolaForm()
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputGondola.html", konteks)

# ======= Gedung =================================================================


@login_required
@akses_admin()
def daftarGedungAdmin(request):
    a = Gedung.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "admin/daftarGedung.html", konteks)


@login_required
@akses_admin()
def inputGedungAdmin(request):
    if request.method == 'POST':
        form = GedungForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='daftargedungadmin')
    else:
        form = GedungForm()
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputGedung.html", konteks)


# ----------------------TEKNISI-------------------------------

@login_required
def home(request):
    a = Jadwal.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "teknisi/dashboard.html", konteks)


@login_required
def updatePekerjaan(request):
    try:
        kSatu = Jadwal.objects.get(teknisiSatu=request.user)
        form_update = UpdateForm(instance=kSatu)
    except Jadwal.DoesNotExist:
        kSatu = None
        form_update = UpdateForm()

    try:
        kDua = Jadwal.objects.get(teknisiDua=request.user)
        form_update = UpdateForm(instance=kDua)
    except Jadwal.DoesNotExist:
        kDua = None
        form_update = UpdateForm()
    konteks = {
        'form_update': form_update,
    }
    return render(request, "teknisi/update.html", konteks)


@login_required
def profil(request):
    return render(request, "teknisi/profil.html")


@login_required
def note(request):
    a = Gedung.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "teknisi/note.html", konteks)


@login_required
def noteDetail(request, id):
    try:
        a = Note.objects.get(gedung=id)
    except Note.DoesNotExist:
        a = None
    konteks = {
        'a': a
    }
    return render(request, "teknisi/noteDetail.html", konteks)


@login_required
def bak(request):
    a = BAK.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "teknisi/bak.html", konteks)


@login_required
def inputbak(request):
    form = BakForm()
    konteks = {
        'form': form,
    }
    return render(request, "teknisi/inputBak.html", konteks)


@login_required
def daftarGondola(request):
    a = TipeGondola.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "teknisi/daftarGondola.html", konteks)


@login_required
def daftarGedung(request):
    a = Gedung.objects.all()
    konteks = {
        'a': a
    }
    return render(request, "teknisi/daftarGedung.html", konteks)
