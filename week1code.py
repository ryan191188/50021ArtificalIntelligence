import numpy as np
import matplotlib.pyplot as mpl
import math

def datagen(n):
  c=np.random.randint(1,3,size=(n))
  us=np.random.normal(loc=0,scale=1,size=(2,n))
  
  #######################
  # your code here
  xs, ys = []

  A = np.dot(np.array([[math.cos(math.pi/4),math.sin(math.pi/4)],[-math.sin(math.pi/4),math.cos(math.pi/4)]]), np.array([[3,0],[0,1]]))
  miu_1 = np.zeros((2,1))
  miu_2 = np.array([[2.5],[0]])
  for i in c:
    u = np.random.choice(us[i-1],(2,1))
    if i == 1:
      x = np.matmul(A,u) + miu_1
      y = np.random.choice([0,1],1,p=[0.3,0.7])
    else:
      x = np.matmul(A,u) + miu_2
      y = np.random.choice([0,1],1,p=[0.6,0.4])
    xs.append(x)
    ys.append(y) 

  #######################
  
  return xs,ys,c
  
def plot1(n):
  xs,ys,c=datagen(n)

  #######################
  # your code here
  color= ['red' if l == 1 else 'green' for l in c]
  mpl.scatter(xs, ys, color=color)
  mpl.show()

  #######################
  

  
def knn(traindata, trainlabels,x):
  
  dists=np.ones(traindata.shape[1])
  minind=0

  #######################
  # your code here
  

  #######################  

      
  return trainlabels[minind]

def cls(n):
  xs,ys,c=datagen(n)
  
  xt,yt,ct=datagen(n)
  

  err0=0
  #######################
  # KNN prediction of training data
  # your code here
  

  #######################
  print ('err0',err0)

  err1=0
  #######################
  # KNN prediction of testing data
  # your code here
  

  #######################
  print ('err1',err1)
  
  err2=0
  #######################
  # other prediction of testing data
  # your code here
  

  #######################
  print ('err2',err2)  

  
if __name__=='__main__':
  #plot1(1000)
  cls(1000)

