# Tugas 6: Javascript dan AJAX

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023 

#

### Deployment Heroku
[Link Heroku Tugas 6 PBP Rafi Rasendrya Favian](https://pbp-tugas2-papian.herokuapp.com/todolist/json)

#

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Jawab:

Perbedaan utama antara asyncrhonus programming dengan synchronus programming terletak pada metodenya.
- Asychronus programming berarti program dapat menjalankan beberapa task / tugas secara bersamaan. Ketika sebuah function asyncrhonus dipanggil, baris code selanjutnya tetap dapat dijalankan tanpa perlu menunggu function tersebut selesai dijalankan (concurrent).
- Synchronus programming berarti program menjalankan tugas / task secara berurutan. Ketika sebuah task/function dijalankan, instruksi untuk menjalankan task lainnya diblokir. Sedemikian sehingga harus menunggu task/function tersebut selesai terlebih dahulu baru bisa menjalankan task/function berikutnya (sequential).

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini
Jawab:

Paradigma Event-Driven Programming merupakan suatu momen dimana program dieksekusi berdasarkan event yang terjadi. Paradigma ini sangat bergantung pada event, sehingga flow dari program dapat dijalankan seperti konsep asynchronus programming yang tidak sequential. Salah satu contoh penerapannya pada tugas kali ini adalah ketika button `add` pada `add task` diklik, program akan selalu menjalankan suatu fungsi untuk membuat task baru ketika terdapat event yaitu click `document.getElementById("addtaskbutton").onclick = addTodolistModal`

### Jelaskan penerapan asynchronous programming pada AJAX
Jawab:

Penerapan asynchronus programming pada AJAX contohnya ketika sebuah event terjadi maka event tersebut akan menjalankan suatu fungsionalitas AJAX. Pada tugas 6 ini, penerapannya terjadi ketika user melakukan klik button add pada form untuk membuat task baru, makan AJAX POST akan dilakukan dan mengirim data ke server. Kemudian, setelah server berhasil mengolah data tersebut, callback function akan dijalankan sehingga dapat menangkap data dan mengirimkannya ke server tanpa harus melakukan reload pada website. Hal tersebut tentu akan membuat user experience dari website jauh lebih baik.

    ```
    <script>
    async function refreshTodolist() {
        document.getElementById("idRow").innerHTML = ""
        const todolist = await getTodolist()
        let cardAjax = ``
        ...

    }

    refreshTodolist()  
    </script>
    ```

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
Jawab:

AJAX GET
- Menambahkan 2 function yaitu `todolist_ajax` dan `get_todolist_json` pada `views.py` yang berfungsi untuk mengambil data task dalam bentuk JSON yang sesuai dengan user yang login saat itu. Function tersebut akan merev Selanjutnya menambahkan routing path pada `urls.py` agar views dapat terhubung. Ketika website berhasil di load, AJAX GET akan otomatis terpanggil dan mendapatkan task dalma bentuk JSON kemudian memasukkannya ke dalam masing-masing cards.

```
# TODOLIST AJAX
@login_required(login_url='/todolist/login/')
def todolist_ajax(request):
    ajax_todolist = Task.objects.filter(user=request.user)
    context = {
    'ajax_todolist' : ajax_todolist,
    'username' :  request.user.username,
    'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist_ajax.html", context)

# AJAX GET
def get_todolist_json(request):
    data_ajax = Task.objects.filter(user=request.user)

    return HttpResponse(serializers.serialize("json", data_ajax), content_type="application/json")

```
    path('json/', todolist_ajax, name='show_json'),
    path('get_todolist_json/', get_todolist_json, name='get_todolist_json'),
   
#

AJAX POST

- Membuat button add task yang sebelumnya redirect ke todolist/create_task, berubah menjadi memunculkan modal. Dalam implementasinya, menambahkan function `add` pada `views.py` dan routing pada urls.py agar dapat terhubung. Pada function ini diterapkan pula asynchronus programming sedemikian sehingga task yang ditambahkan akan otomatis terupdate tanpa perlu melakukan relaod pada website.

```
# ADD TASK MODAL
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        Task.objects.create(title=title, description=description, date=date, user=user)
         
        return HttpResponse(b"CREATED", status=201)

```

#

Oiyaa, tidak lupa untuk membuat `todolist_ajax_html` dan didalamnya mengimport Jquery Ajax dengan `    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>`. Kemudian menambahkan modal dan script yang berisi asynchronus function pada bagian body html untuk mengimplementasikan logic asynchronus programming pada views.py.