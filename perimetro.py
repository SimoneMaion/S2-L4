def perimetroQuadrato (lato):
    return 4*lato
        
def circonferenzaCerchio (raggio):
    return raggio*3.14159*2
    
def perimetroRettangolo (lato1, lato2):
    return (lato1+lato2)*2

def perimetri():
    
    print (f"Questo software calcola il perimetro delle seguenti figure:\n1) Quadrato\n2) Cerchio \n3) Rettangolo")
    scelta = int(input("Scegli un elemento della lista inserendo il numero corrispondente: "))
    
    if scelta == 1:
        lato = float(input("Inserisci la misura del lato: "))   
        print ("Il perimetro del quadrato è ", perimetroQuadrato(lato))

    elif scelta == 2:
        raggio = float(input("Inserisci la misura del raggio: ")) 
        print ("La circonferenza del cerchio è ", circonferenzaCerchio(raggio))
        
    elif scelta == 3:
        lato1 = float(input("Inserisci la misura del primo lato: "))
        lato2 = float(input("Inserisci la misura del secondo lato: "))
        print ("Il perimetro del rettangolo è ", perimetroRettangolo(lato1, lato2))
        
    else:
        print ("Scelta non valida")
    
     
perimetri() 