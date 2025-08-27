# Catatan Belajar Numpy
Numpy memungkinkan pengembang untuk mengalokasikan memori lebih optimal dengan membuat tipe sebuah data lebih spesifik penggunaan ukuran memorinya, int8, int16, float32, dll.
default size dai numerical memory allocation tergantung dari arsitektur sistem (32bit / 64bit)

Slicing np.array sama aturannya dengan python list
Multi indexing : alih alih melakukan slicing terhadap setiap index, numpy array memungkinkan untuk multi indexing dengan menggunakan slicing memakai list of indices arr[[0, 1, -1]] yang juga menghasilkan np.array
Ketika membuat multidimensional array, apabila terdapat 1 dimensi yang mismatch, maka akan disimpan sebagai tipe data ```object (dtype.('O'))```, untuk dimensi yang bermaslah sampai ke turunannya. Misalkan pada array 3 dimensi yang harusnya berukuran (2, 2, 3), apabila salah satu data hanya memiliki 1 rows, maka shape array akan menjadi (2,) <- deprecated, soalnya kalo dilakuin sekarang bakal error
Multidimensional slicing -> ```arr[d1, d2, d3, ..., dn]```
assigning value pada np.array dengan slicing akan merubah semua elemen turunannya jika dilakukan pada dimensi yang lebih tinggi -> untuk A1 yang 2-d, jika A[0] akan merubah isi A[0, 0-n]
```axis=0``` orientasinya vertikal (top bottom), ```axis=1``` orientasinya horizontal (left right)
penggunaan parameter ```size=``` akan menghasilkan nilai dalam bentuk array
penggunaan memory sebuah array NumPy dapat dihitung menggunakan ```arr.size * array.itemsize``` (byte)
[::n] n-step indexing, mulai dari 0 kalau tidak ada angka sebelum colon pertama
default: `.any()` -> True jika ada yang falsy, `.all()` -> False jika ada yang falsy

### Apa sih broadcasting dan vecorized operation? Vektor ya?
Sangat tekait dengan boolean operation, vectorized operation adalah operasi yang diterapkan pada setiap elemen array
Sedangkan broadcasting adalah kemampuan numpy adalam melakukan vectorized operation pada array yang memiliki dimensi yang berbeda 
Comparison operator akan menghasilkan boolean array (masks) sehingga dapat digunakan untuk multiindexing -> arr[arr >= 2]
operator yang mendukung multiindexing di numpy yaitu tilde ```~``` (not), bar or (`|`), ampersand and (`&`) -> `arr[(a >= 2) & (a % 2 == 0) | (a < 10) & (a > 3)]`
```sys.gesizeof(x)``` -> mengembalikan jumlah byte yang dibutuhkan sebuah variabel
```np.dtype(type).itemsize``` -> sama, tapi dengan numpy


# Catatan Belajar Pandas
### Apasih Pandas? Apa juga sih Series?
Tipe data pandas terdiri dari Series dan DataFrame
Series adalah serangkaian data terindeks yang disimpan dengan tipe data tertentu
Index dari series dapat diganti menjadi value lain / label, ["label"], kalau teteap indexing menggunakan angka dapat menggunakan .iloc
Range indexing pada pandas tetap memasukkan upper limit -> [1:3] = 1, 2, 3
Boolean operator disini akan menghasilkan boolean series

konversi tipe data pada series dapat dilakukan dengan membuat ulang series baru dengan tipe data yang berbeda.
sorting -> `series.sort_values()`

DataFrame merupakan kumpulan data / Series dalam format tabel
Dalam membuat dataframe ada 3 komponen esensial, data, index, dan columns
`.info()` -> stuktur dataframe
`.describe()` -> statistik summary dari dataframe

`.loc` indexing menggunakan labeled index, sedangkan `.iloc` indexing dengan posisi
hasil dari pengindeksan dataframe adalah series
dataframe juga support multiindexing `df[['idx1', 'idx2'], ['col1', 'col2']]`
drop row dari dataframe `.drop(['index'])`
drop column dataframe `.drop(columns=['col1'])` atau `.drop(['colName'], axis=1)`
kolom baru `pd.Series([], index=['target'], name='colBaru')`
ganti nilai kolom dapat menggunakan =
kolom baru dari hasil operasi kolom lain dapat menggunakan `df['newCol'] = df['oldCol1'] / df['oldCol2']`
secara default baris pertama csv dianggap sebagai header, sehingga untuk menghilangkanya dapat menggunakan parameter header=None
list kolom dari df dapat dilihat dengan .columns
konversi string ke tanggal dengan pandas -> `pd.to_datetime()`
preview data make `.head()` -> teratas, `.tail()` -> terbawah, default 5 data
`.to_frame()` -> menjadikan output series jadi format yang lebih bagus secara visual

`.set_index()` dapat digunakan untuk mengganti index dari dataframe ke salah satu kolom
header, names, index_col, parse_dates -> merupakan parameter yang dapat diteruskan ke fungsi `.read_csv()`
    `header=None` : jangan treat baris 1 sebagai header
    `names=[""]` : nama kolom
    `index_col` : kolom ke-n yang akan dijadikan sebagai index
    `parse_dates`(bool) : merubah format tanggal bertipe string ke tipe data tanggal

`.plot()` merupakan fungsi yang digunakan untuk menampilkan visualisasi data dari dataframe, yang dibangun diatas library matplotlib.pyplot
Dataframe pandas juga dapat melakukan date indexing -> `'2020-05-14':'2020-05-17'`

# Data Cleaning
Tahapan penting dalam proses data cleaning yaitu:
1. Mengatasi missing data, mengatasi data yang hilang dapat dilakukan dengan cara menghubungi pihak yang terlibat
misalkan pada pihak tempat data kita berasal.
2. Mengatasi invalid values, invalid values dapat dikategorikan menjadi data yang memiliki tipe yang salah, ataupun data yang nilainya tidak masuk akal.
contohnya seperti umur pelanggan yang bernilai lebih dari 150 atau sesuatu yang seupa, tergantung dengan data apa yang kita olah.
3. Memperbaiki data
    `.isnull()` dan `.isna()` mengecek apakah sebuah data, series, atau dataframe memiliki null value
    `.dropna()` menghapus series yang memiliki nilai null, parameter axis menentukan apa yang dihapus apakah kolom atau baris
        parameter `how="all|any"` menentukan bagaimana rule na diaplikasikan, apakah sebuah series atau harus berisi null semua atau hanya beberapa
        `thresh` merupakan parameter yang menentukan berapa nilai yang harus ada dalam suatu series yang memiliki nilai null
    `.fillna()` mengganti nilai null menjadi sebuah nilai tertentu
        parameter `method=ffill|bfill` forward-fill dan backward-fill, mengisi nilai dari nilai sebelumnya kalau forward fill, sebaliknya kalau bfill.
            ffill akan meninggalkan na jika item pertama bernilai null, sedangkan bfill meninggalkan item terakhir na jika bernilai null

