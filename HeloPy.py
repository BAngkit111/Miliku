import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca dataset
customers_df = pd.read_excel("products_dataset-checkpoint.csv")
orders_df = pd.read_csv("orders_dataset-checkpoint.csv")

# Mengatur gaya visualisasi
sns.set(style='dark')

# Fungsi untuk mencari produk paling populer
def find_most_popular_product(df):
    frekuensi_produk = df['product_category_name'].value_counts()
    produk_terpopuler = frekuensi_produk.head(1)  # Ambil 10 nama teratas
    return produk_terpopuler

# Fungsi untuk menghitung keterlambatan pesanan
def count_delayed_orders(df):
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])

    df['delay'] = df['order_delivered_customer_date'] - df['order_estimated_delivery_date']

    jumlah_keterlambatan = len(df[df['delay'] > pd.Timedelta(0)])
    return jumlah_keterlambatan

# Fungsi untuk menampilkan dashboard
def show_dashboard():
    st.title("Dashboard")
    st.subheader("Statistics:")
    st.markdown(f"**Total Orders:** {len(orders_df)}")
    st.markdown(f"**Total Revenue:** $5000") 
    st.markdown(f"**Most Popular Product:** {find_most_popular_product(customers_df).index[0]}")
    
    st.subheader("Filters:")
    start_date = st.date_input("Start date")
    end_date = st.date_input("End date")
    product_category = st.selectbox("Product Category", ["Category A", "Category B", "Category C"])
    
    st.subheader("Analysis:")
    st.write("Here you can find various analysis tools and charts.")

# Fungsi untuk menampilkan data pengiriman pesanan
def show_delivery_status():
    jumlah_keterlambatan = count_delayed_orders(orders_df)
    
    st.title("Delivery Order Status")
    st.write("Jumlah pesanan yang mengalami keterlambatan:", jumlah_keterlambatan)
    
    # Visualisasi data
    st.subheader("Visualisasi Data keterlambatan pengiriman")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(['Terlambat', 'Tepat Waktu'], [jumlah_keterlambatan, len(orders_df) - jumlah_keterlambatan], color=['red', 'green'])
    ax.set_title('Status Pengiriman')
    ax.set_ylabel('Jumlah Pesanan')
    
    st.pyplot(fig)

# Fungsi untuk menampilkan analisis produk
def show_product_analysis():
    st.title("Product Analysis")
    
    st.write("DataFrame Pelanggan:")
    st.dataframe(customers_df)
    
    produk_terpopuler = find_most_popular_product(customers_df)
    
    st.write("Produk Terpopuler")
    st.write(produk_terpopuler)
    
    st.subheader("10 Produk apa yang paling diminati oleh pelanggan:")
    
    frekuensi_produk = customers_df['product_category_name'].value_counts().head(10)
    frekuensi_produk = frekuensi_produk.sort_values(ascending=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax = sns.barplot(x=frekuensi_produk.values, y=frekuensi_produk.index, palette="viridis")
    plt.title('10 Produk apa yang paling diminati oleh pelanggan')
    plt.xlabel('Frekuensi')
    plt.ylabel('Nama Produk')
    plt.tight_layout()
    
    st.pyplot(fig)

# Memanggil fungsi-fungsi untuk menampilkan konten
if __name__ == '__main__':
    show_dashboard()
    show_delivery_status()
    show_product_analysis()
