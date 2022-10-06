# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

#

### Deployment Heroku
[Link Heroku Tugas 5 PBP Rafi Rasendrya Favian](https://pbp-tugas2-papian.herokuapp.com/todolist/)

#

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Jawab :
- Inline CSS
- Merupakan penulisan kode CSS langsung pada atribut elemen HTML. Kelebihan dari inline CSS adalah proses request HTTP lebih singkat sehingga proses load website akan lebih cepat, dapat memperbaiki kode dengan cepat, dan membantu ketika developer ingin menguji perubahan pada satu elemen. Namun kekurangan inline CSS adalah kurang efisien dikarenakan inline CSS hanya dapat diterapkan pada satu elemen HTML.
- Internal CSS
- Merupakan penulisan kode CSS dalam tag style dan penulisan kode HTML di header file HTML. Untuk membuat memiliki tampilan yang berbeda-beda sangat cocok menggunakan Internal CSS dikarenakan Internal CSS dapat membuat tampilan unik pada setiap page (halaman) website. Kelebihan dari Internal CSS adalah HTML dan CSS berada di dalam satu file sehingga tidak memerlukan untuk upload beberapa file. Selain itu, perubahan pada Internal CSS berlaku pada satu halaman saja. Namun, kekurangan dari Internal CSS adalah membuat performa website lebih lambat karena terdapat file CSS yang berbeda-beda pada setiap halaman akan membuat loading ulang setiap user mengganti halaman website.
- External CSS
- Merupakan penulisan kode CSS yang terpisah dengan kode HTML. External CSS ditulis pada file khusus `(.css)` dan diletakkan setelah bagian head halaman. Kelebihan dari External CSS adalah membuat ukuran dan struktur kode file HTML menjadi lebih kecil dan rapih, loading website lebih cepat dan file CSS dapat digunakan di beberapa halaman sekaligus. Namun, kekurangan dari External CSS adalah gagalnya pemanggilan file CSS oleh file HTML yang menyebabkan halaman web bisa saja menjadi berantakan. Hal tersebut dapat terjadi apabila koneksi internet tidak stabil.

### Jelaskan tag HTML5 yang kamu ketahui!
Jawab :

- `<div>`  = Merepresentasikan container/section.
- `<head>` = Mendefinisikan head dari dokumen HTML, biasanya berisi title.
- `<body>` = Mendefinisikan body dari dokumen HTML.
- `<h1>` to `<h6>` = Mendefinisikan ukuran heading HTML.
- `<title>` = Mendefinsikan title dari dokumen HTML.
- `<link>` = Mendefinisikan hubungan antara dokumen HTML dengan dokumen external.
- `<meta>` = Menyediakan metadata terstruktur mengenai konten dokumen.
- `<a>` = Mendefinisikan hyperlink.

### Jelaskan tipe-tipe CSS selector yang kamu ketahui!
Jawab :

- ID Selector adalah tipe CSS selector yang berfungsi untuk menambahkan style dengan ID tertentu. Penggunaannya dengan menuliskan hashtag diikuti dengan nama ID. Contohnya `#idSatu {`.
- Class Selector adalah tipe CSS selector yang berfungsi untuk menambahkan style dengan class tertentu. Penggunannya dengan menuliskan titik diikuti dengan nama classnya. Contohnya `.classSatu {`.
- Tag Selector adalah tipe CSS selector yang berfungsi untuk menambahkan style pada sebuah tag. Penggunaannya dengan menuliskan tag yang ingin diberikan style, Contohnya `div {`.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Jawab :

 ✅ Melakukan import framework bootstrap pada setiap halaman html (`login.html`, `register.html`, `create.html`, `todolist.html`) yang ingin saya kustomisasi. Kode tersebut didapat dari https://getbootstrap.com/docs/5.2/getting-started/introduction/ .
 ```
    <!-- BOOTSTRAP -->
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
    </head>
```

 ✅ Selanjutnya, menkostumisasi halaman `login.html`, `register.html` dan `create.html` dengan mengubah warna background, padding, margin, font, text-allignment, serta menambahkan emoji agar lebih menarik. Selain itu, saya juga memanfaatkan cards dari bootstrap agar lebih tersusun rapih. Tak lupa juga menambahkan kode pada body html.
 ```
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
 ``` 
 Link cards bootstrap =  https://getbootstrap.com/docs/5.2/components/card/ .

 ✅ Lalu, kustomisasi halaman `todolist.html` dengan cara yang sama dengan `login.html`, `register.html`, `create.html` namun perbedaanya dalam pemanfaatan cards dari bootstrapnya. Pada `todolist.html` saya memasukkan setiap task yang dibuat menjadi satu cards dan membungkus cards cards tersebut dalam sebuah class yang mengatur baris dan kolom cards tersebut `<div class="row row-cols-md-3 mx-auto" style="width: 100%;">`. Oiyaa, saya juga menambahkan navbar dengan warna dark dan fixed top yang berarti tetap stay ada diatas ketika saya melakukan scroll kebawah pada halaman ini. Navbar tersebut saya memanfaatkan untuk menampilkan nama saya `a Todolist by Rafi Rasendrya Favian`.       

✅  Kemudian, saya melakukan pengecekan terhadap seluruh halamnan apakah sudah responsive atau belum dengan melakukan inspect pada website, mengubah ubah ukuran website, dan mencoba mengakses website dengan HP. 

✅ Terakhir, saya membuat folder `css` yang berisi file `style.css` pada folder `static`. Didalam file `style.css` saya tambahkan kode CSS :
```
.card:hover {
        transform: scale(1.015);
        box-shadow: 20px 20px 20px rgba(24, 73, 31, 0.12), rgba(24, 114, 66, 0.06);
}
```
Untuk membuat efek hover pada setiap card yang saya buat di file html termasuk halaman todolist.