library(C50)
library(gmodels)
person <- read.csv("person.csv")
person_train <- person[1:7,-5]
person_test <- person[8:10,-5]
person_train_labels=person[1:7,5]
person_test_labels=person[8:10,5]
person_model <- C5.0(person_train,as.factor(person_train_labels))
person_model
summary(person_model)
person_pred <- predict(person_model,person_test)
person_pred
CrossTable(person_test_labels,person_pred,prop.chisq=FALSE)