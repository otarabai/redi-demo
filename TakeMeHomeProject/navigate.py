import mvg_api
import datetime

def get_id_of_station(station_name):
    return mvg_api.get_id_for_station(station_name)

def get_departures(station_id):
    return mvg_api.get_departures(station_id)

def convert_from_epoch(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time/1000).strftime('%Y-%m-%d %H:%M:%S')

def navigate_between(source_name, destination_name):
    starting_destination_id = get_id_of_station(source_name)
    print(starting_destination_id)

    destination_station_id = get_id_of_station(destination_name)
    print(destination_station_id)

    return mvg_api.get_route(starting_destination_id, destination_station_id)

def closest_station( lat, lon):
    nearest_stations=mvg_api.get_nearby_stations(lat,lon )
    return nearest_stations[0]['name']
