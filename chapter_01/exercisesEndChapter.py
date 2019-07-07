#1. Quanti secondi ci sono in 42 minuti e 42 secondi?

print('1. solution: (42x60)+42=',42*60+42)

#2. Quante miglia ci sono in 10 chilometri? Suggerimento: un miglio equivale a 1,61 km.
print('2. solution: 10x1.61=',10*1.61)

#3. Se correte una gara di 10 chilometri in 42 minuti e 42 secondi, qual è la vostra cadenza media
#   (tempo per miglio in minuti e secondi)? Qual è la vostra velocità media, in miglia all’ora?

print('3. solution:\nfirst convert km to mi -> 10x1.61=',10*1.61)
print('second convert m:s to h -> 42m42s to h: 42/60=',42/60,' + 42/(60x60)=',42/(60**2),'=',(42/60)+(42/(60**2)))
print('after use physics formula: speed= distance covered/time (mi/h) -> speed= ',10*1.61/(42/60)+(42/(60**2)))
print('now convert mi/h to m:s per mi -> m= INT(60/speed) s=((60/speed)-INT(60/speed))x60')
print('m= ',int (60/(10*1.61/(42/60)+(42/(60**2)))))
print('s= ',int (((60/(10*1.61/(42/60)+(42/(60**2)))-60//(10*1.61/(42/60)+(42/(60**2))))*60)))
print('final result ',int (60//(10*1.61/(42/60)+(42/(60**2)))),':',int (((60/(10*1.61/(42/60)+(42/(60**2)))-60//(10*1.61/(42/60)+(42/(60**2))))*60)),'m:s per mi')
