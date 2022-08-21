from re import X


x=0#declare var
while(x<=30):#cyclo declare with 30 steps
    print(x)#message on screen
    if(x == 4 or x == 6):#validation to skip numbers stablish
            x+=1#counter inside validation
            print("se salto el valor de:", x, "de x")#message on screen when x is equal to value determined
            continue#instruction to skip when value
    if(x==15):#validation to break when while is 30
        print("se rompio la ejecucion")
        break
    x+=1
    print("El valor del bucle es:", x)