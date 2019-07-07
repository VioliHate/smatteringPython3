#3.1 Scrivete una funzione chiamata giustif_destra che richieda una stringa s come
# parametro e stampi la stringa con tanti spazi iniziali da far sì che l’ultima lettera
#della stringa cada nella colonna 70 del display.

def giustif_destra(word):
    repeatSpace=70-len(word)
    print(' '*repeatSpace+word)

giustif_destra('I sleep all night and I work all day.')
