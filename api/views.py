from multiprocessing import context
from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def get_data_from_dict(key, data):

    if key in data:
        return data[key]
    return ""

def get_all_rockets(request):
    response = requests.get("https://api.spacexdata.com/v3/rockets")

    json_data = response.json()

    rockets = []

    for data in json_data:

        rocket = {
            'rocket_id': get_data_from_dict('rocket_id', data),
            'rocket_name': get_data_from_dict('rocket_name', data),
            'cost_per_launch': get_data_from_dict('cost_per_launch', data),
            'success_rate_pct': get_data_from_dict('success_rate_pct', data),
            'first_flight': get_data_from_dict('first_flight', data)
        }

        rockets.append(rocket)

    context = {
        'rockets': rockets
    }

    return render(request, 'get_all_rockets.html', context)


def get_rocket_details(request, pk):
    response = requests.get(f"https://api.spacexdata.com/v3/rockets/{pk}")

    json_data = response.json()

    data = ['rocket_name', 'stages', 'boosters', 'cost_per_launch', 'success_rate_pct', 'first_flight', 'company', 'height', 'diameter', 'mass', 'first_stage', 'second_stage']

    rocket = {}

    for key in data:
        rocket[key] = get_data_from_dict(key, json_data)

    context = {
        'rocket': rocket
    }

    return render(request, 'rocket_details.html', context)
