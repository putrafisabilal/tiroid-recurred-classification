import streamlit as st
import plot as ep

def eda():
    # isi page
    # title
    st.title("Exploratory Data Analysis")
    eda = st.selectbox('Pilih EDA',['Distribusi Umur Pasien?','Apakah terdapat perbedaan proporsi kanker tiroid berdasarkan gender ? dan bagaimana potensi Reccured dari masing-masing gender?','Seberapa banyak pasien pada tiap kombinasi T, N, M yang mengalami Recurred?','Apakah respon hasil terapi dapat mempengaruhi reccured?','Apakah tingkat risiko (Risk: Low, Intermediate, High) berpengaruh secara signifikan terhadap stadium kanker (Stage)?','Apakah nilai rata-rata usia pasien berbeda secara signifikan antara kelompok yang reccured dan tidak reccured (Recurred)?','Apakah ada perbedaan usia yang signifikan antar kategori Stage?'])

    st.markdown("---")

    # EDA
    if eda == 'Distribusi Umur Pasien?':
        # EDA 1 
        st.markdown("## Distribusi Umur Pasien?")
        st.pyplot(ep.eda1())
        st.write("Berdasarkan histogram distribusi usia pasien kanker tiroid di atas, terlihat bahwa kelompok usia terbanyak berada pada rentang antara 25 hingga 45 tahun, dengan puncaknya sekitar 30 hingga 35 tahun, di mana jumlah pasien mencapai lebih dari 40 orang per interval. Distribusi ini menunjukkan pola yang condong ke kiri (right-skewed), artinya sebagian besar pasien berada pada usia muda hingga paruh baya, sementara jumlah pasien menurun secara bertahap seiring bertambahnya usia. Meskipun pasien usia lanjut (di atas 60 tahun) masih ditemukan, frekuensinya jauh lebih rendah dibandingkan dengan kelompok usia muda. Hal ini mengindikasikan bahwa kanker tiroid dalam data ini lebih sering ditemukan pada individu berusia produktif, yang memiliki implikasi penting terhadap aspek penanganan dan kualitas hidup karena mayoritas pasien mungkin masih aktif bekerja atau memiliki tanggung jawab keluarga.Kesimpulannya, visualisasi ini memperlihatkan bahwa pasien kanker tiroid dalam dataset ini didominasi oleh kelompok usia muda hingga dewasa awal, sehingga pendekatan klinis dan psikososial terhadap mereka perlu disesuaikan dengan karakteristik usia tersebut.")
        st.markdown("---")
    elif eda == 'Apakah terdapat perbedaan proporsi kanker tiroid berdasarkan gender ? dan bagaimana potensi Reccured dari masing-masing gender?':
        # EDA 2
        
        st.markdown("## Apakah terdapat perbedaan proporsi kanker tiroid berdasarkan gender ? dan bagaimana potensi Reccured dari masing-masing gender?")
        st.pyplot(ep.eda2())
        st.write("Berdasarkan grafik pertama, distribusi pasien kanker tiroid menurut jenis kelamin menunjukkan bahwa jumlah pasien perempuan (F) jauh lebih tinggi dibandingkan laki-laki (M). berati dalam data ini menyimpulkan bahwa kanker tiroid lebih sering terjadi pada perempuan. perempuan mencakup lebih dari tiga perempat total pasien, sedangkan laki-laki hanya sebagian kecil.Namun, ketika kita meninjau grafik kedua yang menunjukkan jumlah recurred berdasarkan gender, muncul pola yang menarik. Meskipun jumlah pasien perempuan lebih banyak, proporsi reccured pada laki-laki terlihat lebih tinggi. Terlihat bahwa jumlah laki-laki yang mengalami reccured bahkan lebih besar dibandingkan laki-laki yang tidak reccured. Sebaliknya, pada perempuan, mayoritas pasien tidak mengalami reccured.Hal ini menunjukkan bahwa walaupun kanker tiroid lebih umum terjadi pada perempuan, tingkat reccurednya cenderung lebih tinggi pada pasien laki-laki. Secara klinis, ini berarti bahwa laki-laki dengan kanker tiroid mungkin memerlukan pemantauan lebih ketat dan pendekatan terapi yang lebih agresif untuk mencegah reccured. Dengan demikian, gender tidak hanya mempengaruhi proporsi pasien yang terdiagnosis, tetapi juga dapat menjadi faktor risiko dalam prognosis penyakit, khususnya dalam hal reccured.")
        st.markdown("---")
    elif eda == 'Seberapa banyak pasien pada tiap kombinasi T, N, M yang mengalami Recurred?':
        # EDA 3
        st.markdown("## Seberapa banyak pasien pada tiap kombinasi T, N, M yang mengalami Recurred?")
        st.markdown('''
            Penjelasan Kombinasi TNM

            - `T1aN0M0` : Tumor kecil (≤1 cm), tidak menyebar ke kelenjar getah bening, tidak ada metastasis jauh → *Stadium awal, sangat ringan.*
            - `T1aN1bM0`: Tumor kecil (≤1 cm), tapi sudah menyebar ke kelenjar getah bening sisi leher → *Risiko menengah.*
            - `T1bN0M0` : Tumor kecil (>1–2 cm), belum menyebar → *Stadium awal.*
            - `T1bN1bM0`: Tumor kecil, tapi sudah menyebar ke kelenjar getah bening lateral → *Risiko menengah.*
            - `T2N0M0`  : Tumor 2–4 cm, tidak menyebar → *Masih tergolong awal.*
            - `T2N1bM0` : Tumor 2–4 cm, sudah menyebar ke leher lateral → *Risiko lebih tinggi.*
            - `T2N1aM0` : Tumor 2–4 cm, menyebar ke leher tengah → *Risiko sedang.*
            - `T2N0M1`  : Tumor 2–4 cm, tidak menyebar ke kelenjar tapi sudah metastasis jauh → *Serius.*
            - `T3aN0M0` : Tumor besar (>4 cm), tidak menyebar → *Risiko meningkat.*
            - `T3aN1bM0`: Tumor besar, menyebar ke kelenjar leher lateral → *Risiko tinggi.*
            - `T3aN1aM0`: Tumor besar, menyebar ke kelenjar leher tengah → *Risiko menengah–tinggi.*
            - `T3aN1bM1`: Tumor besar, menyebar ke kelenjar leher lateral dan metastasis jauh → *Sangat tinggi.*
            - `T3bN1aM0`: Tumor menyusup ke jaringan sekitar + sebaran ke leher tengah → *Agresif.*
            - `T3bN0M0` : Tumor menyusup lokal, belum menyebar → *Risiko sedang.*
            - `T3bN1bM0`: Tumor menyusup + menyebar ke leher lateral → *Agresif.*
            - `T3bN1aM1`: Tumor menyusup + sebaran ke leher tengah + metastasis → *Sangat serius.*
            - `T3bN1bM1`: Tumor menyusup + leher lateral + metastasis jauh → *Sangat tinggi.*
            - `T4aN0M0` : Tumor menyusup ke trakea/laring, belum menyebar → *Lokal lanjut.*
            - `T4aN1bM0`: Tumor menyusup + sebar ke leher lateral → *Agresif.*
            - `T4aN1bM1`: Tumor menyusup + leher lateral + metastasis → *Kritikal.*
            - `T4aN0M1` : Tumor menyusup ke struktur sekitar + metastasis jauh → *Sangat serius.*
            - `T4aN1aM1`: Tumor menyusup + leher tengah + metastasis → *Risiko tertinggi.*
            - `T4bN1bM0`: Tumor menyebar ke struktur vital + kelenjar leher lateral → *Sangat agresif.*
            - `T4bN1bM1`: Tumor menyebar ke struktur vital + leher lateral + metastasis → *Stadium paling berat.*
                    ''')
        st.pyplot(ep.eda3())
        st.markdown('''
                    Grafik di atas menunjukkan distribusi jumlah pasien kanker tiroid yang mengalami Recurred dan tidak Recurred berdasarkan kombinasi klasifikasi TNM (T = ukuran tumor, N = penyebaran ke kelenjar getah bening, M = metastasis). Terlihat bahwa kombinasi T2N0M0 dan T1bN1bM0 merupakan yang paling sering muncul pada pasien tanpa reccured, sedangkan reccured lebih sering terjadi pada kombinasi seperti T3aN0M0, T3aN1bM0, dan T4aN1bM0. Semakin kompleks dan lanjut kombinasi TNM-nya, terlihat cenderung memiliki proporsi reccured yang lebih tinggi.

                    Pola ini menunjukkan bahwa kombinasi TNM tertentu, terutama yang mencerminkan ukuran tumor besar, keterlibatan kelenjar getah bening tingkat lanjut (N1b), dan keterlibatan metastasis, cenderung berasosiasi dengan risiko reccured yang lebih besar. Ini mengindikasikan bahwa TNM dapat menjadi indikator penting dalam memprediksi reccured pasien, dan dapat digunakan sebagai salah satu dasar dalam penentuan strategi follow-up dan penanganan.
                    ''')
        st.markdown("---")

    elif eda == 'Apakah respon hasil terapi dapat mempengaruhi reccured?':
        # EDA 4
        st.markdown("## Apakah respon hasil terapi dapat mempengaruhi reccured?")
        st.markdown('''
                    Respons pasien terhadap terapi:
                    - `Excellent`: sembuh atau tanpa bukti sisa kanker
                    - `Indeterminate`: hasil tidak pasti
                    - `Structural Incomplete`: masih ada massa tumor
                    - `Biochemical Incomplete`: hormon tumor masih tinggi tapi tidak terlihat tumor
                    ''')
        st.pyplot(ep.eda4())
        st.markdown('''
                    Berdasarkan grafik di atas, terlihat bahwa respon hasil terapi memiliki hubungan yang kuat terhadap kemungkinan Recurred pada pasien kanker tiroid. Pasien dengan respon terapi “Excellent” hampir seluruhnya tidak mengalami reccured, yang mengindikasikan bahwa hasil terapi yang optimal secara signifikan menurunkan risiko reccured.

                    Sebaliknya, pada kelompok dengan respon “Structural Incomplete”, jumlah pasien yang mengalami reccured sangat dominan, menunjukkan bahwa hasil terapi yang tidak tuntas secara struktural sangat berkaitan dengan tingginya risiko reccured. Sementara itu, kategori “Indeterminate” dan “Biochemical Incomplete” menunjukkan distribusi yang lebih seimbang antara pasien yang kambuh dan tidak kambuh, meskipun tetap terdapat kecenderungan bahwa “Biochemical Incomplete” memiliki proporsi reccured yang relatif lebih tinggi dibanding “Indeterminate”.

                    Secara keseluruhan, grafik ini mengindikasikan bahwa semakin buruk respons terapi pasien, semakin tinggi kemungkinan terjadinya reccured. Dengan demikian, klasifikasi respons terapi dapat dijadikan indikator penting untuk mengevaluasi efektivitas pengobatan dan merancang strategi pemantauan lanjutan pada pasien kanker tiroid.
                    ''')
        st.markdown("---")
    elif eda == 'Apakah tingkat risiko (Risk: Low, Intermediate, High) berpengaruh secara signifikan terhadap stadium kanker (Stage)?':
        # EDA 5
        st.markdown("## Apakah tingkat risiko (Risk: Low, Intermediate, High) berpengaruh secara signifikan terhadap stadium kanker (Stage)?")
        st.pyplot(ep.eda5())
        st.markdown('''
                    === Hasil Uji Chi-Square ===

                    Chi-square statistic : 251.64

                    P-value               : 7.7305e-50

                    Cramér’s V            : 0.573"
                    ''')
        st.markdown('''
                    Berdasarkan hasil uji chi-square antara variabel Risk dan Stage, diperoleh nilai chi-square sebesar `251.64` dengan p-value sangat kecil `7.73 × 10⁻⁵⁰`, yang menunjukkan bahwa hubungan antara tingkat risiko dan stadium kanker sangat signifikan secara statistik. Selain itu, nilai Cramér’s V sebesar `0.573` mengindikasikan bahwa kekuatan hubungan tersebut berada dalam kategori kuat, sehingga kita dapat menyimpulkan bahwa tingkat risiko pasien secara nyata berkaitan dengan tingkat keparahan stadium kanker tiroid yang dialaminya.

                    Visualisasi heatmap mendukung kesimpulan ini. Terlihat bahwa pasien dengan risk rendah (Low) seluruhnya berada pada stadium I, sedangkan pada risk intermediate, sebagian besar berada pada stadium I dan II. Sementara itu, pasien dengan risk tinggi (High) memiliki distribusi stadium yang lebih merata, termasuk proporsi yang cukup besar pada stadium lanjut seperti IVB (34%) dan stadium II ke atas.

                    Kesimpulannya, semakin tinggi tingkat risiko pasien, semakin besar kemungkinan mereka berada pada stadium kanker yang lebih lanjut. Hal ini memperkuat pentingnya klasifikasi risiko dalam praktik klinis sebagai indikator awal untuk mendeteksi dan mengantisipasi tingkat keparahan kanker tiroid.
                    ''')
        st.markdown("---")

    elif eda == 'Apakah nilai rata-rata usia pasien berbeda secara signifikan antara kelompok yang reccured dan tidak reccured (Recurred)?':
        # EDA 6
        st.markdown("## Apakah nilai rata-rata usia pasien berbeda secara signifikan antara kelompok yang reccured dan tidak reccured (Recurred)?")
        st.markdown('''
        H0 : Tidak terdapat perbedaan rata-rata usia antara pasien yang mengalami reccured dan yang tidak.

        H1 : Terdapat perbedaan rata-rata usia antara pasien yang mengalami reccured dan yang tidak.

        Dalam konteks analisis ini, kita ingin mengetahui apakah usia pasien memiliki hubungan yang signifikan dengan kemungkinan terjadinya reccured kanker tiroid. Oleh karena itu, dilakukan uji t two sample independen terhadap dua kelompok: 
        pasien yang mengalami reccured (Recurred = Yes) dan pasien yang tidak (Recurred = No). 

        Hipotesis nol (H0) menyatakan bahwa tidak ada perbedaan rata-rata usia antara kedua kelompok tersebut, yang berarti usia bukan faktor yang membedakan terjadinya reccured. Sebaliknya, 

        hipotesis alternatif (H1) menyatakan bahwa terdapat perbedaan rata-rata usia yang signifikan antara kedua kelompok. Jika hasil uji menghasilkan p-value yang lebih kecil dari 0.05, maka kita menolak H0 dan menerima H1, yang menunjukkan bahwa usia pasien kemungkinan memiliki pengaruh terhadap reccured kanker.
        ''')
        st.pyplot(ep.eda6())
        st.markdown('''
                    Berdasarkan hasil uji t two sample yang ditampilkan pada grafik dan output di atas, diperoleh nilai t-statistik sebesar `4.52` dengan p-value sebesar `1.23 × 10⁻⁵`, yang berarti hasilnya signifikan secara statistik karena p-value jauh di bawah 0.05. Ini menunjukkan bahwa terdapat perbedaan rata-rata usia yang bermakna antara pasien yang mengalami reccured kanker tiroid dan yang tidak . Nilai Cohens d sebesar `0.549` mengindikasikan bahwa kekuatan perbedaan ini berada dalam kategori sedang, yang berarti cukup penting secara praktis. 
                    
                    Dari visualisasi boxplot, terlihat bahwa pasien yang mengalami reccured cenderung memiliki usia yang lebih tinggi dibandingkan dengan yang tidak kambuh. Di tujukan dengan median usia pasien yang kambuh lebih tinggi, dan rentang usia atas pada grup ini juga lebih lebar. Hal ini memperkuat interpretasi bahwa usia pasien dapat menjadi faktor risiko terhadap kemungkinan reccured kanker tiroid, sehingga kelompok usia lebih tua perlu mendapatkan perhatian lebih dalam pemantauan dan tindak lanjut pengobatan.
                    ''')
        st.markdown("---")
    
    elif eda == 'Apakah ada perbedaan usia yang signifikan antar kategori Stage?':
        # EDA 7
        st.markdown("## Apakah ada perbedaan usia yang signifikan antar kategori Stage?")
        st.markdown('''
                    H0 : Tidak terdapat perbedaan rata-rata usia yang signifikan antara kelompok stadium kanker (Stage).

                    H1 : Terdapat minimal satu kelompok stadium kanker yang memiliki rata-rata usia berbeda secara signifikan.

                    Dalam analisis ini, kita ingin mengetahui apakah terdapat perbedaan rata-rata usia pasien kanker tiroid berdasarkan stadium penyakitnya (Stage). Untuk menjawab pertanyaan tersebut, dilakukan uji ANOVA satu arah, karena kita membandingkan satu variabel numerik (usia) terhadap satu variabel kategorikal dengan lebih dari dua kategori (stadium I, II, III, dst.). 

                    Hipotesis nol (H0) menyatakan bahwa tidak ada perbedaan rata-rata usia antar kelompok stadium, yang berarti usia pasien tidak berpengaruh terhadap klasifikasi stadium kanker yang dialami. Sementara itu, 

                    hipotesis alternatif (H1) menyatakan bahwa terdapat paling tidak satu kelompok stadium yang memiliki rata-rata usia yang berbeda secara signifikan. Jika hasil uji ANOVA menunjukkan p-value < 0.05, maka H0 ditolak, sehingga kita dapat menyimpulkan bahwa usia pasien berpotensi berpengaruh terhadap stadium kanker yang dideritanya.
                    ''')
        st.pyplot(ep.eda7())
        st.markdown('''
                    === Hasil Uji ANOVA ===

                    F-statistik : 48.72

                    P-value     : 4.8382e-33

                    Eta Squared : 0.340
                    ''')
        st.markdown('''
                    Berdasarkan hasil uji ANOVA yang ditampilkan, diperoleh nilai F-statistik sebesar 48.72 dengan p-value sebesar 4.84 × 10⁻³³, yang jauh lebih kecil dari tingkat signifikansi 0.05. Hal ini menunjukkan bahwa terdapat perbedaan yang sangat signifikan secara statistik dalam rata-rata usia pasien antar kelompok stadium kanker tiroid. Selain itu, nilai effect size (Eta Squared) sebesar 0.34 mengindikasikan bahwa perbedaan tersebut bersifat kuat — artinya sekitar 34% variasi usia pasien dapat dijelaskan oleh perbedaan stadium kanker yang mereka alami.

                    Visualisasi dalam bentuk boxplot mendukung hasil tersebut, di mana terlihat bahwa pasien dengan stadium awal (seperti stadium I) cenderung memiliki usia lebih muda, sedangkan pasien pada stadium lanjut (seperti III dan IV) cenderung berusia lebih tua. Kesimpulannya, usia pasien merupakan faktor yang berasosiasi kuat dengan tingkat keparahan stadium kanker tiroid, sehingga usia dapat menjadi pertimbangan penting dalam penilaian awal risiko stadium kanker pada pasien.
                    ''')
        st.markdown("---")
    
if __name__ == "main":
    eda()