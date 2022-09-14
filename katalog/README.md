# Tugas 2 Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

## Nama : Rafi Rasendrya Favian
## NPM  : 2106751581

### Link Heroku
pbp-tugas2-papian.herokuapp.com/katalog

### Bagan request client ke web aplikasi berbasis Django
![Gambar]('../../PolaDjangoReqClient%20-%20RafiRasendryaFavian.png?raw=true')

Penjelasan :

Bagan / Pola request client ke web aplikasi berbasis Django berawal dari permintaan masuk (request) ke dalam server Django yang akan diproses melalui urls (urls.py) untuk diteruskan ke views (views.py) yang telah didefinisikan oleh pengembang untuk memproses permintaan tersebut. Jika terdapat proses data yang membutuhkan keterlibatan database, maka nantinya views akan memanggil respon data (query) ke models lalu database akan mengembalikan hasil dari query tersebut ke views. Setelah permintaan telah selesai diproses, Hasil proses tersebut akan ditampilkan ke dalam HTML yang sudah didefinisikan sebelum nanti HTML tersebut dikembalikan ke client sebagai respons.

### Kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Penjelasan :

Virtual environment atau biasa disebut venv merupakan environment manager dari python yang berfungsi untuk membuat sebuah scope virtual yang terisolasi. Ketika kita membuat project, env akan memastikan seluruh data yang ada di library project hanya berubah di virtual environtment env dan tidak akan berubah pada storage local kita. Intinya venv ini akan mengisolasi packages dan dependancies yang ada di project kita.

Jika kita membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, maka yang terjadi ketika kita run atau update program maka otomatis akan terjadi perubahan pada packages dan dependancies di local storage sedemikian sehingga berpotensi terjadi perbedaan versi dari data-data tersebut.

### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Penjelasan : 

Poin 1 --> views.py
Saya mengimplementasikan views.py dengan mengambil semua data yang ada di database dan menambahkan beberapa variabel penting seperti nama dan npm. Variabel tersebut disimpan dalam scope context yang selanjutnya dibawa ke dalma fungsi render sebagai paramater tambahan untuk nantinya digunakan di html.

Poin 2 --> urls.py
Saya mengimplementasikan urls.py dengan menambahkan path('katalog/', include('katalog.urls')) pada file urls yang berada di folder project_django. Hal tersebut berguna untuk melakukan route '/katalog' dengan katalog/urls.py agar menjalankan function show_katalog yang ada di katalog.views.py 

Poin 3 --> katalog.html
Ketika mengimplementasikan katalog, program akan melakukan render di katalog.html, dan saya menambahkan data tambahan berupa nama dan npm dengam mengimplementasikannya menggunakan variabel "{{nama}}" dan "{{npm}}". Saya juga memberikan tambahan style itu memberikan tampilan web yang cukup eye-catching. Selain itu, saya juga menggunakan for loop untuk mengambil data-data yang disimpan pada list_catalog di database.

Poin 4 --> deploy
Ketika mengimplementasikan deploy, saya menyambungkan (connect) antara repository github ini ke akun heroku dengan cara memasukkan variabel HEROKU_APP_NAME dan HEROKU_API_KEY di github secrets --> actions supaya dapat connect secara realtime ke heroku dan langsung aja di deploy melalui github.