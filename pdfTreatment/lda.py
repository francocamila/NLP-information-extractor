import pandas as pd
import re
from wordcloud import WordCloud
import nltk.corpus
#import matplotlib.pyplot as plt



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
print(howdy)
wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
wordcloud.generate(howdy)
image = wordcloud.to_image()
image.show()

