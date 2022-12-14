# Water Prediction
Water prediction merupakan sebuah aplikasi berbasis website yang berfungsi untuk menentukan apakah suatu air yang ingin kita klasifikasikan merupakan air yang aman untuk dikonsumsi atau tidak berdasarkan indeks bakteri, uranium, virus, fluoride, dan aluminium. Adapun pembuatan aplikasi ini yaitu dengan menggunakan bahasa pemrograman Python,HTML,dan Jupyter Notebook.
# Data Cleaning
* Menghilangkan beberapa kolom yang tidak penting
* Melakukan konversi yang kolom yang ada unsur NULL ke 0
* Mengubah tipe data kolom dari object ke int
* Melakukan ekspor dataframe yang lama ke dataframe baru setelah menghapus beberapa kolom

Untuk membaca Data Frame
```
df = pd.read_csv('waterQuality1.csv')
df.head()
```
<br>
Melakukan penghapusan kolom 

```
df = df.drop(['ammonia', 'arsenic', 'barium', 'cadmium', 'chloramine', 'chromium', 'copper', 'lead', 'nitrates', 'nitrites', 'mercury', 'perchlorate', 'radium', 'selenium', 'silver'], axis=1)
```
<br>
Membuat x dan y dimana x merupakan predictor dan y outcome

```
y = df['is_safe']
x = df[['aluminium', 'flouride', 'bacteria', 'viruses', 'uranium']]
```
Melakukan konversi nilai NULL ke 0 pada kolom outcome
```
df['is_safe']= pd.to_numeric(df['is_safe'], errors='coerce').fillna(0).astype(np.int64)
```

Melakukan ekspor dataframe baru 
```
df.to_csv('waterQuality2.csv', index=False)
```

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
 # Dibuat Oleh
 Agung Kartika Ardhiyanda
