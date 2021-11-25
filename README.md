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

<p align="center">
     ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/Scheme.png?raw=true)
</p>


## Comfortability :
  
  I wrote code description on every stage so everybody can understand what's going on
  and also replaced the standard (print) representation of the objects to more UI friendly
  and one can easly understand every stage of the program
  <p align="center">
  print(Building):
  
 ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/Building%20header.png?raw=true)
  
  
  after every building will be (if uncomment) print(elevator[i]) by order:
  
  
 ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/Elevator%20Repr.png?raw=true)
 
  then for every elevator will be their specific calls to answer:
  
  
  ![name-of-you-image](https://github.com/Denis-Dev-2020/OOP_Ex1/blob/main/ScreenShots/CallRepr.png?raw=true)
  </p>
## Testing :



  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
