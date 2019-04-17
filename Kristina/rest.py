from bottle import route, run
@route('/')
def start():
    return 'Enter the station'

@route('/stationid/<stationid:int>')
def get_ring_from_id(stationid):
    return {stationid: 2}

@route('/station/<stationname>')
def get_ring_from_name(stationname):
    return {stationname: 3}


@route('/stations')
def list_all_stations():
    stations =[{'Marienplatz': 1},{'Karlsplatz': 1}]
    return dict(data = stations)

run(host='localhost', port=8080, debug=True)