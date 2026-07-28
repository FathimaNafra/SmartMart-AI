from pydantic import BaseModel


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