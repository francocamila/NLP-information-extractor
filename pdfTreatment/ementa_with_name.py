import textract
import re
 
pdf_name = "./pdfs/4.PDF"
text = textract.process(pdf_name, method='pdfminer').decode('utf-8')

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
    paragraphs = re.split('\n', text)
    return paragraphs
    

def get_orgao(paragraphs):
    '''
    Gets the organization of each judgment and treats them.
    Returns the organization.
    '''
    keyword = "conselho"
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        if keyword in comparative_paragraph:
            orgao = paragraph
            break
    return orgao


def find_processos(text):
    '''
    Finds the process number.
    Receives the text and returns the occurrences of process numbers.
    '''
    pattern = r"\d{5}\.\d{5}.?\d\/\d{4}[^\d]\d{2}|\d{5}\.\d{3}.?\d{3}\/\d{2}(-| )\d{2}|\d{3}\.\d{3}.?\d{3}\/\d{2}(-| )\d{2}|\d{4}\.\d{3}.?\d{3}\/\d{2}(-| )\d{2}"
    return re.findall(pattern, text)


def get_processos(paragraphs):
    '''
    Treates and gets the first occurrence of the process number.
    '''
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        if find_processos(paragraph):
            out = paragraph
            break
    return out


def ementa_extract(paragraphs):
    '''
    Extracts the ementas from pdf's.
    Receives the text and returns the ementa.
    '''
    texts = []
    start = "assunto:"
    ends = ["vistos", "acordam"]
    mark = 0
    
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        if start in comparative_paragraph:
            mark = 1
        for end in ends: 
            if end in comparative_paragraph:
                mark = 2
        if mark == 1:
            texts.append(paragraph)
        if mark == 2:
            break
    ementa = '\n'.join(texts)
    return ementa

