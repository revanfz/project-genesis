# Catatan Belajar Pandas
Numpy memungkinkan pengembang untuk mengalokasikan memori lebih optimal dengan membuat tipe sebuah data lebih spesifik penggunaan ukuran memorinya, int8, int16, float32, dll.
default size dai numerical memory allocation tergantung dari arsitektur sistem (32bit / 64bit)

Slicing np.array sama aturannya dengan python list
Multi indexing : alih alih melakukan slicing terhadap setiap index, numpy array memungkinkan untuk multi indexing dengan menggunakan slicing memakai list of indices arr[[0, 1, -1]] yang juga menghasilkan np.array
Ketika membuat multidimensional array, apabila terdapat 1 dimensi yang mismatch, maka akan disimpan sebagai tipe data object (dtype.('O')), untuk dimensi yang bermaslah sampai ke turunannya. Misalkan pada array 3 dimensi yang harusnya berukuran (2, 2, 3), apabila salah satu data hanya memiliki 1 rows, maka shape array akan menjadi (2,)
Multidimensional slicing -> arr[d1, d2, d3, ..., dn]
assigning value pada np.array dengan slicing akan merubah semua elemen turunannya jika dilakukan pada dimensi yang lebih tinggi -> untuk A1 yang 2-d, jika A[0] akan merubah isi A[0, 0-n]
axis=0 orientasinya row (left right), axis=1 orientasinya column (top down)

Apa sih broadcasting dan vecorized operation? Vektor ya?