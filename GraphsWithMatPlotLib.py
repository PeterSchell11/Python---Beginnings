

#Plotting List Data ith mathplotlib package
#
#windows on command prompt
#	pip install matplotlib
#mac on terminal
#	sudo pip3 install matplotlib

import matplotlib.pyplot as graph

x_coords=[0,1,2,3,4]
y_coords=[0,3,1,5,2]

graph.plot(x_coords,y_coords)
#plt.show()
#display  markers
#graph.plot(x_coords,y_coords, marker='v')#can use 'o','v','*' google symbols

#adding axis titles, labels and grid

graph.title('Sample Data') #Title

graph.xlabel('X axis label')#labesl
graph.ylabel('Y axis label')

graph.grid(True)#grid T or F

#graph.show()

graph.xlim(xmin=1, xmax=10)#axis limits
graph.ylim(ymin=1,ymax=6)

#graph.show()

#customize tick marks
graph.xticks([0,1,2,3,4],['2016','2017','2018','2019','2020'])
graph.yticks([0,1,2,3,4,5],['$0M','$1M','$2M','$3M','$4M','$5M'])
graph.show()

#display  markers
#graph.plot(x_coords,y_coords, marker='v')


#examples
import matplotlib.pyplot as graph1
import matplotlib.pyplot as graph2

x_coords=[1,2,5,3]
y_coords=[5,1,10,4]

graph1.plot(x_coords,y_coords, marker='v')

graph1.title('Sample Data') 

graph1.xlabel('X axis label')
graph1.ylabel('Y axis label')

graph1.grid(True)


graph1.show()

xaxis=[1,2,5,3,5,4,3,2]
yaxis=[5,1,10,4,4,5,3,2]


graph2.plot(xaxis,yaxis, marker='v')

graph2.title('Sample Data') 

graph2.xlabel('X axis label')
graph2.ylabel('Y axis label')

graph2.show()

#bar graph

import matplotlib.pyplot as graph3



def main():
    
    x_coords=[0,10,20,30,40]
    y_coords=[100,200,300,400,500]

    graph3.bar(x_coords,y_coords,4, color=('r','g','b','y','k'))
    #4 is the bar width

    graph3.title('Sample Data') 

    graph3.xlabel('X axis label')
    graph3.ylabel('Y axis label')

    graph3.show()

main()





