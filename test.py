#!/usr/bin/env python
import spacy
import plac
from spacy import displacy
from spacy.util import minibatch
import torch
import random
import thinc
from tqdm.auto import tqdm
import unicodedata
import wasabi
import numpy
from collections import Counter




@plac.annotations(
    model=("Model to load (needs parser and NER)", "positional", None, str)
)
def main(model='/home/camila/Documents/pt_bertbaseportuguesecased_lg'):
    is_using_gpu = spacy.prefer_gpu()
    if is_using_gpu:
        torch.set_default_tensor_type("torch.cuda.FloatTensor")
    nlp = spacy.load(model)
    print("Loaded model '%s'" % model)
    #print("Processing %d texts" % len(TEXTS))

    doc = ("Aqui está um texto, é isso aí.")
    
    print(doc._.trf_word_pieces_) # String values of the wordpieces
    


if __name__ == "__main__":
    plac.call(main)
                                                                                                                                                                                                                                            