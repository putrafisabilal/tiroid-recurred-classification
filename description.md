# Judul Project

## Repository Outline

Contoh:
```
1. README.md - Penjelasan gambaran umum project
2. P1M2_Putra_Fisabil_Muhammad.ipynb - Notebook yang berisi pengolahan data dengan python
3. P1M2_Inference_Putra_Fisabil_Muhammad.ipynb - Notebook yang berisi uji coba model terbaik yang sudah dibuat
4. function.py - Berisi fungsi fungsi yang digunakan dalam notebook
5. Thyroid_Diff.csv - Dataset penyakit tiroid untuk modelling
6. app.py - aplikasi main untuk menjalankan deployment
7. eda.py - visualisasi EDA untuk deployment
8. home.py - penjelasan penelitian untuk deployment
9. prediction.py - inference untuk deployment
10. plot.py - berisikan fungsi pembuatan plot
11. requirements.txt - libraries untuk deployment
12. model.SVM.pkl - model yang digunakan untuk prediksi
13. P1M2_Putra_Fisabil_Muhammad_conceptual.txt - berisikan jawaban konseptual dari readme.md
14. url.txt - berisikan link dataset dan link deployment
```

## Problem Background
(Differentiated Thyroid Cancer/DTC) merupakan jenis kanker yang umumnya memiliki prognosis baik atau tidak terlalu ganas, tetapi tetap berisiko kambuh kembali (recurrence). Mendekteksi lebih awal terhadap potensi kambuh ini sangat penting agar dokter dapat melakukan pemantauan lebih intensif dan perencanaan terapi yang tepat pasca operasi. sebagai data science saya akan membuat model machine learning untuk memudahkan dokter mengontrol pasien mereka pasca 

## Project Output
project ini menghasilkan model machine learning untuk memprediksi kambuh dari pasien dengan riwayat tiroid, yang kemudian akan di deploy menjadi webapps sehingga model ini dapat digunakan secara online oleh dokter maupun pasien

## Data
RangeIndex: 383 entries, 0 to 382
Data columns (total 17 columns):
 #   Column                Non-Null Count  Dtype   Jenis
---  ------                --------------  -----   -----
 0   Age                   383 non-null    int64    Fitur
 1   Gender                383 non-null    object   Fitur
 2   Smoking               383 non-null    object   Fitur
 3   Hx Smoking            383 non-null    object   Fitur
 4   Hx Radiothreapy       383 non-null    object   Fitur
 5   Thyroid Function      383 non-null    object   Fitur
 6   Physical Examination  383 non-null    object   Fitur
 7   Adenopathy            383 non-null    object   Fitur
 8   Pathology             383 non-null    object   Fitur
 9   Focality              383 non-null    object   Fitur
 10  Risk                  383 non-null    object   Fitur
 11  T                     383 non-null    object   Fitur
 12  N                     383 non-null    object   Fitur
 13  M                     383 non-null    object   Fitur
 14  Stage                 383 non-null    object   Fitur
 15  Response              383 non-null    object   Fitur
 16  Recurred              383 non-null    object   Target
dtypes: int64(1), object(16)

## Method
Setelah membandingkan 5 model mulai dari KNN, SVC, Decision Tree, Random Forest Classifier, Xgboost hasil yang paling baik untuk modelling adalah SVC sehingga kita akan menggunakan SVC algoritma utama untuk modelling pada project ini.

## Stacks
- pandas – Digunakan untuk manipulasi dan analisis data. Ini memungkinkan pemuatan dataset, pembersihan data, dan melakukan operasi seperti pengelompokan, penyaringan, dan agregasi.

- numpy – Digunakan untuk fungsi matematika yang mendukung perhitungan numerik secara efisien.

- scipy – Digunakan untuk analisis ilmiah dan statistik, dalam proyek ini digunakan untuk melihat korelasi antara tingkat bunuh diri dan PDB.

- matplotlib – Merupakan dasar dari pustaka visualisasi untuk seaborn.

- seaborn – Dibangun di atas matplotlib, digunakan untuk membuat plot dan grafik statis seperti grafik garis, diagram batang, dan histogram untuk memvisualisasikan tren dan perbandingan.

- sklearn – Merupakan pustaka utama untuk membangun dan mengevaluasi model machine learning. Digunakan untuk klasifikasi, regresi, clustering, preprocessing data, validasi model, serta pemilihan fitur. Dalam proyek ini, sklearn digunakan untuk membuat pipeline model, tuning hyperparameter, dan evaluasi performa model.

- scipy – Digunakan untuk fungsi-fungsi ilmiah dan statistik tingkat lanjut seperti uji chi-square, uji ANOVA, uji t-test, serta manipulasi matriks. Dalam proyek ini, scipy membantu dalam melakukan pengujian statistik terhadap hubungan antar variabel.

- statsmodels – Pustaka statistik untuk membuat model regresi dan analisis statistik lanjutan. Cocok untuk eksplorasi data yang butuh interpretasi matematis yang lebih mendalam, seperti model OLS (Ordinary Least Squares), uji normalitas, dan regresi logistik dengan laporan lengkap (summary). 

- pickle – Digunakan untuk menyimpan dan memuat model machine learning dalam bentuk file `.pkl`. Dengan `pickle`, model yang sudah dilatih bisa disimpan dan digunakan kembali tanpa perlu retraining ulang.


## Reference
Link Deployment Hugging Face [Link](https://huggingface.co/spaces/Putrafisabilal/P1M2_Deployment)
SVC [link](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
SVM [link](https://www.researchgate.net/publication/344458945_The_effect_of_gamma_value_on_support_vector_machine_performance_with_different_kernels)
SMOTE [link](https://biodatamining.biomedcentral.com/articles/10.1186/s13040-023-00330-4)
SHAP [link](https://www.sciencedirect.com/science/article/pii/S2213231724004488)
---

**Referensi tambahan:**
- Pandas [link](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- scikit-learn [link](https://scikit-learn.org/stable/user_guide.html)
- scipy [link](https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide)
- matplotlib [link](https://matplotlib.org/stable/users/index.html)
- numpy [link](https://numpy.org/devdocs/user/index.html#user)