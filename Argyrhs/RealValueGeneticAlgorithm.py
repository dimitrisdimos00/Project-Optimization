import numpy as np
from numpy import cos, random
import math


class Reproduction:
    def Fitness_function(self,x,y,z):
        self.k=1/(1+Objective_function(x,y,z))
        return self.k
    #this function calculates the calculative probability    
    def Calc_probability(self,x,sum):
        self.p=x/sum
        return self.p
    #this function calculates the cumulative probability       
    def Calc_Cumulative_prob(self,mylist):
        self.newlist=[]
        self.position=1
        for x in range(len(mylist)):
            self.cumul=0
            for y in range(self.position):
                self.cumul=self.cumul+mylist[y]
            self.newlist.append(self.cumul)    
            self.position=self.position+1  
        return self.newlist     


#Function creating random members of population of given size where it's gene is a number from 0.0 to 9.9  
def Population(size):
    des_vector=random.randint(0,999,size=(size))/100.00
    return des_vector

#the objective function

def Objective_function(x,y,z):
    #objective=30+x**2-10*cos(2*math.pi*x)+y**2-10*cos(2*math.pi*y)+z**2-10*cos(2*math.pi*z)
    objective=x**2+y**2+z**2
    return objective

#this function calculates the sum of fitness function of every member of the population
def Calc_sum(mylist):
    sum=0
    for x in mylist:
        ex=Reproduction()
        sum=sum+ex.Fitness_function(x[0],x[1],x[2])
    return sum

#this function calculates the calculative probability of every member from the type with the type (fitness(i)/sum of all fitness(i))
def Calc_prob(mylist,summ):
    list2=[]
    for x in mylist:
        ex=Reproduction()
        y=ex.Calc_probability(ex.Fitness_function(x[0],x[1],x[2]),summ)
        list2.append(y)
    return list2    


def Crossover(mylist,pc):
    passing_list=[]
    reproduction_list=[]
    offspring_list=[]
    for x in mylist:
        r=random.uniform(0.0,1.0)
        if r<=pc:
            reproduction_list.append(x)
        else:
            passing_list.append(x)       
    if len(reproduction_list)==1:
        offspring_list=mylist.copy()
        return offspring_list        
    if len(reproduction_list)%2==1:
        offspring_list.append(reproduction_list[-1])
        reproduction_list.remove(reproduction_list[-1])
    r=random.uniform(0.0,1.0)
    for i in range(2):
        for x in range(0,len(reproduction_list),2):
            new_list=[]
            for y in range(3):
                gamma=random.uniform(-0.5,1.5)
                new_list.append(round(gamma*reproduction_list[x][y]+(1-gamma)*reproduction_list[x+1][y],2))
            #print(new_list)
            offspring_list.append(new_list)
    offspring_list=offspring_list+passing_list
    return offspring_list                         

#this function is doing Mutation through swapping.Given a default possibillity of Mutation each member
#has its own random possibility to mutate,so if a member's gene has possibility to mutate<= from the default
#mutation possibility then it swaps the gene with next one if there is one else if the gene is the last then swapp the gene with its previous

def Mutation(mylist,possibility_of_mutation):
    for x in range(len(mylist)):
        r=random.uniform(0.0,1.0)
        for y in range(len(mylist[x])):
            if r<=possibility_of_mutation and y!=0:
                temp=mylist[x][y]
                mylist[x][y]=mylist[x][y-1]
                mylist[x][y-1]=temp
                break   
            if r<=possibility_of_mutation and y==0: 
                temp=mylist[x][y]
                mylist[x][y]=mylist[x][y+1]
                mylist[x][y+1]=temp
                break
    return mylist

pop_size=3
list1=[]
for x in range(300):
    list1.append(list(Population(pop_size)))

i=0
while i<=100:
    summ=Calc_sum(list1)
    
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list2=Calc_prob(list1,summ)
    ex1=Reproduction()
    list3=ex1.Calc_Cumulative_prob(list2)
    for x in range(300):
        position=0
        r=random.uniform(0.0,1.0)
        for y in list3:
            if r<=y:
                list4.append(list1[position])
                break
            position=position+1     
    list6=Crossover(list4,0.80)

    mutation_poss=random.uniform(0.0,1.0)
    list5=Mutation(list6,0.20)
    sum=0
    for x in list5:
        ex=Reproduction()
        sum=sum+ex.Fitness_function(x[0],x[1],x[2])/len(list5)
    
    
    print(f"average fitness function of {i} iteration is {sum}")    
    i=i+1
    list1.clear()
    list1=list5.copy()
    

