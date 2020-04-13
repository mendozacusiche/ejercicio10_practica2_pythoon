imagenes=['im1','im2','im3']

listas1 = []

cordenadas = []

while len(cordenadas) != 6:
    
    x = int(input("Ingrese la cordenada x :"))
    y = int(input("Ingrese la cordenada y :"))
    
    if len(cordenadas) == 0:
        
        cordenadas.append(x)
        cordenadas.append(y)
    elif len(cordenadas) == 2:
        
        if (cordenadas[0] != x) and  (cordenadas[1] != y):
             cordenadas.append(x)
             cordenadas.append(y)
         
    elif len(cordenadas) == 4:
        if ((cordenadas[0] != x) and  (cordenadas[1] != y) or (cordenadas[2] != x) and  (cordenadas[3] != y)):
            
            cordenadas.append(x)
            cordenadas.append(y)
     
    print(cordenadas)        
  
listas1 = []

for i in range(3):
 
    listas1.append(imagenes[i])
    listas1.append(cordenadas[i])
    listas1.append(cordenadas[i + 1])
    
print(listas1)