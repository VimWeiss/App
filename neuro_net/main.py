import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

train_in = np.array([[0,0,1],
                  [1,1,1],
                  [1,0,1],
                  [0,1,1]])

train_out = np.array([[0,1,1,0]]).T

np.random.seed(1)
weights = 2 * np.random.random((3,1)) - 1
print("Случайные инициализирующие веса:")
print(weights)

#Обратное распространение
for i in range(20000):
    in_lay = train_in
    outputs = sigmoid(np.dot(in_lay, weights))
    err = train_out - outputs
    adjustments = np.dot (in_lay.T, err * (outputs * (1 - outputs)))
    weights += adjustments

print("Веса после обучения:")
print(weights)

print("Результат после обучения:")
print(outputs)

#тест
new_in = np.array([1,1,0])
output = sigmoid(np.dot(new_in, weights))
print("Новый тест:")
print(output)