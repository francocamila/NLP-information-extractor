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

spark = sparknlp.start()

print("Spark NLP version:", sparknlp.version())
print("Apache Spark version:", spark.version)

pipeline=PretrainedPipeline('entity_recognizer_sm', lang='pt')
text = "O meu nome é Gonzaguinha. Eu sou um cachorro. Moro em Brasília e gosto muito de comer pão de queijo."
result = pipeline.annotate(text)
print(list(result.keys()))
print(result['sentence'])
print(result['token'])
print(list(zip(result['token'], result['ner'])))
print(result['entities'])