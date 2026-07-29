from pydantic import BaseModel, ConfigDict


class SalesRequest(BaseModel):
    Store: int
    DayOfWeek: int
    Open: int
    Promo: int
    SchoolHoliday: int
    CompetitionDistance: float
    CompetitionOpenSinceMonth: int
    CompetitionOpenSinceYear: int
    Promo2: int
    Promo2SinceWeek: int
    Promo2SinceYear: int
    Year: int
    Month: int
    Day: int
    Week: int
    Quarter: int
    DayOfYear: int
    IsWeekend: int

    StateHoliday: str
    StoreType: str
    Assortment: str
    PromoInterval: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "Store": 1,
                "DayOfWeek": 5,
                "Open": 1,
                "Promo": 1,
                "SchoolHoliday": 0,
                "CompetitionDistance": 1270.0,
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
            }
        }
    )