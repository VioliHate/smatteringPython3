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
def print_twice(bruce):
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


#3.3 Scrivete una funzione che disegni una griglia come questa:
"""
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""
#.1
print(end='\n\n')

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def printSquare():
    printHoLevels()
    do_four(printVeLevels)
    printHoLevels()
    do_four(printVeLevels)
    printHoLevels()

def printHorizontalLevel():
    print('+ - - - -', end=' ')


def printVerticalLevel():
    print('|        ', end=' ')

def printHoLevels():
    do_twice(printHorizontalLevel)
    print('+')
    
def printVeLevels():
    do_twice(printVerticalLevel)
    print('|')
    
printSquare()
print(end='\n\n')
    
#.2 Scrivete una funzione che disegni una griglia simile, con quattro righe e quattro colonne.

def printHorizontal():
    do_four(printVerticalLevel)
    printHorizontalLevel
    print('|')


def printBigSquare():
    do_four(printHorizontalLevel)
    print('+')
    do_four(printHorizontal)
    do_four(printHorizontalLevel)
    print('+')
    do_four(printHorizontal)
    do_four(printHorizontalLevel)
    print('+')
    do_four(printHorizontal)
    do_four(printHorizontalLevel)
    print('+')
    do_four(printHorizontal)
    do_four(printHorizontalLevel)
    print('+')


printBigSquare()



























