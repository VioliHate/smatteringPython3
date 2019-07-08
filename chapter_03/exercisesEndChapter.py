#3.1 Scrivete una funzione chiamata giustif_destra che richieda una stringa s come
# parametro e stampi la stringa con tanti spazi iniziali da far sì che l’ultima lettera
#della stringa cada nella colonna 70 del display.

def giustif_destra(word):
    repeatSpace=70-len(word)
    print(' '*repeatSpace+word)

giustif_destra('I sleep all night and I work all day.')

#3.2
#.1 Scrivete questo esempio in uno script e provatelo.
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam') 
do_twice(print_spam)

#.2 Modificate do_twice in modo che accetti due argomenti,
# un oggetto funzione e un valore, e che chiami la funzione
# due volte passando il valore come argomento.

def do_twice(f,value):
    f(value)
    f(value)

def print_spam(valore):
    print(valore)

#.3 Copiate nel vostro script la definizione di print_twice che abbiamo
# visto nel corso di questo capitolo.
print('')
do_twice(print_spam,'hello')
def do_twice(bruce):
    print(bruce)
    print(bruce)
#.4 Usate la versione modificata di do_twice per chiamare
# do_twice per due volte, passando 'spam' come argomento.

print('')
do_twice(print_twice,'spam')

#.5 Definite una nuova funzione di nome fai_quattro che richieda un
# oggetto funzione e un valore e chiami la funzione per 4 volte,
# passando il valore come argomento. Dovrebbero esserci solo due
# istruzioni nel corpo di questa funzione, non quattro.

def do_four(f,value):
    do_twice(f,value)
    do_twice(f,value)
print('')
do_four(print_twice,'spam')
