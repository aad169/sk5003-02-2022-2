import random 

print('Random number from 0 to 1 :', random.random()) 
print('Uniform Distribution between [1,10] :', random.uniform(1, 10)) 
print('Gaussian Distribution with mean = 0.5 and standard deviation = 1.5 :', random.gauss(0.5, 1.5)) 
print('Exponential Distribution with lambda = 0.95 :', random.expovariate(0.95)) 
print('Normal Distribution with mean = 1 and standard deviation = 3.8:', random.normalvariate(1, 3.8))
