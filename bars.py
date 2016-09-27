import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding="utf-8-sig") as handle:
            data = json.load(handle)    
    return data
    
    
def get_biggest_bar(data):
    seats = data[0]['Cells']['SeatsCount']
    for d in data:
        if d['Cells']['SeatsCount'] > seats:
            seats = d['Cells']['SeatsCount']
            biggest_bar = d
    return biggest_bar    


def get_smallest_bar(data):
    seats = data[0]['Cells']['SeatsCount']
    for d in data:
        if d['Cells']['SeatsCount'] < seats:
            seats = d['Cells']['SeatsCount']
            biggest_bar = d
    return biggest_bar   


def get_closest_bar(data, longitude, latitude):
    dist = ((longitude-data[0]['Cells']['geoData']['coordinates'][0])**2 +
                (latitude-data[0]['Cells']['geoData']['coordinates'][1])**2)
    for i in data:
        long = i['Cells']['geoData']['coordinates'][0]
        lat = i['Cells']['geoData']['coordinates'][1]
        new_dist = ((longitude-long)**2 +
                        (latitude-lat)**2)
        if new_dist < dist:
            dist = new_dist
            closest_bar = i
    return closest_bar

if __name__ == '__main__':
    path = '/projects/3_bars/bars.json'
    file = load_data(path)
    try:
        latitude = float(input('Введите широту: '))
        longitude = float(input('Введите долготу: '))
    except ValueError:
        print('Некорректые координаты!')
        
    big_bar = get_biggest_bar(file)
    small_bar = get_smallest_bar(file)
    closest_bar = get_closest_bar(file, longitude, latitude)
    print('Самый большой бар: ' + big_bar['Cells']['Name'] + ', ' + big_bar['Cells']['Address'] + ', Количество мест: ' + str(big_bar['Cells']['SeatsCount']))
    print('Самый маленький бар: ' + small_bar['Cells']['Name'] + ', ' + small_bar['Cells']['Address'] + ', Количество мест: ' + str(small_bar['Cells']['SeatsCount']))
    print('Ближайший бар: ' + closest_bar['Cells']['Name'] + ', ' + closest_bar['Cells']['Address'] + ', Количество мест: ' + str(closest_bar['Cells']['SeatsCount']))
    
            
    
