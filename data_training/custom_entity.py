import spacy

        LABEL_1 = "GANHOS EM DESAPROPRIAÇÃO"
        LABEL_2 = "PERMUTA DE BENS IMÓVEIS"

TRAIN_DATA = [
        ("Se remuneratória, ensejando a tributação.", {"entities": [(3, 16, LABEL_1)]}),
        ("o efetivo ganho de capital decorrente da indenização por desapropriação do imóvel,", {"entities": [(10, 26, LABEL_1)]}),
        ("mas sobre o ganho de capital apurado", {"entities": [(12, 28, LABEL_1)]}),
        ("haverá efetivo ganho de capital,", {"entities": [(15, 31, LABEL_1)]}),
        ("a indenização decorrente de desapropriação não é ganho de capital,", {"entities": [(49, 64, LABEL_1)]}),
        ("investimentos avaliados pelo custo de aquisição;", {"entities": [(38, 47, LABEL_1)]}),
        ("a aquisição da disponibilidade econômica ou jurídica de renda", {"entities": [(2, 11, LABEL_1)]}),
        ("aplicação de multa exigida isoladamente,", {"entities": [(0, 9, LABEL_1)]}),
        ("aplicação da multa isolada", {"entities": [(0, 9, LABEL_1)]}),
        ("a indenização decorrente de desapropriação não encerra ganho de capital,", {"entities": [(55, 71, LABEL_1)]}),
        ("comprovar o efetivo ganho de capital decorrente da indenização por desapropriação do imóvel,", {"entities": [(20, 36, LABEL_1)]}),
        ("apuração de ganho de capital,", {"entities": [(12, 28, LABEL_1)]})]
        
