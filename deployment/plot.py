import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_tiroid = pd.read_csv('src/Thyroid_Diff.csv')

def eda1():
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Plot histogram
    bars = sns.histplot(data_tiroid['Age'], bins=20, kde=True, ax=ax)

    # Tambahkan label angka di atas batang
    for patch in bars.patches:
        height = patch.get_height()
        if height > 0:
            ax.annotate(f'{int(height)}', 
                        xy=(patch.get_x() + patch.get_width() / 2, height),
                        xytext=(0, 5),
                        textcoords='offset points',
                        ha='center', va='bottom', fontsize=9)
    
    ax.set_title('Distribusi Umur Pasien')
    ax.set_xlabel('Umur')
    ax.set_ylabel('Jumlah Pasien')
    plt.tight_layout()

    return fig

def eda2():
    # Buat satu figure dengan dua subplot (axes)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Plot 1: Recurred berdasarkan Gender
    ax1 = sns.countplot(data=data_tiroid, x='Gender', hue='Recurred', ax=axes[0])
    ax1.set_title('Recurred berdasarkan Gender')
    ax1.set_xlabel('Gender')
    ax1.set_ylabel('Jumlah')

    # Tambahkan label angka di atas batang
    for p in ax1.patches:
        height = p.get_height()
        if height > 0:
            ax1.annotate(f'{height}',
                         (p.get_x() + p.get_width() / 2., height),
                         ha='center', va='bottom', fontsize=14)

    # Plot 2: Distribusi Gender Pasien
    ax2 = sns.countplot(data=data_tiroid, x='Gender', ax=axes[1])
    ax2.set_title('Distribusi Gender Pasien')
    ax2.set_xlabel('Gender')
    ax2.set_ylabel('Jumlah')

    for p in ax2.patches:
        height = p.get_height()
        if height > 0:
            ax2.annotate(f'{height}',
                         (p.get_x() + p.get_width() / 2., height),
                         ha='center', va='bottom', fontsize=14)

    plt.tight_layout()
    return fig

def eda3():
   # Gabungkan T, N, dan M menjadi kolom TNM
    data = data_tiroid.assign(TNM=data_tiroid['T'] + data_tiroid['N'] + data_tiroid['M'])

    # Buat figure dan axis
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot countplot
    sns.countplot(data=data, x='TNM', hue='Recurred', ax=ax)

    # Atur tampilan
    ax.set_title('Recurred berdasarkan Kombinasi TNM')
    ax.set_xlabel('Kombinasi TNM')
    ax.set_ylabel('Jumlah Pasien')
    ax.tick_params(axis='x', rotation=45)

    # Tambahkan label angka di atas batang
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f'{height}', 
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom',
                        fontsize=8)

    plt.tight_layout()
    return fig

def eda4():
    # Buat figure dan axis
    fig, ax = plt.subplots(figsize=(8, 5))

    # Buat countplot
    sns.countplot(data=data_tiroid, x='Response', hue='Recurred', ax=ax)

    # Judul dan label
    ax.set_title('Recurred berdasarkan Respons Terapi')
    ax.set_xlabel('Respons Terapi')
    ax.set_ylabel('Jumlah Pasien')
    ax.tick_params(axis='x', rotation=45)

    # Tambahkan angka di atas batang
    for p in ax.patches:
        height = p.get_height()
        if height > 0:
            ax.annotate(f'{int(height)}',
                        (p.get_x() + p.get_width() / 2., height),
                        ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    return fig

def eda5():
    # Buat tabel kontingensi
    ct_risk_stage = pd.crosstab(data_tiroid['Risk'], data_tiroid['Stage'])

    # plot histogram sebaran data rating
    plt.figure(figsize=(8, 5))
    fig= plt.figure()

    sns.heatmap(ct_risk_stage.div(ct_risk_stage.sum(axis=1), axis=0), annot=True, cmap='Blues', fmt=".2f")
    plt.title('Proporsi Stadium berdasarkan Risk (Heatmap)')
    plt.ylabel('Risk')
    plt.xlabel('Stage')
    plt.tight_layout()
    return fig

def eda6():
    # plot histogram sebaran data rating
    plt.figure(figsize=(8, 5))
    fig= plt.figure()

    # Visualisasi: Boxplot usia berdasarkan reccured
    sns.boxplot(data=data_tiroid, x='Recurred', y='Age')
    plt.title('Boxplot Usia berdasarkan Status reccured')
    plt.xlabel('reccured')
    plt.ylabel('Usia Pasien')
    plt.tight_layout()
    plt.show()
    return fig

def eda7():
    # plot histogram sebaran data rating
    plt.figure(figsize=(8, 5))
    fig= plt.figure()

    sns.boxplot(data=data_tiroid, x='Stage', y='Age')
    plt.title('Boxplot Usia berdasarkan Stadium Kanker')
    plt.xlabel('Stadium')
    plt.ylabel('Usia Pasien')
    plt.tight_layout()
    plt.show()
    return fig