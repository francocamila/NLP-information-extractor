# problemas:
# o textract nem sempre separa os paragrafos de forma correta
# os carimbos estão sujando algumas informações importantes

import textract
import re
 
text = textract.process("6.pdf", method='pdftotext').decode('utf-8')

#separa a string em várias outras sempre que tiver duas quebras de linha:
paragraphs = re.split('\n\n', text) 

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
        
# print(ementa)



        
