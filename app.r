
library(ggplot2)
library(forecast)
library(tseries)
library(highcharter)
d=read.csv('beef.csv', header=TRUE, stringsAsFactors=FALSE)
attach(d)

# Plotting the Demand
GDP=ts(GDP,frequency=1)
plot(GDP,col="blue",lwd=2,main="Sales",xlab="Year",ylab="Date")

# ACF and PACF Plot
par(mfrow=c(1,2))
Acf(GDP,main="",col="red",lwd=2)
Pacf(GDP,main="",col="red",lwd=2)

# Stationarity Check
# Formal Tests
adf.test(GDP, alternative = "stationary")
kpss.test(GDP)

# First Difference
GDP_1=diff(GDP,1)

# ACF and PACF Plot of First Difference
par(mfrow=c(1,2))
Acf(GDP_1,main="",col="red",lwd=2)
Pacf(GDP_1,main="",col="red",lwd=2)

adf.test(GDP_1, alternative = "stationary")
kpss.test(GDP_1)


# Model Fitting
fit=auto.arima(GDP,seasonal=TRUE)

res=residuals(fit)
par(mfrow=c(1,2))
Acf(res,main="ACF",col="red",lwd=2)
Pacf(res,main="PACF",col="red",lwd=2)

Box.test(res,fitdf=2,lag=10)
Box.test(res,fitdf=2,lag=10,type="Lj")

par(mfrow=c(1,1))



library(shiny)
ui <- fluidPage(


    mainPanel(highchartOutput("hcontainer",height = "500px")))
server <- function(input,output) {
  output$hcontainer <- renderHighchart({
    par(mfrow=c(1,1))
    hchart(forecast(fit,w=1),lwd=2)
  })
  
  
  
  
  
}

shinyApp(ui = ui, server = server)