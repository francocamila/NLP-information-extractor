import textract
import re
from .models import Jugdments


def occurrences_keywords(paragraphs):
    '''
    Occurrences counter of judgments keywords.
    Receives the paragraphs of the text,
    returns a dictionary of keywords and occurrences.
    '''
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
    return occurrences


def save_db(lastest_file, occurrences_keywords):
    for occurrence in occurrences_keywords.items():
        judgments = Judgments(title = lastest_file, keyword = occurrence[0], count = occurrence[1])
        judments.save()


def cleanner(text):
    '''
    Cleans some parts unwanteds and prepares the text for extration
    Add new words in the variable 'keywords' whenever necessary
    '''
    blocks = re.split('\n\n', text)
    keywords = ["assinado", "fl. 2", "df carf mf",]
    for block in blocks:
        comparative_paragraph = block.lower()
        for keyword in keywords:
            if keyword in comparative_paragraph:
                position_exc = comparative_paragraph.find(keyword)
                excludent = block[position_exc:]
                text = text.replace(excludent, " ")
    clean_paragraphs = re.split('\n', text)
    return clean_paragraphs


def get_orgao(clean_paragraphs):
    '''
    Gets the organization of each judgment and treats them.
    Returns the organization.
    '''
    orgao = ''
    keyword = "conselho"
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        if keyword in comparative_paragraph:
            orgao = paragraph
            break
    if orgao:
        return orgao
    else:
        return "Superior Tribunal de Justiça"


def find_processos(text):
    '''
    Finds the process number.
    Receives the text and returns the occurrences of process numbers.
    '''
    pattern = r"\d{5}\.\d{5}.?\d\/\d{4}[^\d]\d{2}|\d?\d?\d{3}\.?\d{3}.?\d{3}\/\d{2}(-| )\d{2}|\d?\.?\d{3}.\d{3}"
    return re.findall(pattern, text)


def get_processos(clean_paragraphs):
    '''
    Treates and gets the first occurrence of the process number.
    '''
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        if find_processos(paragraph):
            out = paragraph
            break
    try:
        return out
    except:
        print("Process number not found")


def get_named_ementa(clean_paragraphs):
    '''
    Extracts the ementas that have a start word.
    Receives the clear text and returns the ementa.
    '''
    texts = []
    starts = ["assunto:", "ementa"]
    ends = ["vistos", "acordam", "acórdão"]
    mark = 0
    
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        if mark == 0:
            for start in starts:
                if start in comparative_paragraph:
                    mark = 1
                    break    
        if mark == 1:
            texts.append(paragraph)
            for end in ends: 
                if end in comparative_paragraph:
                    ementa = '\n'.join(texts)
                    return ementa


def get_unnamed_ementa(text):
    '''
    Extracts the ementas that do not have a start word.
    Receives the pure text and returns the ementa.
    '''
    paragraphs = re.split('\n\n', text)
    texts = []
    ends = ["vistos", "acordam"]
    
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        for end in ends: 
            if end in comparative_paragraph:
                ementa = '\n'.join(texts[-2:])
                return ementa  
        texts.append(paragraph)