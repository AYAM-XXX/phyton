reta1, reta2, reta3 = map(int, input("insira as retas: ").split())

if(((reta1 + reta2)  > reta3) and ((reta2 + reta3)  > reta1) and ((reta1 + reta3)  > reta2) ):
    if( reta1 == reta2 == reta3):
        print("equilatero")
    elif((reta1  == reta2) or (reta2  == reta1) or (reta3 == reta2)):
        print(("isoceles"))
    else:
        print(("escaleno"))
else:
    print("não pode ser definido um triangulo")


