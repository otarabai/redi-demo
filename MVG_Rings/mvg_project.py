import mvg_api as mvg




'''

for i in range (1,10):

        mvg_stations = {}
        station_data = mvg.get_stations(i)

        #mvg_stations[i] = station_data[0]['name']
        #print(station_data)
        
        if i == 12:
            index = 0
            while index < len(station_data):
                for key in station_data[index]:
                    print(key,index,station_data[index][key])
                index += 1

        '''
'''
route = mvg.get_route(1, 3)
#print((route))

index = 0
while index < len(route):
    for key in route[index]:
        print(key,index,route[index][key])
    index += 1

#print(route[8]['ringFrom'])
'''

station_from = input("Enter Origin : ")
station_data_from = mvg.get_stations(station_from)  #'Karlsplatz (Stachus)' Isartor Marienplatz
station_id_from = station_data_from[0]['id']
station_to = input("Enter Destination : ")
station_data_to = mvg.get_stations(station_to)  # Feldmoching   Frankfurter Ring Scheidplatz
station_id_to = station_data_to[0]['id']

#print (station_id_from)
#print (station_id_to)
route_data = mvg.get_route(station_id_from, station_id_to)

#print(route_data[0]['ringFrom'])
#print(route_data[0]['ringTo'])
print (route_data)

print('You have to travel from Ring: ' + str(route_data[0]['ringFrom']) + ' to Ring: ' + str(route_data[0]['ringTo']))

'''
new_list_stations = []
idss = mvg.get_stations('')
for station in idss:
    #print(station)
    id = station['id']
    name = station['name']
    new_idss = {'id': id , 'name': name}
    print (new_idss)

    new_list_stations.append(new_idss)

start_station = 1110
for station in new_list_stations:
    mvg.get_route(start_station,station['id'])

'''












