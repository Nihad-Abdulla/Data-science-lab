library(C50)
library(gmodels)
cricket <- read.csv("cricket.csv")
cricket_train <- cricket[1:10,-5]
cricket_test <- cricket[11:14,-5]
cricket_train_labels=cricket[1:10,5]
cricket_test_labels=cricket[11:14,5]
cricket_model <- C5.0(cricket_train,as.factor(cricket_train_labels))
cricket_model
summary(cricket_model)
cricket_pred <- predict(cricket_model,cricket_test)
cricket_pred
CrossTable(cricket_test_labels,cricket_pred,prop.chisq=FALSE)