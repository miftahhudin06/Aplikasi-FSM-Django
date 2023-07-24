
from django import forms
from django.contrib.auth.models import User
from work.models import BAK, Gedung, Jadwal, Karyawan, Note, TipeGondola
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import UpdateView


class loginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-sm', 'type': 'email', 'placeholder': 'Masukan email'}))
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm', 'type':'password'}))


class KaryawanCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-sm'}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    first_name = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    last_name = forms.CharField(max_length=1000, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'required': 'false'}))
    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm'}))
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-sm'}))
    foto = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control', 'required': 'false'}))

    class Meta:
        model = Karyawan
        fields = ["email", "username", "first_name", "last_name",
                  "password1", "password2", "is_teknisi", "is_admin", "foto"]


class KaryawanChangeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    last_name = forms.CharField(max_length=1000, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm', 'required': 'false'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-sm'}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Karyawan
        fields = ["first_name", "last_name", "email",
                  "username", "foto", "is_admin", "is_teknisi"]


class GedungForm(forms.ModelForm):
    namaGedung = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    pengelola = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Gedung
        fields = '__all__'


class GondolaForm(forms.ModelForm):
    gedung = forms.ModelChoiceField(queryset=Gedung.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    tower = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    tipe = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = TipeGondola
        fields = '__all__'


class JadwalForm(forms.ModelForm):
    tgl = forms.DateField(required=True, widget=forms.DateInput(
        attrs={'class': 'form-control form-control-sm', 'type': 'date'}))
    gedung = forms.ModelChoiceField(queryset=Gedung.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    teknisiSatu = forms.ModelChoiceField(queryset=Karyawan.objects.filter(
        is_teknisi=True), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    teknisiDua = forms.ModelChoiceField(queryset=Karyawan.objects.filter(
        is_teknisi=True), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    pekerjaan = forms.CharField(max_length=1000, required=True, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-sm'}))
    hasilPekerjaan = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-sm'}))
    catatanKhusus = forms.CharField(max_length=1000, required=False, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-sm'}))

    def __init__(self, *args, **kwargs):
        super(JadwalForm, self).__init__(*args, **kwargs)
        self.fields['hasilPekerjaan'].required = False

    class Meta:
        model = Jadwal
        fields = '__all__'


class UpdateForm(forms.ModelForm):
    tgl = forms.DateField(disabled=True, widget=forms.DateInput(
        attrs={'class': 'form-control form-control-sm', 'type': 'date'}))
    gedung = forms.ModelChoiceField(disabled=True, queryset=Gedung.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    teknisiSatu = forms.ModelChoiceField(disabled=True, queryset=Karyawan.objects.filter(
        is_teknisi=True), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    teknisiDua = forms.ModelChoiceField(disabled=True, queryset=Karyawan.objects.filter(
        is_teknisi=True), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    pekerjaan = forms.CharField(disabled=True, max_length=1000, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    hasilPekerjaan = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-sm'}))
    catatanKhusus = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Jadwal
        fields = '__all__'


class InputNoteForm(forms.ModelForm):
    gedung = forms.ModelChoiceField(queryset=Gedung.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    picSatu = forms.ModelChoiceField(queryset=Karyawan.objects.filter(
        is_teknisi=True), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    picDua = forms.ModelChoiceField(queryset=Karyawan.objects.filter(
        is_teknisi=True), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    bulan = forms.CharField(required=False, widget=forms.DateInput(
        attrs={'class': 'form-control form-control-sm', 'type': 'month'}))
    tgl = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control form-control-sm', 'type': 'date'}))
    tipeGondola = forms.ModelChoiceField(queryset=TipeGondola.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    service = forms.CharField(max_length=1000, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    catatan = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={'class': 'form-control form-control-sm'}))
    fotoKerusakan = forms.CharField(required=False, widget=forms.FileInput(
        attrs={'type': 'file', 'class': 'form-control', 'id': 'customFile'}))
    status = forms.CharField(max_length=1000, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Note
        fields = '__all__'


class BakForm(forms.ModelForm):
    gondola = forms.ModelChoiceField(queryset=TipeGondola.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    tgl = forms.CharField(widget=forms.DateInput(
        attrs={'class': 'form-control form-control-sm', 'type': 'date'}))
    sparepart = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    spesifikasi = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    teknisiSatu = forms.ModelChoiceField(queryset=Karyawan.objects.filter(
        is_teknisi=True), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    teknisiDua = forms.ModelChoiceField(queryset=Karyawan.objects.filter(
        is_teknisi=True), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    qty = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    analisa = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    solusi = forms.CharField(max_length=1000, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control form-control-sm'}))
    fotoKerusakan = forms.CharField(max_length=1000, required=False, widget=forms.FileInput(
        attrs={'type': 'file', 'class': 'form-control', 'id': 'customFile'}))

    class Meta:
        model = BAK
        fields = '__all__'
