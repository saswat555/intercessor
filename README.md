# Intercessor
## _The Smart Warehouse Management system




Intercessor is a smart warehouse management tool that uses machine learning to reduce the wastage of perishable goods. The main goal is to make a system that can forecast the upcoming sales for a warehouse and then use the same to restock according to the predicted sales. So this is the main idea behind the project.

## Tech Stack and major libraries used

- MongoDb for managing and storing the csv files
- Flask web framework for webapp
- Tensorflow for using ARIMA model
- R programming for estimating the prediction variables
- Pandas and numpy for other miscellaneous

## To deploy the app, follow the steps

- Customize the data present in the CSV files as per your choice
- Adjust the variable of forecast using the R file.
- Change the variables for the particular commodity in the app.py file
- Change the mongodb credentials with your credentials in the app.py file
- To run the app, use flask run after installing the requirements
- Please raise an issue if you face any issue in running the app or forecasting

## The app is currently deployed on heroku server- https://intercessor555.herokuapp.com/



