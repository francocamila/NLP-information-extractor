import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]
import sys
import time

import sparknlp
from sparknlp.pretrained import PretrainedPipeline
from sparknlp.annotator import *
from sparknlp.common import RegexRule
from sparknlp.base import *
import pyspark.sql.functions as F

spark = sparknlp.start()

print("Spark NLP version:", sparknlp.version())
print("Apache Spark version:", spark.version)

#pipeline=PretrainedPipeline('entity_recognizer_sm', lang='pt')


document = DocumentAssembler()\
    .setInputCol("text")\
    .setOutputCol("document")

sentence = SentenceDetector()\
    .setInputCols(['document'])\
    .setOutputCol('sentence')

token = Tokenizer()\
    .setInputCols(['sentence'])\
    .setOutputCol('token')

bert = BertEmbeddings.load('./BertEmbeddings_bert-base-portuguese-cased')\
    .setInputCols(["sentence", 'token'])\
    .setOutputCol("bert")

loaded_ner_model = NerDLModel.load('./models/NER_bert_first')\
    .setInputCols(["sentence", "token", "bert"])\
    .setOutputCol("ner")

converter = NerConverter()\
    .setInputCols(["document", "token", "ner"])\
    .setOutputCol("ner_span")

#Custom pipeline

custom_ner_pipeline = Pipeline(
    stages = [
        document,
        sentence,
        token,
        bert,
        loaded_ner_model,
        converter
    ]
)

text = "Campos do Jordão é um município que recebe bastante turistas ao longo do ano. A maior parte das pessoas costuma ir até lá nos meses em que faz frio, pois há mais atrações nessas épocas.\
A cidade também é conhecida pela grande quantidade de comidas típicas de inverno, como chocolate quente, por exemplo. No lugar há diversões para gostos variados\
Pessoas de várias regiões do país costumam frequentar Campos do Jordão. Há turistas que também vem de países estrangeiros vizinhos ou mais afastados para aproveitarem tudo o que a cidade oferece na alta temporada."

prediction_data = spark.createDataFrame([[text]]).toDF("text")
prediction_model = custom_ner_pipeline.fit(prediction_data)
#prediction_model = pipeline(prediction_data)
preds = prediction_model.transform(prediction_data)
preds.show()
preds.select('token.result', 'ner.result').show(truncate=False)

#prettier
preds.select(F.explode(F.arrays_zip("ner_span.result", "ner_span.metadata")).alias("entities"))\
.select(F.expr("entities['0']").alias("chunk"),
        F.expr("entities['1'].entity").alias("entity")).\
        show(truncate=False)