from itertools import islice
import math
def main():
    cities = []
    with open('cities10k.txt','r') as file:
        for line in islice(file, 10):
            city, lat, lon = line.rstrip().split()
            cities.append((city, float(lat), float(lon)))
    minv=math.sqrt(math.pow((cities[0][1] - cities[1][1]), 2) - math.pow((cities[0][1] - cities[1][1]), 2))  
    mincity1 = cities[0][0]
    mincity2 =cities[1][0]
    mincoord1 = [cities[0][1], cities[0][2]]
    mincoord2 = [cities[1][1], cities[1][2]]
    for city in cities:
        lat1=city[1]
        lon1=city[2]
        for city2 in cities:
            if city[0] == city2[0]:
                continue
            lats = lat1 - city2[1]
            lons = lon1 - city2[2]
            distance=math.sqrt(lats*lats + lons*lons)
            if(minv > distance):
                minv = distance
                mincity1 = cities[city][0]
                mincity2=cities[city2][0]
                mincoord1=[cities[city][1], cities[city][2]]
                mincoord2 = [cities2[1], cities[city2][2]]
    print("The shortest-distanced cities are:")
    print(mincity1, mincoord1, mincity2, mincoord2, "with distance: ", minv)

if __name__ == '__main__':
    main()
