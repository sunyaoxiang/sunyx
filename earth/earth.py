import numpy
from pyearth import Earth
from matplotlib import pyplot

# Create some fake data
numpy.random.seed(0)
m = 1000
n = 10
X = 80 * numpy.random.uniform(size=(m, n)) - 40
y = numpy.abs(X[:, 6] - 4.0) + 1 * numpy.random.normal(size=m)

# Fit an Earth model
model = Earth()
model.fit(X, y)

#Print the model
print(model.trace())
print(model.summary())

#Plot the model
y_hat = model.predict(X)
pyplot.figure()
pyplot.plot(X[:, 6], y, 'r.')
pyplot.plot(X[:, 6], y_hat, 'b.')
pyplot.xlabel('x_6')
pyplot.ylabel('y')
pyplot.title('Simple Earth Example')
pyplot.show()