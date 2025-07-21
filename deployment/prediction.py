import streamlit as st
import pandas as pd
import pickle
import os

def run():
    # load saved files
    # save model yang udah dibuat
    model_path = os.path.join(os.path.dirname(__file__), "..", "src/model_SVM.pkl")
    with open(model_path, "rb") as f:
            model = pickle.load(f) 

    st.title("Prediksi Reccured Pasien Pasca Operasi")

    # buat form
    with st.form('pasien'):
        age = st.number_input('1. Masukan Usia', 0, 100, 15)
        gender = st.radio('Masukan Jenis Kelamin Anda',['Wanita','Pria'])
        smoking = st.radio('Apakah Anda Merokok?',['Ya','Tidak'],key="radio_smoking")
        r_smoking = st.radio('Apakah Punya Riwayat Merokok?',['Ya','Tidak'],key="radio_riwayat_smoking")
        r_radiothreapy = st.radio('Apakah Punya Riwayat Merokok?',['Ya','Tidak'])
        tf = st.selectbox('Bagaimana Fungsi Tiroid Anda?',['Euthyroid','Clinical Hyperthyroidism','Clinical Hypothyroidism','Subclinical Hyperthyroidism','Subclinical Hypothyroidism'])
        pe = st.selectbox('Bagaimana Hasil Pemeriksaan Tiroid Anda?',['Single nodular goiter-left','Multinodular goiter','Single nodular goiter-right','Normal','Diffuse goiter'])
        ade =  st.selectbox('Bagaimana Abnormalitas Kelenjar Getah Bening Anda?',['No','Right','Extensive','Left','Bilateral','Posterior'])
        patho = st.selectbox('Apa Jenis Sel Kanker Anda?',['Micropapillary','Papillary','Follicular','Hurthel cell'])
        foca = st.radio('Bagaimana Focality Tiroid Anda?',['Uni-Focal','Multi-Focal'])
        risk = st.radio('Bagaimana Tingkat Resiko Kanker Tiroid Anda?',['Low','Intermediate','High'])
        t = st.selectbox('Bagaimana Ukuran Penyebaran Kanker Tiroid Anda?',['T1a','T1b','T2','T3a','T3b','T4a','T4b'])
        n = st.selectbox('Bagaimana Penyebaran Kanker Tiroid Terhadap Kelenjar Getah Bening Anda?',['N0','N1b','N1a'])
        m = st.selectbox('Bagaimana Metastatis Anda?',['M0','M1'])
        stage = st.selectbox('Bagaimana Respon Hasil Terapi Anda?',['I','II','III','IVA','IVB'])
        response = st.selectbox('Bagaimana Tingkat Resiko Kanker Tiroid Anda?',['Indeterminate','Excellent','Structural Incomplete','Biochemical Incomplete'])
        
        submitted = st.form_submit_button("Submit")

        # mengganti format gender sesuai dengan kebutuhan model
        # gender
        if gender == 'Wanita' :
            gender = 'F'
        else:
            gender = 'M'
        # smoking
        if smoking == 'Ya' :
            smoking = 'Yes'
        else:
            smoking = 'No'
        # Hx Smoking
        if r_smoking == 'Ya' :
            r_smoking = 'Yes'
        else:
            r_smoking = 'No'
        # Hx Radiothreapy
        if r_radiothreapy == 'Ya' :
            r_radiothreapy = 'Yes'
        else:
            r_radiothreapy = 'No'

    # data inference
    data_input = {
    'Age' : age,
    'Gender' : gender,
    'Smoking' : smoking,
    'Hx Smoking' : r_smoking,
    'Hx Radiothreapy': r_radiothreapy,
    'Thyroid Function' : tf,
    'Physical Examination' : pe,
    'Adenopathy' : ade,
    'Pathology' : patho,
    'Focality' : foca,
    'Risk' : risk,
    'T' : t,
    'N' : n,
    'M' : m,
    'Stage' : stage,
    'Response' : response,
    }

    data = pd.DataFrame([data_input])
    reccured = model.predict(data)

    if reccured == 0 :
        hasil = 'Tidak Berpotensi Kambuh'
    else:
        hasil = 'Berpotensi Kambuh'

    if hasil == "Berpotensi Kambuh":
        st.markdown(f"""
        <div style="padding: 1rem; background-color: #ffe6e6; border-left: 5px solid red; border-radius: 5px;">
            <b style="color:red;">Hasil Penelitian Menyatakan Bahwa Anda: {hasil}</b>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="padding: 1rem; background-color: #e6ffed; border-left: 5px solid green; border-radius: 5px;">
            <b style="color:green;">Hasil Penelitian Menyatakan Bahwa Anda: {hasil}</b>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "main":
    run()