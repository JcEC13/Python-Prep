def factorial(numero):
    if(type(numero)!=int):
        return 'El numero debe ser un entero'

    if(numero<0):
        return 'El numero debe ser poditivo'
    
    if(numero>1):
        numero=numero*factorial(numero-1)

    return numero

def convert(valor,origen,destino):
    if(origen=='C'):
        if(destino=='F'):
            valor = (valor*(9/5))+32
        if(destino=='K'):
            valor=valor+273.15
        if(destino=='C'):
            pass
    if(origen=='F'):
        if(destino=='F'):
            pass
        if(destino=='K'):
            valor= ((valor-32)*(5/9))+273.15
        if(destino=='C'):
            valor = (valor-32)*(5/9)
    if(origen=='K'):
        if(destino=='F'):
            valor= ((valor-273.15)*(9/5))+32
        if(destino=='K'):
            pass
        if(destino=='C'):
            valor = valor-273.15
    
    return valor

def is_prime(n):
  is_prime= True
  for i in range(2,n):
    if (n%i) == 0:
        is_prime= False
        break
  return is_prime


def imprimir_mayor(diccionario,maximo):
    for x in diccionario.items():
        if (maximo==x[1]):
            print(x)
    

def contar_elementos(lista):
    max=0
    dicc={}
    uni=list(set(lista))
    for count,x in enumerate(uni):
        count=0
        for i in lista:
            if(x==i):
                count+=1
        
        if(count>max):
            max=count   
        dicc['Elemento '+str(x)]=count
    
    imprimir_mayor(dicc,max)