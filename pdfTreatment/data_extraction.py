import textract
import re
import json
import csv

pdf_name = "./acordaos-18-11-2020/40.PDF"
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
    orgao = ''
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
    pattern = r"\d{5}\.\d{5}.?\d\/\d{4}[^\d]\d{2}|\d?\d?\d{3}\.?\d{3}.?\d{3}\/\d{2}(-| )\d{2}|\d?\.?\d{3}.\d{3}"
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
    try:
        return out
    except:
        print("Process number not found")


def get_named_ementa(paragraphs):
    '''
    Extracts the ementas that have a start word.
    Receives the clear text and returns the ementa.
    '''
    texts = []
    starts = ["assunto:", "ementa:", " ementa ", "assunto"]
    ends = [" vistos ", "acordam", "vistos,"]
    mark = 0
    
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower() 
        if mark == 0:
            for start in starts:
                if start in comparative_paragraph:
                    print(paragraph)
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
    rest = []
    ends = ["vistos", "provido", "negado.", "acordam", "vistos,"] 
    mark = 0
    
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        for end in ends: 
            if end in comparative_paragraph:
                ementa = '\n'.join(texts[-5:])
                rest.append(ementa)
                mark = 1
                break
        if mark == 1:
            rest.append(paragraph)
        texts.append(paragraph)
    text = '\n'.join(rest)
    return ementa, text


def get_text(paragraphs):
    '''
    Extracts the rest of the text.
    Receives the paragraphs of entire document and returns the text.
    '''
    texts = []
    starts = ["assunto:", "ementa"]
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
    text = '\n'.join(texts)
    return text


def convert_to_json(paragraphs):
    '''
    Transfers all data to a json file.
    Receives the clear text and returns a json.
    '''
    if get_orgao(paragraphs):
        dados['orgao'] = get_orgao(paragraphs)
    else:
        dados['orgao'] = "Superior Tribunal de Justiça"

    dados['processo'] = get_processos(paragraphs)
    ## Se a ementa não tiver indicada
    # dados['ementa'], dados['texto'] = get_unnamed_ementa(text)

    ## Se a ementa estiver indicada
    # dados['ementa'] = get_named_ementa(paragraphs)
    # dados['texto'] = get_text(paragraphs)


    with open('./jsons/0.json', 'w') as fp:
                fp.write(json.dumps(dados, ensure_ascii=True, indent=4))


def convert_to_csv(paragraphs):
    '''
    Transfers all data to a csv file.
    Receives the clear text and returns a row in the csv table.
    '''
    if get_orgao(paragraphs):
        orgao = get_orgao(paragraphs)
    else:
        orgao = "Superior Tribunal de Justiça"

    processo = get_processos(paragraphs)
    ## Se a ementa tiver indicada com "assunto"
    # ementa = get_named_ementa(paragraphs)
    # texto = get_text(paragraphs)

    ## Se a ementa não tiver indicada
    # ementa, texto = get_unnamed_ementa(text)

    with open('dados_acordaos.csv', mode='a', newline='') as csv_file:
        fieldnames = ["nomePdf", "orgao", "processo", "ementa", "texto"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)    # Comment this line after reading the first file
        writer.writerow({
            "nomePdf": pdf_name, 
            "orgao": orgao, 
            "processo": processo, 
            "ementa": ementa, 
            "texto": texto
            })



paragraphs = cleanner(text)
# for paragraph in paragraphs:
#     print(paragraph)
#     print("---------")

# print(paragraphs)
# print("Orgao-----------")
# if get_orgao(paragraphs):
#     orgao = get_orgao(paragraphs)
# else:
#     orgao = "Superior Tribunal de Justiça"

# print(orgao)
# print("Processo--------")
# print(get_processos(paragraphs))
# print("Ementa---------")
print(get_unnamed_ementa(text)[0])
# print("Texto----------")
# print(get_unnamed_ementa(text)[1])
# convert_to_csv(paragraphs)
# convert_to_json(paragraphs)







