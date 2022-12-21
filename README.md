# Water Prediction
Water prediction merupakan sebuah aplikasi berbasis website yang berfungsi untuk menentukan apakah suatu air yang ingin kita klasifikasikan merupakan air yang aman untuk dikonsumsi atau tidak berdasarkan indeks bakteri, uranium, virus, fluoride, dan aluminium.
# Data Cleaning
* Menghilangkan beberapa kolom yang tidak penting
* Melakukan konversi yang kolom yang ada unsur NULL ke 0
* Mengubah tipe data kolom dari object ke int
* Melakukan ekspor dataframe yang lama ke dataframe baru setelah menghapus beberapa kolom

# Split Data Into Training And Testing
```
x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.2, random_state=0)
```

# Decision Tree Classifier
Untuk melakukan klasifikasi, menggunakan metode Decision Tree
```
 isSafe = DecisionTreeClassifier(criterion="gini", max_depth=10)
 isSafe.fit(x_train, y_train)
 ```
 
 # Melakukan Prediksi
 ```
 x_new = np.array((aluminium, flouride, bacteria, viruses, uranium))
 x_new = np.reshape(x_new, (1, -1))
 predTree = isSafe.predict(x_new)
 output = predTree[0]
 ```
