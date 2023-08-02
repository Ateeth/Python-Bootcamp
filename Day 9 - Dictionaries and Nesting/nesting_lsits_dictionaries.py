capitals = {
    'France': 'Paris',
    'Germany': 'Berlin'
}

# Nest list in dictionary
travel_log = {
    "France": ['Paris', 'Lille', 'Dijon'],
    "Germany": ['Berlin', 'Hamburg', 'Stuttgart']
}

list1 = ['A', 'B', ['C', 'D']]

# Nest Dictionary into Dictionary
travel_log1 = {
    "France": {
        "cities_visited": ['Paris', 'Lille', 'Dijon'] ,
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ['Berlin', 'Hamburg', 'Stuttgart'],
        "total_visits": 5
    }
}

# Nest Dictionary into a List
travel_log2 = [
    {
        "country": "France",
        "cities_visited": ['Paris', 'Lille', 'Dijon'] ,
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ['Berlin', 'Hamburg', 'Stuttgart'],
        "total_visits": 5
    }
]

