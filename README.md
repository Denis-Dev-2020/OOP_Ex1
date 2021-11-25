# Exercise 1 - Elevator Problem

- In this exercise we will try to figure out the best algorithm for 
  an elevators , which use smart panel calls the user will press
  the desired floor and the elevator system will figure our the way
  to distribute every user to its desired floor with the minimum time
  possible (total time and individual user time)
  
  
## Basic Idea - theoretical understanding :

  So after testing different ways to redirect elevators to their destination
  I found out that distributing all the elevators equaly along the building
  will not be efficiant due to over using of certain floors such as the 0 floor
  after testing different call found out that more then 50% percent of calls
  start at ground (0) floor so I begin my entire elevator system at 0
  then each call go to different elevator equaly distributed
  that way we save time on the return also 
  
## Implementation :
  
  I created an object for the building and after importing json and csv files
  I took the elevators data from the dictionary and converted it to a list
  that way it would be easy to navigate with different indexs
  
  then for calls I converted them into a stack list and when I took directions for
  the elevators I converted it to a set so double statements get erased and everything 
  will be sorted by order , that way the elevator can easly understand operations


   ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/Scheme.png?raw=true)



## Comfortability :
  
  I wrote code description on every stage so everybody can understand what's going on
  and also replaced the standard (print) representation of the objects to more UI friendly
  and one can easly understand every stage of the program

  ### print(Building):
  
 ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/Building%20header.png?raw=true)
  
  ### after every building will be (if uncomment) print(elevator[i]) by order:
  
 ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/Elevator%20Repr.png?raw=true)
 
  ### then for every elevator will be their specific calls to answer:
  
  ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/CallRepr.png?raw=true)
 
 
## Testing :

  - I tested the import methods that imports json and csv files
  - on json and csv files tested the correct input types
  - on json and csv files tested the correct value (value>=0 , value can be negative etc..)

  ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/tests.png?raw=true)

## Executing :

Bash

run program and will output "out.csv" file , change only 2nd and 3rd argument
2nd should be building json file (can see example inside Ex1_Building folder)
3rd should be calls csv file (can see example inside Ex1_Calls folder)

*note that when executing program you should provide json and csv files without mentioning*
*the folder name before , thats because I already included that in the code so run it like this*

    python main.py B5.json Calls_a.csv

provided tests - my json and csv files are inside folders so please include that in the 5th argument

    java -jar libs/Ex1_checker_V1.2_obf.jar 333333333 Ex1_Buildings/B4.json out.csv out.log
    
    
## Output :

   will output "temp.csv" file that includes calls sorted by elevator number , then import this file sort it and 
   output "out.csv" file that is sorted by time like in the example on google docs
   
  ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/temp%20file.png?raw=true)
  
  
## Thats it thank you for reading , till the next project :)



  
  
