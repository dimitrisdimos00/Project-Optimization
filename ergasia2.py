import numpy as np
from numpy import cos, random
import math


class Reproduction:
    def Fitness_function(self,x,y,z):
        self.k=1/(1+Objective_function(x,y,z))
        return self.k
    def Calc_probability(self,x,sum):
        self.p=x/sum
        return self.p   
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


#Function creating population
def Population(size):
    des_vector=random.randint(0,999,size=(size))/100.00
    return des_vector

#the objective function

def Objective_function(x,y,z):
    #objective=30+x**2-10*cos(2*math.pi*x)+y**2-10*cos(2*math.pi*y)+z**2-10*cos(2*math.pi*z)
    objective=x**2+y**2+z**2
    return objective

def Calc_sum(mylist):
    sum=0
    for x in mylist:
        ex=Reproduction()
        sum=sum+ex.Fitness_function(x[0],x[1],x[2])
    return sum

def Calc_prob(mylist,summ):
    list2=[]
    for x in mylist:
        ex=Reproduction()
        y=ex.Calc_probability(ex.Fitness_function(x[0],x[1],x[2]),summ)
        list2.append(y)
    return list2    

def percent_50_choice(reproduction_list,offspring_least):
    if len(reproduction_list)>1:
        for x in range(0,len(reproduction_list)-1,2):
            new_row=[]
            for y in range(3):
                r1=random.uniform(0.0,1.0)
                r2=random.uniform(0.0,1.0)
                if r1>r2:
                    k=reproduction_list[x][y]
                else:
                    k=reproduction_list[x+1][y]
                new_row.append(k)
            offspring_least.append(new_row)
    return offspring_least


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
    #print(f"reproduction list:{reproduction_list}")
    #print(f"passing:{passing_list}")        
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

#def Mutation(mylist,possibility_of_mutation):
    #for x in range(len(mylist)): 
        #r=random.uniform(0.0,1.0)
        #for y in range(3):
            #if r<=possibility_of_mutation:
                #new_random=round(random.uniform(0.0,9.9),2)
                #mylist[x][y]=new_random
    #return mylist            


pop_size=3
list1=[]

for x in range(300):
    list1.append(list(Population(pop_size)))

# print(f"basic population:{list1}")
i=0
while i<=100:
    summ=Calc_sum(list1)
    
    list2=[]
    list2=Calc_prob(list1,summ)
    # print(f"calc probability:{list2}")
    list3=[]
    ex1=Reproduction()
    list3=ex1.Calc_Cumulative_prob(list2)

    #print(f"cumlative einai:{list3}")

    list4=[]
    for x in range(300):
        position=0
        r=random.uniform(0.0,1.0)
        for y in list3:
            if r<=y:
                list4.append(list1[position])
                break
            position=position+1     

    #print(f" this is:{list4}")
    #print("\n")
    #new_list4=list4[:]
    list6=[]
    list6=Crossover(list4,0.80)

    #print(f"crossover {list6}")
    #print("\n")
    list5=[]
    mutation_poss=random.uniform(0.0,1.0)
    list5=Mutation(list6,0.20)
    sum=0
    for x in list5:
        #print(x)
        ex=Reproduction()
        sum=sum+ex.Fitness_function(x[0],x[1],x[2])/len(list5)
    #print("\n")
    
    print(f"average fitness function of {i} iteration is {sum}")    
    #print(f"mutation:{list5}")
    #print("\n")
    i=i+1
    #print(list5)
    
    list1.clear()
    #print(list1)
    list1=list5.copy()
    

