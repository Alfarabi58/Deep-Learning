# Streamlit
import streamlit as st

# Pandas
import pandas as pd

# Visualisasi
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud

def run():
    # Membuat judul
    st.title('Coronavirus Tweets')

    # Membuat sub judul
    st.subheader('Project Deep Learning')

    st.divider()

    # Menambah Gambar dari url
    st.image('https://assets.rbl.ms/25591747/origin.jpg')

    # Membuat caption
    st.caption("Source: Google")

    st.divider()

    # Buat deskripsi
    st.title('Problem Statement')
    st.write('''
        Pandemi COVID-19 yang dimulai pada akhir 2019 telah memberikan dampak signifikan pada kehidupan manusia di seluruh dunia, tidak hanya dalam bidang kesehatan tetapi juga aspek sosial, ekonomi, dan psikologis. Menghadapi krisis ini, berbagai data terkait COVID-19, termasuk data tekstual dari berita, media sosial, dan laporan ilmiah, menjadi sumber informasi yang sangat berharga. Dataset "COVID-19 NLP Text Classification" dari Kaggle berisi teks terkait COVID-19 yang dapat dianalisis untuk mengklasifikasikan sentimen publik, tema diskusi, dan deteksi berita palsu. Analisis teks ini penting untuk membantu pemerintah dan organisasi kesehatan memahami reaksi masyarakat, menyaring informasi penting, dan merespons kebutuhan publik secara lebih efektif. Model NLP dan klasifikasi teks yang dikembangkan dari dataset ini dapat memberikan wawasan yang berharga untuk pengambilan keputusan yang lebih baik selama pandemi, memastikan respons yang tepat dan cepat terhadap berbagai tantangan yang muncul.
    ''')

    st.divider()

    st.title('Objective')
    st.write('''
        Menggunakan deep learning untuk menganalisis dataset "COVID-19 NLP Text Classification" adalah untuk mengembangkan model yang dapat mendeteksi dan mengklasifikasikan sentimen publik.
    ''')

    st.divider()

    # Menampilkan dataframe
    st.title('Data')
    df= pd.read_csv('Corona_NLP_train.csv',  encoding='latin-1')
    st.dataframe(df)
    st.write('''Data ini diambil dari Kaggle (https://www.kaggle.com/datasets/datatattle/covid-19-nlp-text-classification/data)''')

    st.divider()

    # Visualisasi
    st.title('Exploratory Data Analysis')

    # Menampilkan chart

    # Menghitung top 10 lokasi berdasarkan jumlah
    st.subheader('Distribution of Sentiments')
    top_locations = df['Location'].value_counts().head(10)
    # Create Plotly bar chart
    fig = px.bar(x=top_locations.values, y=top_locations.index, orientation='h',
             labels={'x': 'Count', 'y': 'Location'},
             color=top_locations.values, color_continuous_scale='viridis')
    st.plotly_chart(fig)
    st.write('''Bar chart diatas menunjukan bahwa lokasi yang paling sering melakukan tweet tentang covid adalah London.''')
    
    st.divider()

    # Plotting the distribution of classes
    st.subheader('Distribution of Sentiments')
    # Menggunakan Plotly Express untuk plotting
    fig = px.histogram(df, x='Sentiment', color='Sentiment')
    st.plotly_chart(fig)
    st.write('''Informasi dari bar chart diatas bahwa tweet terbanyak tentang covid19 adalah tweet positive dan tweet yang paling sedikit adalah tweet extreamly negative.''')

    st.divider()

    
    # Select positive tweets
    positive_tweets = df[df["Sentiment"] == "Positive"]
    # Fill NaN values in Location column
    positive_tweets["Location"].fillna("Unknown", inplace=True)
    # Select the top 5 countries where the most positive tweets were made
    top_positive_locations = positive_tweets["Location"].value_counts().nlargest(5)

    # Plotly figure for positive tweets
    st.subheader('Top Countries with Most Positive Tweets')
    fig_positive = px.bar(
    top_positive_locations,
    x=top_positive_locations.values,
    y=top_positive_locations.index,
    orientation='h',
    labels={'x': 'Number of Tweets', 'y': 'Country'},
    color=top_positive_locations.values,
    color_continuous_scale='viridis'
    )
    st.plotly_chart(fig_positive)
    st.write('''London menjadi lokasi terbanyak yang melakukan tweet positive.''')

    # Select negative tweets
    negative_tweets = df[df["Sentiment"] == "Negative"]
    # Fill NaN values in Location column
    negative_tweets["Location"].fillna("Unknown", inplace=True)
    # Select the top 5 countries where the most negative tweets were made
    top_negative_locations = negative_tweets["Location"].value_counts().nlargest(5)

    # Plotly figure for negative tweets
    st.subheader('Top Countries with Most Negative Tweets')
    fig_negative = px.bar(
    top_negative_locations,
    x=top_negative_locations.values,
    y=top_negative_locations.index,
    orientation='h',
    labels={'x': 'Number of Tweets', 'y': 'Country'},
    color=top_negative_locations.values,
    color_continuous_scale='viridis'
    )
    st.plotly_chart(fig_negative)
    st.write('''London juga menjadi lokasi terbanyak yang melakukan tweet negative.''')

    st.divider()

    # Menggabungkan semua teks pada kolom OriginalTweet dengan spasi
    allWords = ' '.join([tweet for tweet in df["OriginalTweet"]])
    # Membuat WordCloud
    wordCloud = WordCloud(width=500, height=300, random_state=2023).generate(allWords)
    # Aplikasi Streamlit
    st.subheader('WordCloud Example')
    # Menampilkan WordCloud menggunakan Plotly Express (px)
    fig = px.imshow(wordCloud)
    st.plotly_chart(fig)
    st.write('''Informasi diatas menunjukan bahwa kata-kata yang paling sering keluar pada OriginalTweet yaitu `https`, `COVID`, `t`, `co`, dll.''')

    st.divider()

    # Aggregate text by sentiment
    negative_text = ' '.join(df[df.Sentiment == 'Negative'].OriginalTweet.tolist())
    neutral_text = ' '.join(df[df.Sentiment == 'Neutral'].OriginalTweet.tolist())
    positive_text = ' '.join(df[df.Sentiment == 'Positive'].OriginalTweet.tolist())

    # Generate WordCloud objects
    negative_wordcloud = WordCloud().generate(negative_text)
    neutral_wordcloud = WordCloud().generate(neutral_text)
    positive_wordcloud = WordCloud().generate(positive_text)
    # Display using Plotly and Plotly Express in Streamlit
    st.subheader('Word Clouds by Sentiment')

    # Negative Word Cloud with Plotly
    st.write('#### Negative Sentiment Word Cloud')
    fig_neg = px.imshow(negative_wordcloud)
    st.plotly_chart(fig_neg)
    st.write('''Negative sentiment: kata-kata yang paling sering keluar yaitu `https`, `COVID`, `coronavirus`, `t`, `co`, dll.''')

    # Neutral Word Cloud with Plotly
    st.write('#### Neutral Sentiment Word Cloud')
    fig_neu = px.imshow(neutral_wordcloud)
    st.plotly_chart(fig_neu)
    st.write('''Neutral sentiment: kata-kata yang paling sering keluar yaitu `https`, `COVID`, `coronavirus`, `t`, `co`, dll.''')

    # Positive Word Cloud with Plotly
    st.write('#### Positive Sentiment Word Cloud')
    fig_pos = px.imshow(positive_wordcloud)
    st.plotly_chart(fig_pos)
    st.write('''Positve sentiment: kata-kata yang paling sering keluar yaitu `https`, `COVID`, `coronavirus`, `t`, `co`, dll.''')

if __name__ == '__main__':
    run()
