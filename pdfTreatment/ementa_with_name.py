filename = 'out.txt'
with open(filename, 'r') as file_object:
    lines = file_object.readlines()
    for i in lines:
        position_ementa = i.find("Ementa")
        position_exc = i.find("Vistos")
        start_ementa = i[position_ementa:]
        excludent = i[position_exc:]

file_object.close()

ementa = start_ementa.replace(excludent, " ")
print(ementa)




        
