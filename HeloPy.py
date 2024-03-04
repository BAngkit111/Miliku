import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Membaca dataset
order_review = pd.read_csv("order_reviews_dataset-checkpoint.csv")
orders_df = pd.read_csv("orders_dataset-checkpoint.csv")

# Mengatur gaya visualisasi
sns.set(style='dark')

# Fungsi untuk mencari rata-rata review produk
def find_average_review(df):
    rata_rata_review = df['review_score'].mean()
    return rata_rata_review

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
    st.sidebar.title("Dashboard")  
    st.sidebar.subheader("Statistics:")  
    st.sidebar.markdown(f"**Total Orders:** {len(orders_df)}")
    st.sidebar.markdown(f"**Total Revenue:** $5000")  
    st.sidebar.markdown(f"**Average Review Score:** {find_average_review(order_review)}")
    
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
    
    st.subheader("Average Review Score:")
    rata_rata_review = find_average_review(order_review)
    st.write(rata_rata_review)
    
    st.subheader("Visualisasi Rata-rata Nilai Review:")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar('Rata-rata', rata_rata_review, color='green')
    ax.set_title('Rata-rata Nilai Review')
    ax.set_xlabel('Review')
    ax.set_ylabel('Nilai Rata-rata')
    ax.set_ylim(0, 5)  
    st.pyplot(fig)

# Memanggil fungsi-fungsi untuk menampilkan konten
if __name__ == '__main__':
    show_dashboard()
    show_delivery_status()
    show_product_analysis()
