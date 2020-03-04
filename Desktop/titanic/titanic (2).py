
import numpy as np
import pandas as pd
import statistics 
import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import defaultdict


#клас "вижив", "ім'я", "секс", "вік", "сібсп", "парч", "квиток", "вартість проїзду", "каюта", "запланована", "човен", "тіло", "home.dest"

    
data = pd.read_csv('titanic.csv', sep=',', quotechar = '"', encoding="utf8")
count = len(data)

labels = 'alive', 'dead'


countSurv = data[data['survived'] == 1] ['survived'].count()
countDead = data[data['survived'] == 0] ['survived'].count()

fig1, ax1 = plt.subplots()

plt.title('Діаграма втрат')
ax1.pie([countSurv, countDead], labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

plt.legend(('{:s} = {:d}'.format(labels[0], countSurv), '{:s} = {:d}'.format(labels[1], countDead)))
plt.show()


classes = data['pclass'].unique()

Surv = data[data['survived'] == 1]
Dead = data[data['survived'] == 0]

dataByClass = []
for c in classes:
    countSurvCl = Surv[Surv['pclass'] == c] ['pclass'].count() 
    countDeadCl = Dead[Dead['pclass'] == c] ['pclass'].count() 
    dataByClass.append([countSurvCl, countDeadCl])
    
dataByClass[0]



fig, ax = plt.subplots()
fig.set_size_inches(10,4)


for i in range(len(dataByClass)):
    plt.subplot(131+i)
    plt.pie( dataByClass[i], labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('{:d} клас'.format(i+1))


textstr = ''
for i in range(len(dataByClass)):
    textstr += '{:d} клас:\nВижило - {:d}\nЗагинуло - {:d}\n------------------------------\n'.format(i+1, dataByClass[i][0], dataByClass[i][1])

props = dict(facecolor='white', alpha=0.5)
plt.text(0, 0.90, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox = props)
plt.show()


ages = data['age'].value_counts()

deadbyage = Dead['age'].value_counts()

survbyage = Surv['age'].value_counts()

fig, ax = plt.subplots()
fig.set_size_inches(15,4)
width = 0.15
ax.yaxis.grid(True)

xsurv = survbyage.index.values.tolist()
xdead = deadbyage.index.values.tolist()

plt.title('Виживші/Загиблі за віком')
#rects1 = ax.bar([x - width for x in xsurv], survbyage, width, label='Alive')
#rects2 = ax.bar([x + width for x in xdead], deadbyage, width, label='Dead')

p1 = plt.bar([x+width for x in survbyage.index.values], survbyage, width, label='survived')
p2 = plt.bar([x-width for x in deadbyage.index.values], deadbyage, width, label='dead')

plt.legend()
plt.show()

foundedBody = Dead['body'].count()
NotfoundedBody = len(Dead) - foundedBody

print ('Знайденно тіл - {}\n'.format(foundedBody))
print ('Не знайденно тіл - {}\n'.format(NotfoundedBody))


destData = data['home.dest'].value_counts()
nancount = len(data['home.dest']) - data['home.dest'].count() 


destDataDict = destData.to_dict()


destData[:10:].index.values


fig, ax = plt.subplots()
fig.set_size_inches(10,4)
width = 0.7
ax.yaxis.grid(True)
plt.axis([0, 70, 0, 70])

plt.title('Кількість пасажирів за походженням')

x = np.arange(1,len(destData)+1)

plt.bar(x, destData, width, )

textstr = ''
num = 1 
for dist in destData[:10:].index.values:
    textstr += '{:d}) {:s}\n'.format(num, dist)
    num += 1
   
plt.text(40, 5, textstr)
plt.show()



