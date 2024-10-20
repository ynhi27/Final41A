# Y Nhi Tran
# Final part 1
# This program write a menu-driven program for De Anza College Food Court.
# Final_part1_main.py

from Final_part1_printFile import saveFile

if __name__ == "__main__":

    flag = True

    while flag:
        order = saveFile()
        order.get_main_inputs()
        order.saveToFile()

        userInputToContinue = input("Continue another order for another member/customer (Any keys= Yes, n= No)? ")

        if userInputToContinue.lower() == 'n':
            print(f'{"THANK YOU":>31}' + "\n" + f'{"HOPE TO SEE YOU AGAIN":>38}')
            print("The system is shutting down!")
            flag = False

"""
The outputs below exported 3 output-files.
So I submitted all of them on Canvas.
--------------------------------------------
OUTPUT 1
WELCOME TO DE ANZA COLLEGE FOOD COURT
         MAIN MENU
C - Create an order
R - Review the current bill
U - Update the current order
D - Delete the order
E - Exit the program

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: a
You have not entered the correct character option.
Please try again!

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: -2
You have not entered the correct character option.
Please try again!

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit:   c
          Burgers Menu
1. De Anza Burger        $5.25
2. Bacon Cheese          $5.75
3. Mushroom Swiss        $5.95
4. Western Burger        $5.95
5. Don Cali Burger       $5.95
6. Exit Burgers Menu
Enter an option: a
Please enter a number.
Enter an option: -9
You have not entered from 1 to 6.
Please try again!
Enter an option: 1
Enter quantity: f
Please enter a number!
Enter quantity: 8
Enter an option: 2
Enter quantity: -9
Error! Please enter a number bigger than zero!
Enter quantity: 
Please enter a number!
Enter quantity: 3
Enter an option: 6
You are 1-Student or 2-Staff: v
Error! This is not a numeric option!
You are 1-Student or 2-Staff: -7
Error! Please enter [1] or [2]!
You are 1-Student or 2-Staff: 
Error! This is not a numeric option!
You are 1-Student or 2-Staff: 3
Error! Please enter [1] or [2]!
You are 1-Student or 2-Staff: 2

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: r
                          BILL
12/15/2022 20:38:37
     Items            Quantity      Price          Total
De Anza Burger           8          $5.25         $42.00       
Bacon Cheese             3          $5.75         $17.25       
Mushroom Swiss           0          $5.95         $0.00        
Western Burger           0          $5.95         $0.00        
Don Cali Burger          0          $5.95         $0.00        
------------------------------------------------------------
Total Before Tax                             $  59.25
Tax amount                                   $   5.33
------------------------------------------------------------
Total After Tax                              $  64.58
------------------------------------------------------------

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: u
          Burgers Menu
1. De Anza Burger        $5.25
2. Bacon Cheese          $5.75
3. Mushroom Swiss        $5.95
4. Western Burger        $5.95
5. Don Cali Burger       $5.95
6. Exit Burgers Menu
Please enter for updating your order.
You order has:
         8 De Anza Burger           
         3 Bacon Cheese             
Enter the new quantity of De Anza Burger: a
Please enter a number!
Enter the new quantity of De Anza Burger: -9
Error! Please enter a positive number!
Enter the new quantity of De Anza Burger: 5
Enter the new quantity of Bacon Cheese: 1
You are 1-Student or 2-Staff: 1
UPDATED YOUR ORDER!

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: r
                          BILL
12/15/2022 20:38:55
     Items            Quantity      Price          Total
De Anza Burger           5          $5.25         $26.25       
Bacon Cheese             1          $5.75         $5.75        
Mushroom Swiss           0          $5.95         $0.00        
Western Burger           0          $5.95         $0.00        
Don Cali Burger          0          $5.95         $0.00        
------------------------------------------------------------
Total Before Tax                             $  32.00
Tax amount                                   $   0.00
------------------------------------------------------------
Total After Tax                              $  32.00
------------------------------------------------------------

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: e
Continue another order for another member/customer (Any keys= Yes, n= No)? n
                      THANK YOU
                 HOPE TO SEE YOU AGAIN
The system is shutting down!

Process finished with exit code 0

--------------------------------------------
OUTPUT 2
WELCOME TO DE ANZA COLLEGE FOOD COURT
         MAIN MENU
C - Create an order
R - Review the current bill
U - Update the current order
D - Delete the order
E - Exit the program

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: c
          Burgers Menu
1. De Anza Burger        $5.25
2. Bacon Cheese          $5.75
3. Mushroom Swiss        $5.95
4. Western Burger        $5.95
5. Don Cali Burger       $5.95
6. Exit Burgers Menu
Enter an option: 6
RETURNED THE MAIN MENU!

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit:   c
          Burgers Menu
1. De Anza Burger        $5.25
2. Bacon Cheese          $5.75
3. Mushroom Swiss        $5.95
4. Western Burger        $5.95
5. Don Cali Burger       $5.95
6. Exit Burgers Menu
Enter an option: 1
Enter quantity: 10
Enter an option: 2
Enter quantity: 20
Enter an option: 6
You are 1-Student or 2-Staff: 1

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: u
          Burgers Menu
1. De Anza Burger        $5.25
2. Bacon Cheese          $5.75
3. Mushroom Swiss        $5.95
4. Western Burger        $5.95
5. Don Cali Burger       $5.95
6. Exit Burgers Menu
Please enter for updating your order.
You order has:
        10 De Anza Burger           
Enter the new quantity of De Anza Burger: 1
        20 Bacon Cheese             
Enter the new quantity of Bacon Cheese: 4
You are 1-Student or 2-Staff: 2
UPDATED YOUR ORDER!

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: r
                          BILL
12/14/2022 19:31:02
     Items            Quantity      Price          Total
De Anza Burger           1          $5.25         $5.25        
Bacon Cheese             4          $5.75         $23.00       
Mushroom Swiss           0          $5.95         $0.00        
Western Burger           0          $5.95         $0.00        
Don Cali Burger          0          $5.95         $0.00        
------------------------------------------------------------
Total Before Tax                             $  28.25
Tax amount                                   $   2.54
------------------------------------------------------------
Total After Tax                              $  30.79
------------------------------------------------------------

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit:   d
DELETED YOUR ORDER!

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: r
                          BILL
12/14/2022 19:31:14
     Items            Quantity      Price          Total
De Anza Burger           0          $5.25         $0.00        
Bacon Cheese             0          $5.75         $0.00        
Mushroom Swiss           0          $5.95         $0.00        
Western Burger           0          $5.95         $0.00        
Don Cali Burger          0          $5.95         $0.00        
------------------------------------------------------------
Total Before Tax                             $   0.00
Tax amount                                   $   0.00
------------------------------------------------------------
Total After Tax                              $   0.00
------------------------------------------------------------

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: e
Continue another order for another member/customer (Any keys= Yes, n= No)? t
WELCOME TO DE ANZA COLLEGE FOOD COURT
         MAIN MENU
C - Create an order
R - Review the current bill
U - Update the current order
D - Delete the order
E - Exit the program

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: c
          Burgers Menu
1. De Anza Burger        $5.25
2. Bacon Cheese          $5.75
3. Mushroom Swiss        $5.95
4. Western Burger        $5.95
5. Don Cali Burger       $5.95
6. Exit Burgers Menu
Enter an option: 12
You have not entered from 1 to 6.
Please try again!
Enter an option: 1
Enter quantity: 12
Enter an option: 5
Enter quantity: 2
Enter an option: 6
You are 1-Student or 2-Staff: 2

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: r
                          BILL
12/14/2022 19:31:33
     Items            Quantity      Price          Total
De Anza Burger           12         $5.25         $63.00       
Bacon Cheese             0          $5.75         $0.00        
Mushroom Swiss           0          $5.95         $0.00        
Western Burger           0          $5.95         $0.00        
Don Cali Burger          2          $5.95         $11.90       
------------------------------------------------------------
Total Before Tax                             $  74.90
Tax amount                                   $   6.74
------------------------------------------------------------
Total After Tax                              $  81.64
------------------------------------------------------------

Please choose an option
C-reate | R-eview | U-pdate | D-elete | E-xit: e
Continue another order for another member/customer (Any keys= Yes, n= No)? n
                      THANK YOU
                 HOPE TO SEE YOU AGAIN
The system is shutting down!

Process finished with exit code 0

"""