# Collatz Conjecture

##### The project is aimed at verifying and visualizing the outputs of the Collatz conjecture.

In the main file, there is a class ```storage_dict``` which is a class of dictionaries that stores the linked list nodes as the values and the values of those nodes as the keys. The values are ```int```.

Furthermore, there is a class decorator ```dec_header``` which in conjuction with the ```storage_dict``` class (and the ```dict``` object) ensure that the same value isn't assigned to multiple nodes.

##### Note: Neither the aforementioned class nor the decorator are needed (or even used) in the project. The code has been modified and they have been made reduntant.


#### The main classes in the project

- ##### ```Collatz```
- ##### ```_node```
- ##### ```List``` 

### ```Collatz``` class
This is the function class that initializes the linear function as ```ax+b``` and does the computation on the inoutted values through the ```cal``` method

| ```Collatz``` methods | Description | Arguments | Output |
| ------------------- | ----------- | --------- | ------ |
| ```__init__``` | Initializes the linear function | ```self```, ```coeff:int```, ```const:int``` | ```None``` |
| ```cal``` | If inp odd, return the output of ```ax + b``` but if even, devide by 2 | ```self```, ```inp:int``` | ```int``` |

### ```_node``` class

The class just initializes the nodes for the linked list ```List``` class. The only agument is ```number:int```. This is where the ```dec_header``` decorator couldve been used to prevent the creation of multiple nodes carrying the same value.

### ```List``` class

Linked list that stores a list of integers. The class is used to store the original input value of the linear function and to subsequently store the coutputes of the function when the input and later on the outputes are plugged into the function recursively.

| ```List``` methods | Description | Arguments | Output |
| ------------------- | ----------- | --------- | ------ |
| ```__init__``` | Initializes the list | ```self```, ```num:int``` | ```None``` |
| ```add_num``` | Adds a number to the List | ```self```, ```input:int``` | ```None``` |
| ```add_node``` | Adds a node to the List | ```self```, ```inp_node:_node``` | ```None``` |
| ```isin``` | Checks if the element is in the list | ```self```, ```inp:int``` | ```bool``` |
| ```_contains``` | Returns a list of elements contained in the linked list | ```self``` | ```list[int]``` |
| ```__str__``` | prints the  linked list where the values are separated with "->" | ```self``` | ```str``` |

##### Note: No default values for any of the above methods.

### ```pathbuilder``` function

This is the function to be used for verifying the result.

It builds the path from the first number up untill presumable second last (before 1) and if one of these numbers starts with a number that is already present in some other sequence (path) it removes it from the list to avoid repetitions.

It requires an ```int``` input of ```itr``` argument which specifies up untill what number the Collatz conjecture should be verified starting from 1. And also an inout of a ```Collatz``` obeject (the linear function) as ```f```.

It returns a ```list``` of linked lists ```List``` that each contain the sequence of the outputs of the Collatz function (and the first input as the first element) 

#### Example of the use of the ```pathfinder``` functon

```
v = pathbuilder(7, Collatz(3, 1))
for linkedlist in v:
    print(linkedlist)

>>> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
>>> 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
>>> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
```

### ```pathbuilder_test``` function

Tests that all the values up until the ```itr``` parameter are present in at least one of the sequences (linked lists).

Returns a ```bool``` -- if ```pathfinder``` function's output satisfies the condition in the previous oararaph then this function returns ```True```, if not then ```False```.