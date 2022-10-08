from flask import Flask,request,render_template
from flask_cors import cross_origin
import pandas as pd
import sklearn
import pickle

app=Flask(__name__)
saved_model=pickle.load(open("flight_fare_pred.pkl","rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict",methods=["GET","POST"])    
@cross_origin()
def flight_fare_prediction():
    if request.method=='POST':

        #Date of Journey
        departure_date=request.form["Departure_Time"]
        journey_Date=int(pd.to_datetime(departure_date,format="%Y-%m-%dT%H:%M").day)
        journey_Month=int(pd.to_datetime(departure_date,format="%Y-%m-%dT%H:%M").month)

        #Departure
        Dep_hour=int(pd.to_datetime(departure_date,format="%Y-%m-%dT%H:%M").hour)
        Dep_min=int(pd.to_datetime(departure_date,format="%Y-%m-%dT%H:%M").minute)

        #Arrival
        date_of_arrival=request.form['Arrival Time']
        Arrival_hour=int(pd.to_datetime(date_of_arrival, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min=int(pd.to_datetime(date_of_arrival, format="%Y-%m-%dT%H:%M").minute)

        #Duration
        Duration_hours= abs(Arrival_hour - Dep_hour)
        Duration_mins=abs(Arrival_min - Dep_min)

        #Total Stops
        Total_Stops=int(request.form['stops'])

        #Airlines
        airline_name=request.form['airline'] 
        if airline_name=='Jet Airways':
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        elif airline_name == 'IndiGo':
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline_name == 'Air India':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline_name == 'Multiple carriers':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline_name == 'SpiceJet':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline_name == 'Vistara':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline_name == 'GoAir':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline_name == 'Multiple carriers Premium economy':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline_name == 'Jet Airways Business':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline_name == 'Vistara Premium economy':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0

        elif airline_name == 'Trujet':
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        source=request.form["source"]
        if source == 'Delhi':
            Delhi = 1
            Kolkata = 0
            Mumbai = 0
            Chennai = 0

        elif source == 'Kolkata':
            Delhi = 0
            Kolkata = 1
            Mumbai = 0
            Chennai = 0

        elif source == 'Mumbai':
            Delhi = 0
            Kolkata = 0
            Mumbai = 1
            Chennai = 0

        elif source == 'Chennai':
            Delhi = 0
            Kolkata = 0
            Mumbai = 0
            Chennai = 1

        else:
            Delhi = 0
            Kolkata = 0
            Mumbai = 0
            Chennai = 0


        destination = request.form["Destination"] 
        if destination == 'Cochin':
            Destination_Cochin = 1
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif destination == 'Delhi':
            Destination_Cochin = 0
            Destination_Delhi = 1
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif destination == 'New_Delhi':
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0

        elif destination == 'Hyderabad':
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0

        elif destination == 'Kolkata':
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1

        else:
            Destination_Cochin = 0
            Destination_Delhi = 0
            Destination_New_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0


        prediction = saved_model.predict([[
            Total_Stops,
            journey_Date,
            journey_Month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            Duration_hours,
            Duration_mins,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            Chennai,
            Delhi,
            Kolkata,
            Mumbai,
            Destination_Cochin,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_New_Delhi
        ]])    



        output=round(prediction[0],2)
        return render_template('home.html',prediction_text=f"Your Predicted Flight Fare is Rs.{output}")

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)