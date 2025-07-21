import pandas as pd
import streamlit as st

def home():    
    # judul
    st.title("Deteksi Reccured Kanker Tiroid Terdiferensiasi (Differentiated Thyroid Cancer) menggunakan Machine Learning:")
    st.markdown("---")
    # deskripsi
    st.markdown("## Latar Belakang :")
    st.markdown('''

    (Differentiated Thyroid Cancer/DTC) merupakan jenis kanker yang umumnya memiliki prognosis baik atau tidak terlalu ganas, tetapi tetap berisiko kambuh kembali (recurrence). Mendekteksi lebih awal terhadap potensi kambuh ini sangat penting agar dokter dapat melakukan pemantauan lebih intensif dan perencanaan terapi yang tepat pasca operasi. sebagai data science saya akan membuat model machine learning untuk memudahkan dokter mengontrol pasien mereka pasca 
                ''')
    st.markdown("## Rumusan Masalah :")
    st.markdown('''           
    dalam waktu 1 minggu ini harus membuat sebuah model machine learning untuk memprediksi apakah penyakit DTC ini akan kambuh kembali atau tidak berdasarkan data klinis, dengan mempertimbangkan nilai recall yang baik dengan confident level 99% karena disini konteks kesehatan harus lebih yakin, dan dengan semua yang sudah di buat harapanya kerja dokter dalam mengontrol pasienya dapat terbantu.
                ''')
    
    st.markdown("---")

    # dataset
    st.markdown("# Dataset")
    data_tiroid = pd.read_csv('src/Thyroid_Diff.csv')
    st.dataframe(data_tiroid.head(5))

    st.markdown("---")

    # data overview
    st.markdown("### Data Overview", unsafe_allow_html=True)

    st.markdown("""
        <table>
        <thead>
        <tr><th>Kolom</th><th>Penjelasan</th></tr>
        </thead>
        <tbody>
        <tr><td>Age</td><td>Usia pasien dalam tahun. Tipe data numerik (int64). Range usia dari 15 hingga 82 tahun.</td></tr>
        <tr><td>Gender</td><td>Jenis kelamin pasien: <code>M</code> (laki-laki), <code>F</code> (perempuan).</td></tr>
        <tr><td>Smoking</td><td>Apakah pasien saat ini merokok (<code>Yes</code>/<code>No</code>).</td></tr>
        <tr><td>Hx Smoking</td><td>Riwayat pernah merokok sebelumnya (<code>Yes</code>/<code>No</code>). Bisa <code>Yes</code> walau saat ini sudah berhenti.</td></tr>
        <tr><td>Hx Radiotherapy</td><td>Riwayat pernah menjalani terapi radiasi (<code>Yes</code>/<code>No</code>).</td></tr>
        <tr><td>Thyroid Function</td>
        <td>
        Status fungsi tiroid berdasarkan tes laboratorium:<br>
        – <code>Euthyroid</code>: normal<br>
        – <code>Clinical Hyperthyroidism</code>: kadar hormon tinggi<br>
        – <code>Clinical Hypothyroidism</code>: hormon rendah<br>
        – <code>Subclinical Hyperthyroidism/Hypothyroidism</code>: gangguan ringan, tidak bergejala jelas
        </td></tr>
        <tr><td>Physical Examination</td>
        <td>
        Hasil pemeriksaan fisik tiroid:<br>
        – <code>Multinodular goiter</code>: benjolan banyak<br>
        – <code>Single nodular goiter-left/right</code>: satu benjolan<br>
        – <code>Diffuse goiter</code>: pembesaran menyebar<br>
        – <code>Normal</code>: tidak ada benjolan terdeteksi
        </td></tr>
        <tr><td>Adenopathy</td>
        <td>
        Pembesaran atau abnormalitas kelenjar getah bening:<br>
        <code>Right</code>, <code>Left</code>, <code>Bilateral</code>, <code>Posterior</code>, <code>Extensive</code>, atau <code>No</code>
        </td></tr>
        <tr><td>Pathology</td>
        <td>
        Jenis sel kanker:<br>
        – <code>Papillary</code>: paling umum dan cenderung tumbuh lambat<br>
        – <code>Follicular</code>: lebih jarang, bisa menyebar ke pembuluh darah<br>
        – <code>Micropapillary</code>: bentuk kecil dari papillary<br>
        – <code>Hurthel cell</code>: varian lebih agresif
        </td></tr>
        <tr><td>Focality</td>
        <td>
        Fokus lesi:<br>
        – <code>Uni-Focal</code>: satu titik kanker<br>
        – <code>Multi-Focal</code>: banyak titik dalam kelenjar tiroid
        </td></tr>
        <tr><td>Risk</td><td>Tingkat risiko kanker berdasarkan kombinasi faktor seperti ukuran tumor dan penyebaran: <code>Low</code>, <code>Intermediate</code>, atau <code>High</code>.</td></tr>
        <tr><td>T</td>
        <td>
        Ukuran dan penyebaran lokal tumor:<br>
        – <code>T1a</code>: Tumor ≤1 cm dan terbatas di tiroid<br>
        – <code>T1b</code>: Tumor >1 cm tapi ≤2 cm, terbatas di tiroid<br>
        – <code>T2</code>: Tumor >2 cm tapi ≤4 cm, masih di dalam tiroid<br>
        – <code>T3a</code>: Tumor >4 cm, tetap terbatas di tiroid<br>
        – <code>T3b</code>: Tumor dengan invasi minimal ke jaringan sekitar (misalnya otot)<br>
        – <code>T4a</code>: Tumor menyebar ke struktur sekitar (misalnya trakea, laring)<br>
        – <code>T4b</code>: Tumor menyebar ke struktur vital (pembuluh besar, tulang belakang, dll)
        </td></tr>
        <tr><td>N</td>
        <td>
        Penyebaran ke kelenjar getah bening:<br>
        – <code>N0</code>: tidak ada penyebaran<br>
        – <code>N1a</code>: ke kelenjar sekitar tiroid<br>
        – <code>N1b</code>: ke kelenjar jauh
        </td></tr>
        <tr><td>M</td>
        <td>
        Metastasis jauh:<br>
        – <code>M0</code>: tidak ada metastasis<br>
        – <code>M1</code>: sudah menyebar ke organ jauh
        </td></tr>
        <tr><td>Stage</td>
        <td>
        Stadium kanker keseluruhan berdasarkan TNM (I, II, III, IVA, IVB).<br>
        <b>Rumus Penentuan Stage:</b><br>
        – <code>Stage I</code>: T1–T3, N0, M0<br>
        – <code>Stage II</code>: T1–T3, N1, M0<br>
        – <code>Stage III</code>: T4a, Any N, M0<br>
        – <code>Stage IVA</code>: T4b, Any N, M0<br>
        – <code>Stage IVB</code>: Any T, Any N, M1
        </td></tr>
        <tr><td>Response</td>
        <td>
        Respons pasien terhadap terapi:<br>
        – <code>Excellent</code>: sembuh atau tanpa bukti sisa kanker<br>
        – <code>Indeterminate</code>: hasil tidak pasti<br>
        – <code>Structural Incomplete</code>: masih ada massa tumor<br>
        – <code>Biochemical Incomplete</code>: hormon tumor masih tinggi tapi tidak terlihat tumor
        </td></tr>
        <tr><td>Recurred</td><td>Apakah kanker kambuh setelah pengobatan? (<code>Yes</code>/<code>No</code>)</td></tr>
        </tbody>
        </table>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Model yang digunakan
    st.markdown("## Algoritma yang Digunakan dalam Pemodelan")
    st.markdown('''
                Support Vector Machine (SVM) menjadi terbaik dalam penelitian ini dengan recall train sebesar `0.98` dan recall test sebesar `0.95`.
                ''')
    
    st.markdown("---")



if __name__ == "main":
    home()