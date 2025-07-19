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


#Function creating random members of population of given size where it's gene is a number from -5.12 to 5,12 for RASTRIGIN FUNCTION
def Population(size):
    des_vector=random.randint(-512,512,size=(size))/100.0
    return des_vector

#Function creating random members of population of given size where it's gene is a number from -2.00 to 2.00 for SPHERE FUNCTION
#def Population(size):
#    des_vector=random.randint(-20000,20000,size=(size))/100.00
#    return des_vector


#Function creating random members of population of given size where its's gene is a number from -5.00 το 10.00 for ROSENBROCK FUNCTION
#def Population(size):
#    des_vector=random.uniform(-5.00,10.00,size=(size))
#    return des_vector

#the objective function

def Objective_function(x,y,z):
    #raistrigin function
    objective=30+x**2-10*cos(2*math.pi*x)+y**2-10*cos(2*math.pi*y)+z**2-10*cos(2*math.pi*z)

    #sphere function
    #objective=x**2+y**2+z**2

    #rosenbrock function
    #objective=100*((y-(x**2))**2)+((1-x)**2)+100*((z-(y**2))**2)+((1-y)**2)
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

#this function calculates the sum of every list given as parameter.It is used in the calculation of the convergence criterion.
def sum_list(mylist):
    sum=0
    for x in mylist:
        sum=sum+x
    return sum    
#this function calculates the convergence criterion
def check_convergence(mylist,limit):
    flag=False
    n=len(mylist)
    mean=sum_list(mylist)/n
    diff=[i-mean for i in mylist]
    diff_2=[x**2 for x in diff]
    my_sum=sum_list(diff_2)
    variance=my_sum/n
    sd=math.sqrt(variance)
    if sd<=limit:
        flag=True
    return flag    

#this function is doing the Crossover Operation.At first there is a list(passing list)  with all the members that pass to the 
#next generation from the beggining.The reproduction list in which there are the elements that will go for crossover and an 
#offspring list which will be the list that will be returned with the new generation after crossover.There is a default 
#crossover probability and for every member there is a random number from 0 to 1 .If the random number<=prob of crossover then 
#the member goes for reproduction else it goes immediately to the next generation.if the length of the reproduction list is 1 then the
#next generation is the same because a member can not crossover on its own.If the length in reproduction list is odd then pass the last member
#to the next generation because it cant crossover and remove it from the reproduction list.
#then for crossover I use this algorithm:a. Select 2 parents: G1, G2
#b. generate uniformly distributed random number gamma from [-alpha, 1 + alpha], where alpha = 0.5
#c. generate an offspring as follows: G = gamma * G1 + (1 - gamma) * G2 twice for every two elements list in the reproduction list
# and the new members are added to offspring list.Finally the returned list is offspring list+passinglist. 
def Crossover(mylist,pc):
    passing_list=[]
    crossover_list=[]
    offspring_list=[]
    for x in mylist:
        r=random.uniform(0.0,1.0)
        if r<=pc:
            crossover_list.append(x)
        else:
            passing_list.append(x)       
    if len(crossover_list)==1:
        offspring_list=mylist.copy()
        return offspring_list        
    if len(crossover_list)%2==1:
        offspring_list.append(crossover_list[-1])
        crossover_list.remove(crossover_list[-1])
    r=random.uniform(0.0,1.0)
    for i in range(2):
        for x in range(0,len(crossover_list),2):
            new_list=[]
            for y in range(3):
                gamma=random.uniform(-0.5,1.5)
                new_list.append(round(gamma*crossover_list[x][y]+(1-gamma)*crossover_list[x+1][y],2))
            #print(new_list)
            offspring_list.append(new_list)
    offspring_list=offspring_list+passing_list
    return offspring_list                         

#this function is doing Mutation through swapping.Given a default possibillity of Mutation each member
#has its own random possibility to mutate,so if a member's gene has possibility to mutate<= from the default
#mutation possibility then it swaps the gene with next one if there is one else if the gene is the last then swapp the gene with its previous

def Mutation(mylist,possibility_of_mutation):
    for x in range(len(mylist)):
        for y in range(len(mylist[x])):
            r=random.uniform(0.0,1.0)
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
     
probability_of_crossover=0.9
probability_of_mutation=0.1
size=3
list1=[]
#initialize a population of 300 members
for x in range(300):
    list1.append(list(Population(size)))
firstpop=list1.copy()    
counter=0
print("POPULATION1 IS:")    
for x in list1:
    print(f"x value of first population is:{x[0]}")
    print(f"y value of first population is:{x[1]}")
    print(f"z value of population is:{x[1]}")
    print("\n")
    counter=counter+1
    if counter==5:
        break
i=0
while i<400:
    summ=Calc_sum(list1)
    
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    list6=[]
    list2=Calc_prob(list1,summ)
    ex1=Reproduction()
    list3=ex1.Calc_Cumulative_prob(list2)
    #for every member creates a random variable from 0 to 1 and if this number is <=
    # from the cumulative prob then it goes to the mating pool 
    for x in range(300):
        position=0
        r=random.uniform(0.0,1.0)
        for y in list3:
            if r<=y:
                list4.append(list1[position])
                break
            position=position+1     
    list6=Crossover(list4,probability_of_crossover)

    mutation_poss=random.uniform(0.0,1.0)
    list5=Mutation(list6,probability_of_mutation)
    sum=0
    #this loop calculates the average fitness function of every generation
    for x in list5:
        ex=Reproduction()
        sum=sum+ex.Fitness_function(x[0],x[1],x[2])/len(list5)
    print(f"Average fitness of {i} iteration is:{sum}")
    #in this point mylist1 will contain all the x elements,mylist2 will contain all the y elements and mylist3 will contain all the z elements of the 300
    # members of the population of every generation.Those lists will be given as parameters in the check_corvegence function with the limit 0.01
    # When all three functions return true then the loop breaks before the iterations reach the default 400 and the algorithm finishes.Then the 
    # last population is printed.    
    mylist1=[]
    mylist2=[]
    mylist3=[]
    for x in list5:
        mylist1.append(x[0])
        mylist2.append(x[1])
        mylist3.append(x[2])
    convergence_limit=0.0005    
    if check_convergence(mylist1,convergence_limit) and check_convergence(mylist2,convergence_limit) and check_convergence(mylist3,convergence_limit):   
        break
    i=i+1
    list1.clear()
    list1=list5.copy()
counter=0    
print("LAST POPULATION1 IS:")    
    
for x in list5:
    print(f"x value of lastpopulation is:{x[0]}")
    print(f"y value of last population is:{x[1]}")
    print(f"z value of last population is is:{x[1]}")
    print("\n")
    counter=counter+1
    if counter==5:
        break
print(f"over in {i} iteration") 