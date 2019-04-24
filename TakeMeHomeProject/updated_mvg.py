import TakeMeHomeProject.navigate as navigate
import googlemaps
import mvg_api

#x = input("enter name of station")
#depatures = navigate.get_id_of_station(station_id)

#starting_station_id = navigate.get_id_of_station(starting_destination_name)
#departures = navigate.get_departure(station_name)

def get_station_from_google():
    gmaps = googlemaps.Client(key='AIzaSyDJ-s_kYjvu_g9VCQ8FuW0H2bQFTDUoc9U')
    my_location = gmaps.geolocate()['location']
    nearby_stations = mvg_api.get_nearby_stations(my_location['lat'], my_location['lng'])
    return navigate.closest_station(my_location['lat'], my_location['lng'])

### TODO use the method  closest_station( lat, lon):

starting_destination_name= get_station_from_google()
final_destination_name = input("enter name of station (destination name)")
#final_station_id = navigate.get_id_of_station(final_destination)

routes =navigate.navigate_between(starting_destination_name, final_destination_name)
first_route = routes[0]
pprint(first_route)

departure_platform = first_route['connectionPartList'][0]['departurePlatform']
richtung = first_route['connectionPartList'][0]['destination']
tickets = first_route['tickets']

print(navigate.convert_from_epoch(first_route['departure']))
print(navigate.convert_from_epoch(first_route['arrival']))