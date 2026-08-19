codigo = input("codigo de rastreamento: ")
if codigo[0:1] in "BR" and codigo.endswith("BR"):
    print("codigo está certo")
else:
    print("codigo está errado")