# Conselho administrativo de recursos fiscais
import textract
import re
 
pdf_name = "48.pdf"
text = textract.process(pdf_name, method='pdfminer').decode('utf-8')

# separa a string em várias outras sempre que tiver duas quebras de linha:
paragraphs = re.split('\n', text) 

def get_orgao(text):
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
    pattern = r"\d{5}\.\d{5}.?\d\/\d{4}[^\d]\d{2}"
    return re.findall(pattern, text)


def get_processos(text):
    '''
    Treates and gets the first occurrence of the process number.
    '''
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        if find_processos(paragraph):
            try:
                out = str(find_processos(paragraph)).split("xad")
                out = out[0].replace("\\", " ") + out[1]
                out = str(out).strip("[], \\,  ''")
            except:
                out = str(find_processos(paragraph)).strip("[], ''")
            break
    return out


def ementa_extract(text):
    '''
    Extracts the ementas from pdf's.
    Receives the text and returns the ementa.
    '''
    texts = []
    start = "assunto:"
    end = "vistos"
    mark = 0
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        if start in comparative_paragraph:
            mark = 1
        if end in comparative_paragraph:
            break
        if mark:
            texts.append(paragraph)

    ementa = '\n'.join(texts)
    return ementa

