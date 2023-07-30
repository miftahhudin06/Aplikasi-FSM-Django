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
    teknisi = Karyawan.objects.filter(is_teknisi=True).count()
    admin = Karyawan.objects.filter(is_admin=True).count()
    a = Jadwal.objects.all()
    konteks = {
        'a': a,
        'teknisi': teknisi,
        'admin': admin
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
            messages.success(request, "Karyawan berhasil ditambahkan")
            return redirect(to='karyawanadmin')
        else:
            messages.error(request, "Data tidak valid")
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
            messages.success(request, "Data Karyawan berhasil di edit")
            return redirect(to='karyawanadmin')
        else:
            messages.error(request, "Data tidak valid")
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
    messages.success(request, "Data Karyawan Berhasil dihapus")
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
            messages.success(request, "Data Tersimpan")
            return redirect(to='profiladmin')
        else:
            messages.error(request, "Data tidak valid")
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
            messages.success(request, "Jadwal berhasil ditambahkan")
            return redirect(to='homeadmin')
        else:
            messages.error(request, "Data tidak valid")
    else:
        form_update = JadwalForm()
    konteks = {
        'form_update': form_update,
    }
    return render(request, "admin/inputJadwal.html", konteks)


@login_required
@akses_admin()
def editPekerjaanAdmin(request, id):
    a = Jadwal.objects.get(id=id)
    if request.method == 'POST':
        form_update = JadwalForm(request.POST, instance=a)
        if form_update.is_valid():
            form_update.save()
            messages.success(request, "Data berhasil di edit")
            return redirect(to='homeadmin')
        else:
            messages.error(request, 'Data tidak valid')
    else:
        form_update = JadwalForm(instance=a)
    konteks = {
        'form_update': form_update,
    }
    return render(request, "admin/inputJadwal.html", konteks)


@login_required
@akses_admin()
def deletePekerjaanAdmin(request, id):
    d = Jadwal.objects.get(id=id)
    d.delete()
    messages.success(request, 'Data berhasil di hapus')
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
        a = Note.objects.filter(gedung=id)
    except Note.DoesNotExist:
        messages.info(request, "Data belum tersedia")
        a = None
    konteks = {
        'a': a,
    }
    return render(request, "admin/noteDetail.html", konteks)


@login_required
@akses_admin()
def inputNoteAdmin(request):
    if request.method == 'POST':
        form = InputNoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Catatan Pekerjaan berhasil ditambahkan")
            return redirect(to='noteadmin')
        else:
            messages.error(request, "Data tidak valid")
    else:
        form = InputNoteForm()
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputNote.html", konteks)


@login_required
@akses_admin()
def editNoteAdmin(request, id):
    a = Note.objects.get(id=id)
    if request.method == 'POST':
        form = InputNoteForm(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()
            messages.success(request, "Catatan Pekerjaan berhasil diedit")
            return redirect(to='noteadmin')
        else:
            messages.error(request, "Data tidak valid")
    else:
        form = InputNoteForm(instance=a)
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputNote.html", konteks)


@login_required
@akses_admin()
def deleteNoteAdmin(request, id):
    d = Note.objects.get(id=id)
    d.delete()
    messages.success(request, 'Data berhasil di hapus')
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
            messages.success(
                request, "Berita Acara Kerusakan berhasil di ajukan")
            return redirect(to='bakadmin')
        else:
            messages.error(request, "Data tidak valid")
    else:
        form = BakForm()
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputBak.html", konteks)


@login_required
@akses_admin()
def editBakAdmin(request, id):
    a = BAK.objects.get(id=id)
    if request.method == 'POST':
        form = BakForm(request.POST, request.FILES, instance=a)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Berita Acara Kerusakan berhasil di ubah")
            return redirect(to='bakadmin')
        else:
            messages.error(request, "Data tidak valid")
    else:
        form = BakForm(instance=a)
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputBak.html", konteks)


@login_required
@akses_admin()
def deleteBakAdmin(request, id):
    a = BAK.objects.get(id=id)
    a.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect(to='bakadmin')
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
            messages.success(request, "Data gondola berhasil ditambahkan")
            return redirect(to='daftargondolaadmin')
        else:
            messages.error(request, "Data tidak valid")
    else:
        form = GondolaForm()
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputGondola.html", konteks)


@login_required
@akses_admin()
def editGondolaAdmin(request, id):
    a = TipeGondola.objects.get(id=id)
    if request.method == 'POST':
        form = GondolaForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            messages.success(request, "Data gondola berhasil di edit")
            return redirect(to='daftargondolaadmin')
        else:
            messages.error(request, "Data tidak valid")
    else:
        form = GondolaForm(instance=a)
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputGondola.html", konteks)


@login_required
@akses_admin()
def deleteGondolaAdmin(request, id):
    a = TipeGondola.objects.get(id=id)
    a.delete()
    messages.success(request, "Data berhasil dihapus")
    return redirect(to='daftargondolaadmin')

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
            messages.success(request, "Data gedung berhasil ditambahkan")
            return redirect(to='daftargedungadmin')
        else:
            messages.error(request, "Data tidak valid")
    else:
        form = GedungForm()
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputGedung.html", konteks)


@login_required
@akses_admin()
def editGedungAdmin(request, id):
    a = Gedung.objects.get(id=id)
    if request.method == 'POST':
        form = GedungForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil di edit")
            return redirect(to='daftargedungadmin')
        else:
            messages.error(request, "Data tidak valid")
    else:
        form = GedungForm(instance=a)
    konteks = {
        'form': form,
    }
    return render(request, "admin/inputGedung.html", konteks)


@login_required
@akses_admin()
def deleteGedungAdmin(request, id):
    a = Gedung.objects.get(id=id)
    a.delete()
    messages.success(request, "Data berhasil di hapus")
    return redirect(to='daftargedungadmin')

# ----------------------TEKNISI-------------------------------


@login_required
def home(request):
    teknisi = Karyawan.objects.filter(is_teknisi=True).count()
    admin = Karyawan.objects.filter(is_admin=True).count()
    a = Jadwal.objects.all()
    konteks = {
        'teknisi': teknisi,
        'admin': admin,
        'a': a
    }
    return render(request, "teknisi/dashboard.html", konteks)


@login_required
def updatePekerjaan(request):
    try:
        kSatu = Jadwal.objects.get(teknisiSatu=request.user)
        form_update = UpdateForm(instance=kSatu)
        if request.method == "POST":
            form_update = UpdateForm(request.POST, instance=kSatu)
            if form_update.is_valid():
                form_update.save()
                messages.success(request, "Update Jadwal Berhasil")
                return redirect(to='home')
            else:
                messages.error(request, "Data tidak valid")
    except Jadwal.DoesNotExist:
        kSatu = None
        form_update = UpdateForm()

    try:
        kDua = Jadwal.objects.get(teknisiDua=request.user)
        form_update = UpdateForm(instance=kDua)
        if request.method == "POST":
            form_update = UpdateForm(request.POST, instance=kDua)
            if form_update.is_valid():
                form_update.save()
                messages.success(request, "Update Jadwal Berhasil")
                return redirect(to='home')
            else:
                messages.error(request, "Data tidak valid")
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
    if request.method == 'POST':
        form = BakForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Berita Acara Kerusakan berhasil di ajukan")
            return redirect(to='bak')
        else:
            messages.error(request, "Data tidak valid")
    else:
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
