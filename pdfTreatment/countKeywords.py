import textract
import re

pdf_name = "1.pdf"
text = textract.process(pdf_name, method='pdfminer').decode('utf-8')
paragraphs = re.split('\n\n', text) # os paragrafos sao elementos de uma lista

keywords = ['irpj', 'lucro real anual', 'antecipação',
            'antecipação mensal',
            'estimativa mensal',
            'multa isolada',
            'multa ofício',
            'não pagamento antecipado',
            'prejuízo fiscal',
            'suspenção de imposto',
            'redução de imposto',
            'atraso dctf',
            'lucro real',
            'compensação estimativa',
            'imposto retido na fonte',
            'selic compensação',
            'ajuste anual',
            'juros',
]
occurrences = {}
for paragraph in paragraphs:
    comparative_paragraph = paragraph.lower()
    for keyword in keywords:
        if keyword in comparative_paragraph:
            if keyword in occurrences:
                occurrences[keyword] += 1
            else:
                occurrences[keyword] = 1

print(occurrences)