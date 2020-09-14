# problemas:
# o textract nem sempre separa os paragrafos de forma correta
# os carimbos estão sujando algumas informações importantes
# 
import textract
import re
 
text = textract.process("48.pdf", method='pdftotext').decode('utf-8')
# separa a string em várias outras sempre que tiver duas quebras de linha:
paragraphs = re.split('\n\n', text) 

def get_processos(text):
    pattern = r"\d{5}\.\d{5}.?\d\/\d{4}[^\d]\d{2}"
    # r"\d{5}\.\d{6}\/\d{4}\-\d{2}"
    return re.findall(pattern, text)


def ementa_extract(paragraphs):
    '''
    extracts the ementas from pdf's.
    receives the paragraphs and return the ementa
    '''
    for paragraph in paragraphs:
        comparative_paragraph = paragraph.lower()
        if "assunto:" in comparative_paragraph:
            position_ementa = comparative_paragraph.find("assunto")
            ementa = paragraph[position_ementa:]
            break

    if "vistos" in comparative_paragraph:
        position_exc = comparative_paragraph.find("vistos")
        excludent = paragraph[position_exc:]
        ementa = ementa.replace(excludent, " ")
        
    return ementa


for paragraph in paragraphs:
    comparative_paragraph = paragraph.lower()
    if get_processos(paragraph):
        try:
            out = str(get_processos(paragraph)).split("xad")
            out = out[0].replace("\\", " ") + out[1]
            out = str(out).strip("[], \\,  ''")
        except:
            out = str(get_processos(paragraph)).strip("[], ''")
        print("Processo nº: ", out)
        break

print(ementa_extract(paragraphs))



        
