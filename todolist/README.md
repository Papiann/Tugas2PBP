# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

#

### Deployment Heroku
[Link Heroku Tugas 4 PBP Rafi Rasendrya Favian](https://pbp-tugas2-papian.herokuapp.com/todolist/)

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
- Menjalankan program `python manage.py startapp todolist` pada direktori cmd.

✅ Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
- Menambahkan path todolist ke dalam urlpatterns yang di `urls.py` pada folder `project_django`.

    ```
    urlpatterns = [
        ...
        path('todolist/', include('todolist.urls')),
    ]
    ```

✅ Membuat sebuah model Task yang memiliki atribut user, date, title, description.
- Menambahkan sebuah model Task pada file models.py dengan fields sesuai dengan ketentuan pada soal.

    ```
    class Task(models.Model):
        user        = models.ForeignKey(User, on_delete=models.CASCADE)
        date        = models.DateField()
        title       = models.TextField()
        description = models.TextField()
    ```

✅ Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan to do list dengan baik.
- Membuat 2 template HTML bernama `login.html` dan `register.html` untuk tampilan user ketika login dan register akun. Selanjutnya, menambahkan 3 fungsi yaitu register, login_user, dan logout_user pada `views.py` untuk menghandle logic register, login, dan logout.

    ```
    def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        ...


    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            ...


    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('todolist:login'))
        ...
    ```

✅ Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
- Membuat sebuah template HTML bernama `todolist.html` untuk tampilan halaman utama. Selanjutnya, menambahkan fungsi show_todolist pada `views.py` untuk menghandle tampilan data user yang sesuai.

    ```
    def show_todolist(request):
        data_todolist = Task.objects.filter(user=request.user)
        context = {
        'list_todolist' : data_todolist,
        'username' :  request.user.username,
        'last_login': request.COOKIES['last_login'],
        }
        return render(request, "todolist.html", context)
    ```

✅ Membuat halaman form untuk pembuatan task.
- Membuat sebuah template HTML bernama `create.html` untuk ditampilkan ke user ketika akan membuat task baru. Selanjutnya, menambahkan sebuah fungsi create_task pada `views.py` untuk menghandle logic pembuatan model task yang baru.

    ```
    def create_task(request):
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            date = datetime.datetime.now()
            user = request.user
            is_finished = False
            Task.objects.create(title=title, description=description, date=date, user=user, is_finished=is_finished)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            return response

    return render(request, "create.html")
    ```

✅ Membuat routing sehingga beberapa fungsi dapat diakses.
- Menambahkan path url yang sesuai pada `urls.py` dan dihubungkan dengan fungsi yang bersangkutan pada `views.py`.

    ```
    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('create-task/', create_task, name='create_task'),
    ]
    ```

✅ Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Deployment ke Heroku sudah berjalan secara otomatis dengan melakukan git push ke repository GitHub.

✅ Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.

~ Akun Dummy Pertama ~
- Username: Rafi
- Password: Rasendrya

    ![Gambar]('../../Akun_Dummy_Pertama.jpg?raw=true')

~ Akun Dummy Kedua ~
- Username: Favian
- Password: Rasendrya

    ![Gambar]('../../Akun_Dummy_Kedua.jpg?raw=true')