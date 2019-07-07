#1. Il volume di una sfera di raggio r è (4/3)pi r^3. Che volume ha una sfera di raggio 5?

radius=5
volume=(4/3)*3.14*(radius**3)
print('1. result:',volume)

#2. Il prezzo di copertina di un libro è € 24,95, ma una libreria ottiene il 40% di sconto.
# I costi di spedizione sono €3 per la prima copia e 75 centesimi per ogni copia aggiuntiva.
#Qual è il costo totale di 60 copie?

bookPriceForBookstore=24.95-24.95*40/100
shipping60=3+0.75*59

print('2. result:',bookPriceForBookstore*60+shipping60)

#3. Se uscite di casa alle 6:52 di mattina e correte 1 miglio a ritmo blando (8:15 al miglio),
# poi 3 miglia a ritmo moderato (7:12 al miglio), quindi 1 altro miglio a ritmo blando,
# a che ora tornate a casa per colazione?

startMinutes=52
startHours=6
easyPaceMinutes=8
easyPaceSeconds=15
moderateMinutes=7
moderateSeconds=12

calcRunningTimeMinutes=7*3+8*2
calcRunningTimeSeconds=easyPaceSeconds*2+moderateSeconds*3
calcRunningTimeMinutes+=(calcRunningTimeSeconds//60)
calcRunningTimeSeconds%=60
breakfastTimeMinutes=startMinutes+calcRunningTimeMinutes
breakfastTimeHours=startHours+breakfastTimeMinutes//60
breakfastTimeMinutes%=60
print('3. result:',breakfastTimeHours,':',breakfastTimeMinutes)

