# Y Nhi Tran
# Final part 1
# This program write a menu-driven program for De Anza College Food Court.
# Final_part1_printFile.py

import time
import datetime

from Final_part1_order import Order

class saveFile(Order):
    def __init__(self):
        super().__init__()

    def saveToFile(self):
        '''
        Use time and date at ordered to get the output file name
        And save the bill into the file
        '''
        timeStamp = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
        orderTimeStamp = orderTimeStamp + '.txt'

        orderTime = datetime.datetime.fromtimestamp(timeStamp).strftime('%m/%d/%Y %H:%M:%S')
        try:
            with open(orderTimeStamp, 'w') as fileToSaveTheBill:
                fileToSaveTheBill.write(f'{"BILL":>30}'+ "\n")
                fileToSaveTheBill.write(f'{orderTime}' + "\n")
                fileToSaveTheBill.write(f'{"Items":>10}' + f'{"Quantity":>20}' + f'{"Price":>11}' + f'{"Total":>15}' + "\n")
                for key in self._orderDict:
                    fileToSaveTheBill.write("%-24s %-10d $%-12.2f $%-12.2f" %
                                            (key, self._orderDict[key], self._priceDict[key],
                                             (self._orderDict[key] * self._priceDict[key])) + "\n")
                fileToSaveTheBill.write("-" * 60 + "\n")
                fileToSaveTheBill.write(f'{"Total Before Tax":<45}' + f'{"$":<1}' + f'{self._priceBtax :>7.2f}' + "\n")
                fileToSaveTheBill.write(f'{"Tax amount":<45}' + f'{"$":<1}' + f'{self._tax :>7.2f}' + "\n")
                fileToSaveTheBill.write("-" * 60 + "\n")
                fileToSaveTheBill.write(f'{"Total After Tax":<45}' + f'{"$":<1}' + f'{self._priceAtax :>7.2f}' "\n")
                fileToSaveTheBill.write("-" * 60 + "\n")
                fileToSaveTheBill.write(f'{"THANK YOU":>33}' + "\n" + f'{"HOPE TO SEE YOU AGAIN":>40}')
        except(IOError):
            print("Error! Cannot create the file!")
