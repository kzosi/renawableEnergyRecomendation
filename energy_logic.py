from meteostat import Stations, Normals
import logging

def dobierz_zrodlo_energii(latitude, longitude, energy_usage, budget, preference):
    stations = Stations()
    stations = stations.nearby(latitude, longitude)
    station = stations.fetch(1)

    data = Normals(station)
    data = data.fetch()
    string = ""
    string += str(latitude)
    string += " "
    string += str(latitude)
    string += " "
    string += str(energy_usage)
    string += " "
    string += str(budget)

    return string
