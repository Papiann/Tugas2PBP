# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

#

### Deployment Heroku
[Link Heroku Tugas 4 PBP Rafi Rasendrya Favian](https://pbp-tugas2-papian.herokuapp.com/todolist/)

~ Akun Dummy Pertama ~
- Username: Rafi
- Password: Rasendrya

~ Akun Dummy Kedua ~
- Username: Favian
- Password: Rasendrya

#

### Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Jawab :

`{% csrf_token %}` pada elemen `<form>` memiliki kegunaan untuk mencegah serangan CSRF (Cross-Site Request Forgery) dengan cara membandingkan key csrf ketika user ingin melakukan method get / post. Selanjutnya, form tersebut akan memberikan respon OK jika key csrf yang dibandingkan sesuai.

Hal yang terjadi apabila tidak ada `{% csrf_token %}` pada elemen `<form>` adalah website kita tetap berjalan dengan normal namun memungkinkan ada beberapa route link sensitif yang dapat di akses oleh umum atau website lain dan melakukan perubahan tanpa kita sadari.


### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Jawab :

Kita tetap dapat membuat elemen `<form>` secara manual tanpa menggunakan generator. Gambaran umumnya adalah dengan cara menggunakan tag `<input>` seperti yang ada di login.html. 

```
<input type="text" name="username" placeholder="Username" class="form-control">
```

Selanjutnya, data tersebut akan diterima dan disimpan oleh form. Lalu, untuk mengaksesnya bisa menggunakan method `get()` dengan parameter nama tag yang diinput.

```
username = request.POST.get('username')
```

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Jawab :

- Pertama, setelah pengguna menekan tombol submit dan data telah disubmisi, data tersebut dibawa oleh request dan disimpan pada suatu variabel di dalam file `views.py`.

    ```
    form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
    ```

- Selanjutnya, kita menggunakan method `save()` untuk menyimpan data kita ke database.

    ```
    form.save()
    ```

- Terakhir, file `views.py` dapat mengambil data dari database `models.py` dan kemudian dikirimkan ke template HTML supaya dapat ditampilkan.

    ```
    from todolist.models import Task

    def show_todolist(request):
        data_todolist = Task.objects.filter(user=request.user)
        context = {
        'list_todolist' : data_todolist,
        'username' :  request.user.username,
        'last_login': request.COOKIES['last_login'],
        }
        return render(request, "todolist.html", context)
    ```


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Jawab :

✅ Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
- Menjalankan program `python manage.py startapp todolist` pada cmd.

✅ Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.

✅ Membuat sebuah model Task yang memiliki atribut user, date, title, description.

✅ Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan to do list dengan baik.

✅ Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.

✅ Membuat halaman form untuk pembuatan task.

✅ Membuat routing sehingga beberapa fungsi dapat diakses.

✅ Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

✅ Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.