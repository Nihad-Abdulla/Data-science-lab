> getwd()
[1] "C:/Users/admin/Desktop"
> getwd()
[1] "C:/Users/admin/Desktop/01.AFRA/29.Economy"
> economy <- read.csv("economy.csv")
> economy_train <- economy[1:20,]
> economy_test <- economy[21:24,]
> economy_model <- lm(Stock_Index_Price ~ Interest_Rate + Unemployment_Rate, data= economy_train)
> economy_model

Call:
lm(formula = Stock_Index_Price ~ Interest_Rate + Unemployment_Rate, 
    data = economy_train)

Coefficients:
      (Intercept)      Interest_Rate  Unemployment_Rate  
           1125.0              374.0             -139.5  

>  
> summary(economy_model)

Call:
lm(formula = Stock_Index_Price ~ Interest_Rate + Unemployment_Rate, 
    data = economy_train)

Residuals:
    Min      1Q  Median      3Q     Max 
-62.715 -30.973   1.983  31.008  73.176 

Coefficients:
                  Estimate Std. Error t value Pr(>|t|)    
(Intercept)        1125.05     623.19   1.805 0.088769 .  
Interest_Rate       374.02      75.56   4.950 0.000122 ***
Unemployment_Rate  -139.49      82.48  -1.691 0.109046    
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 44.2 on 17 degrees of freedom
Multiple R-squared:  0.9444,    Adjusted R-squared:  0.9379 
F-statistic: 144.5 on 2 and 17 DF,  p-value: 2.144e-11

> economy_pred <- predict(economy_model,economy_test)
> economy_pred
      21       22       23       24 
956.6129 914.7665 914.7665 928.7153 
> 
