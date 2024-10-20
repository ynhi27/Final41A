# Y Nhi Tran
# Final part 1
# This program write a menu-driven program for De Anza College Food Court.
# Final_part1_order.py

from Final_part1_occupation import *
import time
import datetime


class Order:
    '''
    This class takes the order from customer, calculates the bill, and prints it on the screen
    '''
    def __init__(self):
        '''
        This is the initialization method.
        '''
        self._option = None
        self._priceBtax = 0
        self._priceAtax = 0
        self._tax = 0
        self._priceDict = {"De Anza Burger": 5.25, "Bacon Cheese": 5.75,
                           "Mushroom Swiss": 5.95, "Western Burger": 5.95,
                           "Don Cali Burger": 5.95}
        self._orderDict = {"De Anza Burger": 0, "Bacon Cheese": 0,
                           "Mushroom Swiss": 0, "Western Burger": 0,
                           "Don Cali Burger": 0}

    def get_main_inputs(self):
        '''
        Display the main menu (CRUD menu)
        Choose the menu C - Create an order
                        R - Review the current bill - display the bill on the screen
                        U - Update the current order - update everything
                        D - Delete the order - every information would be deleted and the bill will be 0
                        E - Exit the program
        Get an option and check their validation
        '''
        print("WELCOME TO DE ANZA COLLEGE FOOD COURT"
              + "\n" + f'{"MAIN MENU":>18}' + "\n"
              + f'{"C - Create an order"}' + "\n"
              + f'{"R - Review the current bill"}' + "\n"
              + f'{"U - Update the current order"}' + "\n"
              + f'{"D - Delete the order"}' + "\n"
              + f'{"E - Exit the program"}')

        command1 = "\nPlease choose an option\n" \
                   "C-reate | R-eview | U-pdate | D-elete | E-xit: "

        flag = True
        while flag:
            str1 = input(command1)
            main_option = str1.strip()
            if main_option.upper() == 'C':
                self.delete_order()
                self.displayMenu()
                self.getInputs()
                self.calculate()
            elif main_option.upper() == 'R':
                self.printBill()
            elif main_option.upper() == 'U':
                self.update_order()
                print("UPDATED YOUR ORDER!")
            elif main_option.upper() == 'D':
                self.delete_order()
                print("DELETED YOUR ORDER!")
            elif main_option.upper() == 'E':
                flag = False
                break
            else:
                print("You have not entered the correct character option.\n"
                      "Please try again!")
                continue

    def displayMenu(self):
        '''
        Display the menu of De Anza College Food Court
        Choose the menu from 1 to 5, choose 6 to exit
        '''

        print(f'{"Burgers Menu":>22}')
        number = 1
        for key in self._priceDict:
            print("{a}. {b:22s}${c:3.2f}".format(a=number, b=key, c=self._priceDict[key]))
            number += 1
        self._option = len(self._orderDict)
        print(str(self._option + 1) + ". Exit Burgers Menu")

    def getInputs(self):
        '''
        Get the burger choices and the quantity from user
        Also check the inputs valid or not
        '''
        global option, qty

        command1 = "Enter an option: "
        command2 = "Enter quantity: "

        ask = True
        while ask:
            try:
                option = int(input(command1))
                if 0 < option < (self._option + 1):
                    check = True
                    while check:
                        try:
                            qty = int(input(command2))
                            if qty > 0:
                                if option == 1:
                                    self._orderDict["De Anza Burger"] = qty
                                elif option == 2:
                                    self._orderDict["Bacon Cheese"] = qty
                                elif option == 3:
                                    self._orderDict["Mushroom Swiss"] = qty
                                elif option == 4:
                                    self._orderDict["Western Burger"] = qty
                                elif option == 5:
                                    self._orderDict["Don Cali Burger"] = qty
                                check = False
                            else:
                                print("Error! Please enter a number bigger than zero!")
                        except ValueError:
                            print("Please enter a number!")
                elif option == (self._option + 1):
                    ask = False
                    break
                else:
                    print("You have not entered from 1 to " + str(self._option + 1) + ".\n"
                          "Please try again!")
                    continue
            except ValueError:
                print("Please enter a number.")

    def calculate(self):
        '''
        Calculate the total paid (before and after tax)
        Calculate tax with occupation option: Student - 0, Staff - 9% rate
        '''
        global tax_rate
        self._priceBtax = 0
        for key in self._orderDict:
            self._priceBtax += self._orderDict[key] * self._priceDict[key]
        if self._priceBtax == 0:
            if option == (self._option + 1):
                print("RETURNED THE MAIN MENU!")

        elif self._priceBtax != 0:
            command3 = "You are 1-Student or 2-Staff: "
            check = True
            while check:
                try:
                    job = int(input(command3))
                    if job == 1:
                        tax_rate = Student().tax
                        check = False
                    elif job == 2:
                        tax_rate = Staff().tax
                        check = False
                    else:
                        print("Error! Please enter [1] or [2]!")
                except ValueError:
                    print("Error! This is not a numeric option!")
            self._tax = round((self._priceBtax * tax_rate), 2)
            self._priceAtax = round((self._priceBtax + self._tax), 2)

    def printBill(self):
        '''
        Display the bill on the screen
        '''
        print(f'{"BILL":>30}')
        orderTime = datetime.datetime.fromtimestamp(time.time()).strftime('%m/%d/%Y %H:%M:%S')
        print(f'{orderTime}')
        print(f'{"Items":>10}' + f'{"Quantity":>20}' + f'{"Price":>11}' + f'{"Total":>15}')
        for key in self._orderDict:
            print("%-24s %-10d $%-12.2f $%-12.2f" %
                 (key, self._orderDict[key], self._priceDict[key], (self._orderDict[key] * self._priceDict[key])))
        print("-" * 60)
        print(f'{"Total Before Tax":<45}' + f'{"$":<1}' + f'{self._priceBtax :>7.2f}')
        print(f'{"Tax amount":<45}' + f'{"$":<1}' + f'{self._tax :>7.2f}')
        print("-" * 60)
        print(f'{"Total After Tax":<45}' + f'{"$":<1}' + f'{self._priceAtax :>7.2f}')
        print("-" * 60)

    def delete_order(self):
        '''
        Reset the order into 0
        '''
        self._orderDict = {"De Anza Burger": 0, "Bacon Cheese": 0, "Mushroom Swiss": 0, "Western Burger": 0,
                           "Don Cali Burger": 0}
        self._priceBtax = 0
        self._priceAtax = 0
        self._tax = 0

    def update_order(self):
        '''
        Update the quantity in the order
        '''
        self.displayMenu()
        print("Please enter for updating your order.")
        print("You order has:")
        for key in self._orderDict:
            if self._orderDict[key] != 0:
                print(f'{str(self._orderDict[key]):>10}' + " " + f'{key:<25}')
        for key in self._orderDict:
            if self._orderDict[key] != 0:
                flag = True
                while flag:
                    try:
                        new_qty = int(input("Enter the new quantity of " + key + ": "))
                        if new_qty >= 0:
                            self._orderDict[key] = new_qty
                            flag = False
                        else:
                            print("Error! Please enter a positive number!")
                    except ValueError:
                        print("Please enter a number!")
        self.calculate()

