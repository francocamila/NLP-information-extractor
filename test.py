import spacy

#Using BERT:
#Model in portuguese:
nlp = spacy.load('/home/camila/Documents/pt_bertlargeportuguesecased_lg')


#Test text:
doc = nlp(
    "Olá mundo! O Gonzaguinha é um cachorro. Ele gosta de dormir, comer e brincar!"
)

#Testing:


for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    token.shape_, token.is_alpha, token.is_stop)
#lemma: qual o lemmatization;
#pos: simple pos tagging;
#tag: detailed pos tagging;
#dep: dependency parsing;
#shape: the word shap;
#is aplha: is the token an alpha chracter?
#is stop: is the token part of a stop list? 

#NER:

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label)


