
import joblib
import pandas as pd

model = joblib.load("models/best_model.pkl")

data = pd.DataFrame([{
    "Store": 1,
    "DayOfWeek": 5,
    "Open": 1,
    "Promo": 1,
    "SchoolHoliday": 0,
    "CompetitionDistance": 1270,
    "CompetitionOpenSinceMonth": 9,
    "CompetitionOpenSinceYear": 2008,
    "Promo2": 1,
    "Promo2SinceWeek": 13,
    "Promo2SinceYear": 2010,
    "Year": 2015,
    "Month": 7,
    "Day": 31,
    "Week": 31,
    "Quarter": 3,
    "DayOfYear": 212,
    "IsWeekend": 0,
    "StateHoliday": "0",
    "StoreType": "c",
    "Assortment": "a",
    "PromoInterval": "Jan,Apr,Jul,Oct"
}])

prediction = model.predict(data)

print(prediction)