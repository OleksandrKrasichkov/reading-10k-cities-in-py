from itertools import islice
def main():
    with open('cities10k.txt','r') as file:
        for line in islice(file, 10):
            city, lat, lon = line.rstrip().split()
            print(city, lat, lon)


if __name__ == '__main__':
    main()
