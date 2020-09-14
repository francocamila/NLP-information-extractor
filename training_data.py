import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["PATH"] = os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline

from sparknlp.annotator import *
from sparknlp.common import *
from sparknlp.base import *

from sparknlp.training import CoNLL


import sparknlp
spark = sparknlp.start()

#Loading training data a CoNLL dataset

training_data = CoNLL().readDataset(spark, "./inputs/train.ner")

#Loading BERT

bert = BertEmbeddings.load('./BertEmbeddings_bert-base-portuguese-cased')\
.setInputCols(["sentence", 'token'])\
.setOutputCol("bert")\
#.setCaseSensitive(False)\
#.setPoollingLayer(0)


nerTagger = NerDLApproach()\
.setInputCols(["sentence", "token", "bert"])\
.setLabelColumn("label")\
.setOutputCol("ner")\
.setMaxEpochs(1)\
.setRandomSeed(0)\
.setVerbose(1)\
.setValidationSplit(0.2)\
.setEvaluationLogExtended(True)\
.setEnableOutputLogs(True)\
.setIncludeConfidence(True)\
.setTestDataset("test.parquet")

#Loading test data
test_data = CoNLL().readDataset(spark, "./inputs/test.ner")
test_data = bert.transform(test_data)
#Results
test_data.write.parquet("test.parquet")

ner_pipeline = Pipeline(stages = [bert, nerTagger])
ner_model = ner_pipeline.fit(training_data)

ner_model.stages[1].write().save('./models/NER_bert_first')