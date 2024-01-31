"""Write a Python program that implements a Python program that filters out dates (in the format "YYYY-MM-DD") that are in the future using the filter function. 

Escribe un programa en python que implement un programa en python que filtre fechas (en el formato "YYYY-MM-DD")
que estan en el futuro usando la funcion filter
"""
from datetime import datetime

date_strings = ["2023-07-11", "2022-02-22", "2024-05-11", "2025-12-31", "2021-01-01"]

currentTime = datetime.now().date()


