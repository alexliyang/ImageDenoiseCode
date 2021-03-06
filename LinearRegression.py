import numpy as np
np.random.seed(1337)
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

X = np.linspace(-1,1,200)
np.random.shuffle(X)
Y = 0.5*X+2+np.random.normal(0,0.05,(200,))
plt.scatter(X,Y)
plt.show()

X_train,Y_train = X[:160],Y[:160]
X_test,Y_test = X[160:],Y[160:]

model = Sequential()
model.add(Dense(input_dim=1,units=1))
model.compile(loss='mse',optimizer='sgd')
print("training.........................")
for step in range(1002):
    cost = model.train_on_batch(X_train,Y_train)
    if step%50==0:
        print ("%d trainings,the cost: %f" %(step,cost))
print("\n testing.......................")
cost = model.evaluate(X_test,Y_test,batch_size = 600)
print("the cost: ",cost)
W,b = model.layers[0].get_weights()
print("weights = ",W,"\n biases = ",b)

#绘制训练结果 
Y_pred = model.predict(X_test)
plt.scatter(X_test,Y_test)
plt.plot(X_test,Y_pred)
plt.show()
