import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

customers_df = pd.read_csv("products_dataset.xls")

def find_most_popular_product(df):
    frekuensi_produk = df['product_category_name'].value_counts()
    produk_terpopuler = frekuensi_produk.head(1)  # Ambil 10 nama teratas
    return produk_terpopuler

# Streamlit interface
def main():
    st.title("Analisis Produk")
    
    # Tampilkan DataFrame jika diperlukan
    st.write("DataFrame Pelanggan:")
    st.dataframe(customers_df)
    
    # Temukan produk paling diminati
    produk_terpopuler = find_most_popular_product(customers_df)
    
    # Tampilkan produk paling diminati
    st.write("Produk Terpopuler")
    st.write(produk_terpopuler)
    
    # Visualisasi data
    st.subheader("10 Produk apa yang paling diminati oleh pelanggan:")
    
    # Memplot data dengan urutan terbalik
    frekuensi_produk = customers_df['product_category_name'].value_counts().head(10)  # Ambil 10 nama teratas
    frekuensi_produk = frekuensi_produk.sort_values(ascending=True)  # Urutkan dari yang terbesar
    
    # Buat plot menggunakan Seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.barplot(x=frekuensi_produk.values, y=frekuensi_produk.index, palette="viridis")
    
    
    # Tampilkan plot menggunakan st.pyplot() dengan meneruskan objek figur
    st.pyplot(fig)

if __name__ == '__main__':
    main()

 
df = pd.read_csv("orders_dataset-checkpoint.csv")

# Ubah kolom tanggal menjadi tipe datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

# Hitung keterlambatan
df['delay'] = df['order_delivered_customer_date'] - df['order_estimated_delivery_date']

# Hitung jumlah pesanan yang terlambat
jumlah_keterlambatan = len(df[df['delay'] > pd.Timedelta(0)])

# Streamlit interface
st.title("Status Pengiriman Pesanan")
st.write("Jumlah pesanan yang mengalami keterlambatan:", jumlah_keterlambatan)

# Visualisasi data
st.subheader("Visualisasi Data keterlambatan pengiriman")

# Buat plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(['Terlambat', 'Tepat Waktu'], [jumlah_keterlambatan, len(df) - jumlah_keterlambatan], color=['red', 'green'])
ax.set_title('Status Pengiriman')
ax.set_ylabel('Jumlah Pesanan')

# Tampilkan plot menggunakan st.pyplot() dengan meneruskan objek figur
st.pyplot(fig)

# Isi sisi bar dengan konten yang menarik
with st.sidebar:
    st.title('Dashboard')
    st.write('sidebar ini tidak ada terhubung dengan tabs maupun column')
    
    st.subheader('Statistics:')
    st.markdown('**Total Orders:** 1000')
    st.markdown('**Total Revenue:** $5000')
    st.markdown('**Most Popular Product:** cama_mesa_banho')
    
    st.subheader('Filters:')
    st.write('Select Date Range:')
    start_date = st.date_input("Start date")
    end_date = st.date_input("End date")
    
    st.write('Select Product Category:')
    product_category = st.selectbox("Product Category", ["Category A", "Category B", "Category C"])
    
    st.subheader('Analysis:')
    st.write('Here you can find various analysis tools and charts.')
