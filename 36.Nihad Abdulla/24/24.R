> library(e1071)
> cars = read.csv("cars.csv")
> cars
> cars_train = cars[,2:4]
> cars_train
> cars_test = data.frame(Color="red", Type="sports", Origin="domestic")
> cl = naiveBayes(cars_train,cars$Stolen.)
> pd = predict(cl , cars_test)
> pd