################################################################################
#
# Course: CS 540, fall 2020
# Homework: HW1
# Date 9/13/2020
# Name: Samuel Kruse
#
################################################################################
import math as M
# – return the Manhattan distance between two dictionary data points from the data set.
def manhattan_distance(data_point1, data_point2):
    dmax = abs(float(data_point1['TMAX']) - float(data_point2['TMAX']))
    dmin = abs(float(data_point1['TMIN']) - float(data_point2['TMIN']))
    dprcp = abs(float(data_point1['PRCP']) - float(data_point2['PRCP']))
    return dmax + dmin + dprcp
 # – return a list of data point dictionaries read from the specified file.    
def read_dataset(filename):
    weatherData = []
    file = open(filename, "r")
    for line in file:
        line = line.strip("\n")
        datos = line.split(" ")
        day = {'DATE':datos[0], 'TMAX':datos[2], 'PRCP':datos[1], 'TMIN':datos[3], 'RAIN': datos[4] }
        weatherData.append(day)
    file.close()
    return weatherData

# – return a prediction of whether it is raining or not based on a majority vote of the list of neighbors.
def majority_vote(nearest_neighbors):
    t = 0
    for day in nearest_neighbors:
        t = (t + 1 if day['RAIN'] == "TRUE" else t + 0)
    return ("TRUE" if t >= M.ceil(float(len(nearest_neighbors))/2.0) else "FALSE")

    # – using the above functions, return the majority vote prediction for whether it's raining or not on the provided test point.
def k_nearest_neighbors(filename, test_point, k, year_interval):
    weatherData = read_dataset(filename)
    interval = calculate_interval(test_point['DATE'], year_interval)
    possibleNeighbors = []
    
    for date in weatherData:
        if is_in_interval(date["DATE"], interval):
            possibleNeighbors.append(date)
            
    with_distances = distance_comp(possibleNeighbors, test_point)
    sorted_neighbors = sorted(with_distances, key = lambda i: i['DIST'])
    print(sorted_neighbors[:k])
    return majority_vote(sorted_neighbors[:k])
      
def calculate_interval(date, year_interval):
    year = int(date.split("-")[0])
    start_year = year - year_interval + 1
    interval = []
    for years in range(start_year, year + year_interval):
        interval.append(str(years))
    return interval

def is_in_interval(date, interval):
    return True if date.split("-")[0] in interval else False

def distance_comp(neighbors, test_point): 
    for neighbor in neighbors:
        dist = manhattan_distance(neighbor, test_point)
        neighbor['DIST'] = dist
    return neighbors
