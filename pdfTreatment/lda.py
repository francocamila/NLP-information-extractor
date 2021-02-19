import pandas as pd
import re
from wordcloud import WordCloud
import nltk.corpus
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import seaborn as sns
sns.set_style('whitegrid')
#%matplotlib inline



processes=pd.read_csv('./dados_acordaos.csv')

#print(processes.head())
processes= processes.drop(columns=['orgao', 'processo', 'texto'])
#print(processes.head())

processes['process_text_processed'] = processes['ementa'].map(lambda x: re.sub('[,\.!?]', '', x))
processes['process_text_processed'] = processes['process_text_processed'].map(lambda x: x.lower())

#print(processes['process_text_processed'].head())
long_string = ','.join(list(processes['process_text_processed'].values))
stopwords= nltk.corpus.stopwords.words('portuguese')
long_string = long_string.split()

howdy=[]
for word in long_string:
    if word not in stopwords or not 'discutidos':
        howdy.append(word)

howdy = '\n'.join(howdy)
wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
wordcloud.generate(howdy)
image = wordcloud.to_image()
image.show()

# Helper function
def plot_10_most_common_words(count_data, count_vectorizer):
    words = count_vectorizer.get_feature_names()
    total_counts = np.zeros(len(words))
    for t in count_data:
        total_counts+=t.toarray()[0]
    
    count_dict = (zip(words, total_counts))
    count_dict = sorted(count_dict, key=lambda x:x[1], reverse=True)[0:10]
    words = [w[0] for w in count_dict]
    counts = [w[1] for w in count_dict]
    x_pos = np.arange(len(words)) 
    
    plt.figure(2, figsize=(15, 15/1.6180))
    plt.subplot(title='10 palavras mais comuns')
    sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth": 2.5})
    sns.barplot(x_pos, counts, palette='husl')
    plt.xticks(x_pos, words, rotation=90) 
    plt.xlabel('words')
    plt.ylabel('counts')
    plt.savefig("mygraph.png")

# Initialise the count vectorizer with the portuguese stop words
count_vectorizer = CountVectorizer(stop_words = stopwords)

# Fit and transform the processed titles
count_data = count_vectorizer.fit_transform(processes['process_text_processed'])

# Visualise the 10 most common words
plot_10_most_common_words(count_data, count_vectorizer)