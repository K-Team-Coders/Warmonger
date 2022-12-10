import spacy
import pandas as pd
import nltk
from nltk import word_tokenize
import re
import string
import numpy as np

from pymystem3 import Mystem
mystem = Mystem() 

import re
import nltk
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from collections import Counter 
from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.cluster import MiniBatchKMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.utils import shuffle
import string
lst_stopwords = nltk.corpus.stopwords.words('russian')
lst_stopwords.extend(['…', '«', '»', '...'])
nlp = spacy.load('ru_core_news_sm')

def clean_text(text, tokenizer, stopwords):

    text = str(text).lower()  
    text = re.sub(r"\[(.*?)\]", "", text)  
    text = re.sub(r"\s+", " ", text)  
    text = re.sub(r"\w+…|…", "", text)  
    text = re.sub(r"(?<=\w)-(?=\w)", " ", text)  
    text = re.sub(
        f"[{re.escape(string.punctuation)}]", "", text
    )  

    tokens = tokenizer(text)  
    tokens = [t for t in tokens if not t in lst_stopwords]  
    tokens = ["" if t.isdigit() else t for t in tokens]  
    tokens = [t for t in tokens if len(t) > 1] 
    return tokens

def prep_tokens(df_raw):
    text_columns = ['text']
    #df_raw['content'] = df_raw['content'].fillna(" ")
    for col in text_columns:
        df_raw[col] = df_raw[col].astype(str)
    # создаем текст основанный на content title и tag
    df_raw["text"] = df_raw[text_columns].apply(lambda x: " | ".join(x), axis=1)
    df_raw["tokens"] = df_raw["text"].map(lambda x: clean_text(x, word_tokenize, lst_stopwords))
    _, idx = np.unique(df_raw["tokens"], return_index=True)
    df_raw = df_raw.iloc[idx, :]

    # Remove empty values
    df_raw = df_raw.loc[df_raw.tokens.map(lambda x: len(x) > 0), ["text", "tokens"]]
    return df_raw

# Векторизируем слова
def vectorize(list_of_docs, model):
    features = []

    for tokens in list_of_docs:
        zero_vector = np.zeros(model.vector_size)
        vectors = []
        for token in tokens:
            if token in model.wv:
                try:
                    vectors.append(model.wv[token])
                except KeyError:
                    continue
        if vectors:
            vectors = np.asarray(vectors)
            avg_vec = vectors.mean(axis=0)
            features.append(avg_vec)
        else:
            features.append(zero_vector)
    return features

def mbkmeans_clusters(X, k, mb=500, print_silhouette_values=False):

    km = MiniBatchKMeans(n_clusters=k, batch_size=mb).fit(X)
    print(f"For n_clusters = {k}")
    print(f"Silhouette coefficient: {silhouette_score(X, km.labels_):0.2f}")
    print(f"Inertia:{km.inertia_}")

    if print_silhouette_values:
        sample_silhouette_values = silhouette_samples(X, km.labels_)
        print(f"Silhouette values:")
        silhouette_values = []
        for i in range(k):
            cluster_silhouette_values = sample_silhouette_values[km.labels_ == i]
            silhouette_values.append(
                (
                    i,
                    cluster_silhouette_values.shape[0],
                    cluster_silhouette_values.mean(),
                    cluster_silhouette_values.min(),
                    cluster_silhouette_values.max(),
                )
            )
        silhouette_values = sorted(
            silhouette_values, key=lambda tup: tup[2], reverse=True
        )
        for s in silhouette_values:
            print(
                f"    Cluster {s[0]}: Size:{s[1]} | Avg:{s[2]:.2f} | Min:{s[3]:.2f} | Max: {s[4]:.2f}"
            )
    return km, km.labels_

def get_clust(X,k):
    clustering, cluster_labels = mbkmeans_clusters(X=X,k=k, print_silhouette_values=True)
    df_clusters = pd.DataFrame({
        "text": docs,
        "tokens": [" ".join(text) for text in tokenized_docs],
        "cluster": cluster_labels
    })
    return df_clusters

# Получи токены
prep_data=prep_tokens(df)
prep_data

model = Word2Vec(sentences=prep_data['tokens'].values, vector_size=100, window=5, min_count=1, workers=4)
vectorized_docs= vectorize(prep_data['tokens'], model=model)
print(len(vectorized_docs), len(vectorized_docs[0]))

prep_data['vectors'] =vectorized_docs
prep_data.fillna('')
print(prep_data)

get_clust(prep_data['vectors'].tolist(),3)

print("Самые популярные темы в кластере:")
k=3 # количесвто класетров ходных
slov1={}
for i in range(k):
    tokens_per_cluster = ""
    most_representative = model.wv.most_similar(positive=[clustering.cluster_centers_[i]], topn=5)
    for t in most_representative:
        tokens_per_cluster += f"{t[0]} "
        slov1[i]=tokens_per_cluster
print(slov1)

test_cluster = 1
most_representative_docs = np.argsort(
    np.linalg.norm(vectorized_docs - clustering.cluster_centers_[test_cluster], axis=1)
)
for d in most_representative_docs[:10]:
    print(docs[d])
    doc = nlp(docs[d])

# в переменной 'doc' теперь содержится обработанная версия текста
# мы можем делать с ней все что угодно!
# например, распечатать все обнаруженные именованные сущности
    for entity in doc.ents:
        print(f"{entity.text} ({entity.label_})")
    print("-------------")