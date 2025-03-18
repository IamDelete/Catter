#generator simplu de parole pentru lrdv 
#09.03.2025
import random 
import string



def pas_gen():
    list_car = list(string.ascii_letters+string.digits)
    lung =  8
    parola  = ''.join(random.choice(list_car) for _ in range(lung))
    print (parola)
    return parola
    #'' actioneaza ca stringul gol initial in care se seleceaza random caractere
    # random choice alege random si merge cu lungimea lung 

if __name__ == "__main__":
    pas_gen()
