# energy_logic.py

# Przykładowe dane dotyczące zasobów naturalnych
naslonecznienie = {
    'Warszawa': 3.5,
    'Gdańsk': 3.0,
    'Kraków': 4.0,
    'Wrocław': 4.2,
}

wietrznosc = {
    'Warszawa': 5.0,
    'Gdańsk': 6.5,
    'Kraków': 4.0,
    'Wrocław': 4.5,
}

# Średnie zużycie energii na podstawie liczby domowników (kWh/rok)
zuzycie_na_rok = {
    1: (800, 1600),
    2: (1100, 1700),
    3: (1400, 2100),
    4: (1900, 2300),
    5: (2200, 2700),
}

# Funkcja doboru źródła energii
def dobierz_zrodlo_energii(location, energy_usage, budget, preference):
    sun_hours = naslonecznienie.get(location, 3.5)
    wind_speed = wietrznosc.get(location, 4.0)
    
    if preference == 'solar' or (preference == '' and sun_hours >= 3.5):
        if budget >= 15000:
            return "Zalecane źródło energii: Panele fotowoltaiczne"
        else:
            return "Panele fotowoltaiczne mogą być kosztowne. Rozważ inne opcje."
    elif preference == 'wind' or (preference == '' and wind_speed >= 5.0):
        if budget >= 20000:
            return "Zalecane źródło energii: Turbiny wiatrowe"
        else:
            return "Turbiny wiatrowe mogą być kosztowne. Rozważ inne opcje."
    elif preference == 'geotermal':
        if budget >= 25000:
            return "Zalecane źródło energii: Instalacja geotermalna"
        else:
            return "Instalacje geotermalne mogą być kosztowne. Rozważ inne opcje."
    else:
        return "Trudno dobrać odpowiednie źródło energii na podstawie dostępnych danych."
