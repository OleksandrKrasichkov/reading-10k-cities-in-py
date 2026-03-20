#from itertools import islice
import math
def main():
    cities = []
    with open('cities10k.txt','r') as file:
        for line in file:
            city, lat, lon = line.rstrip().split()
            cities.append((city, float(lat), float(lon)))
    minv,mincity1,mincity2,mincoord1,mincoord2 = setFirstMinv(cities)
    maxv = minv
    maxcity1 = mincity1
    maxcity2 = mincity2
    maxcoord1 = mincoord1
    maxcoord2 = mincoord2
    for i in range(len(cities) - 1):
        lat1=cities[i][1]
        lon1=cities[i][2]
        for j in range(i+1,len(cities)):
            lats = lat1 - cities[j][1]
            lons = lon1 - cities[j][2]
            distance=math.sqrt(lats*lats + lons*lons)
            if(minv > distance):
                minv = distance
                mincity1 = cities[i][0]
                mincity2=cities[j][0]
                mincoord1=[cities[i][1], cities[i][2]]
                mincoord2 = [cities[j][1], cities[j][2]]
            if(maxv < distance):
                maxv = distance
                maxcity1 = cities[i][0]
                maxcity2 = cities[j][0]
                maxcoord1 = [cities[i][1],cities[i][2]]
                maxcoord2 = [cities[j][1], cities[j][2]]
    print("The shortest-distanced cities are:")
    print(mincity1, mincoord1, mincity2, mincoord2, "with distance: ", minv)
    print("The farthest cities are:")
    print(maxcity1, maxcoord1, maxcity2, maxcoord2, "with distance: ", maxv)


def setFirstMinv(cities):
    for i in range(len(cities)-1):
        lat1=cities[i][1]
        lon1=cities[i][2]
        for j in range(i+1,len(cities)):
             lats = lat1 - cities[j][1]
             lons = lon1 - cities[j][2]
             distance=math.sqrt(lats*lats + lons*lons)
             if distance != 0:
                return [distance, cities[i][0], cities[j][0],[cities[i][1],cities[i][2]],[cities[j][1],cities[j][2]]]


if __name__ == '__main__':
    main()
