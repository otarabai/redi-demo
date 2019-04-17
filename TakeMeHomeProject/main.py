import navigate
from pprint import pprint

starting_destination_name = input("Enter name of station (starting point): ")
final_destination_name = input("Enter name of station (destination point): ")

routes = navigate.navigate_between(starting_destination_name, final_destination_name)
first_route = routes[0]
#pprint(first_route)

departure_platform = first_route['connectionPartList'][0]['departurePlatform']
richtung = first_route['connectionPartList'][0]['destination']

print(navigate.convert_from_epoch(first_route['departure'])/n)
print(navigate.convert_from_epoch(first_route['arrival']))
print("rings change : " + str(first_route['ringFrom']) + ' to ' + str(first_route['ringTo']))
print("Zug from platform " + departure_platform + " in the direction of " + richtung)

tickets = first_route['tickets']

for ticket in tickets:
    print(ticket['displayText'] + ' => ' + str(ticket['fare']) + ' ' + ticket['currency'])
print()