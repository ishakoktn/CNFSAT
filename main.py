from random import  random, randrange
from string import ascii_letters
from math import *
import copy


class Gate():
    def __init__(self, lst):
        self.arr = lst
        if len(self.arr[0]) < 2:
            self.fill()

    def get_arr(self):
        return self.arr

    def set_arr(self, index1, index2, value):
        self.arr[index1][index2] = value

    def fill(self):
        for i in range(len(self.arr)):
            self.arr[i].append(randrange(2))

def cost(array):
    cst = 0
    gates = list()
    for _ in array:
        gates.append(_[0])
    for _ in EXPRESSION:
        for j in _:
            if "!" not in j and array[gates.index(j)][1] == 1:
                print(j, "  ", array[gates.index(j[0])][0])
                cst += 1
                break
            elif "!" in j and array[gates.index(j.replace("!",""))][1] == 0:
                print(j)
                cst += 1
                break
    print("SENDED ARRAY   ", array, "    cost : ", cst)
    return cst
    # Return result 0 of conjuctions {i.e: (a+b)(a+c)  a=b=0, c=1. return is 1}

#formula type is "(a+b)(c!+b)(a+z!+d)"
def separate(formula):
    arr = list()
    accepted_chars = list((ascii_letters + "+!()"))
    for _ in formula:
        if(_  not in accepted_chars):
            formula = formula.replace(_,  "")

    formula = formula.replace(" ", "").replace(")(", "|")
    formula = formula.replace("(", "").replace(")", "")


    for _ in formula.split("|"):
        arr.append(_.split("+"))

    return arr

def neighbor():
    rslt = Gate(copy.deepcopy(gate_list)).get_arr()
    return rslt  #Create new random solution

def acceptance_probablitiy(old_cost, new_cost, t):
    return  e**((new_cost - old_cost) /t)

#solution is list type of Gate.get_arr()
def simulated_annel(solution):
    old_cost = cost(solution)
    t = 1.0
    t_min = 0.001
    alpha = 0.8
    while t > t_min:
        i = 1
        while i <= 100:
            print("-----------------------------------------------------------------")
            new_solution = neighbor()
            new_cost = cost(new_solution)
            print("old solition : ", solution)
            print("new solition : ", new_solution)
            ap = acceptance_probablitiy(old_cost, new_cost, t)
            if ap > random():
                print("!!!!!!!!!!!!!!!!   ",ap)
                solution = new_solution
                old_cost = new_cost
            i += 1
            print("-----------------------------------------------------------------")
        t = t * alpha
    return  solution

#if __name__ == "__main__":
    # Edit formula  [['a', 'b'], ['c', 'b!'], ['a!', 'z', 'd']]
formula = input("""Enter formula like "(a+b)(c!+b)(a+z!+d)(b!+g)(f)(r!+x)" """)
EXPRESSION = separate(formula)
# find gates
gate_list = list()
count = 0
for i in formula:
    if ((i in ascii_letters) and  sum(x.count(i) for x in gate_list)==0):
        gate_list.append([])
        gate_list[count].append(i)
        count += 1

# creating array of gates and its values like [['a', 1], ['b', 1], ['c', 0], ['z', 1], ['d', 0]]
Array = Gate(copy.deepcopy(gate_list))
print(Array.get_arr())
print(gate_list)

result = simulated_annel(Array.get_arr())
print(result)