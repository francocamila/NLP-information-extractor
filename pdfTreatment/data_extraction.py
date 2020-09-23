import textract
import re
 
pdf_name = "./pdfs/6.pdf"
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


def get_named_ementa(paragraphs):
    '''
    Extracts the ementas that have a start word.
    Receives the clear text and returns the ementa.
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
                ementa = '\n'.join(texts)
                return ementa
        if mark == 1:
            texts.append(paragraph)

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


# paragraphs = cleanner(text)
# print("DATA EXTRATION:")
# print("------------------------------------------------------------------")
# print(get_orgao(paragraphs))
# print("------------------------------------------------------------------")
# print(get_processos(paragraphs))
# print("------------------------------------------------------------------")
# # Se a ementa tiver indicada com "assunto"
# print(get_named_ementa(paragraphs))
# print("------------------------------------------------------------------")
# # Se a ementa não tiver indicada
# print(get_unnamed_ementa(text))
# print("------------------------------------------------------------------")
