
#PlottingPieChart

import matplotlib.pyplot as plt

def main():
    #Create a list of values
    values = [20, 60, 80, 40]
    
    #Create a pie chart from the values
    plt.pie(values)
    
    #Display the pie chart
    plt.show()
    
main()

def main1():
    sales = [100, 400, 300, 600]
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
    
    plt.pie(sales, labels=slice_labels)
    plt.title('Sales by Quarter')
    plt.show()
    
main1()
