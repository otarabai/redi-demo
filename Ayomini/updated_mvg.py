import navigate
from pprint import pprint

#x = input("enter name of station")
#depatures = navigate.get_id_of_station(station_id)

#starting_station_id = navigate.get_id_of_station(starting_destination_name)
#departures = navigate.get_departure(station_name)
starting_destination_name= input('Enter name of station(starting point)')
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
print("rings change : " + str(first_route['ringFrom']) + ' to ' + str(first_route['ringTo']))
print("zug from platform" + departure_platform + " in the direction of " + richtung)

for ticket in tickets:
    print(ticket['displayText'] +  '=>' + str(ticket['fare']) + '' + ticket['currency'] )
print()

#for departure in departures:
#   print(departure['departureId'])
#print(departures)
