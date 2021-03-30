# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep
from numpy import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    pass;


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import requests

    # Making a PUT request
    key = '9149a3e4-b8b9-47f7-a31c-fc297567a612'

    # url = "https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/Baloon1/Properties/neon_level?method=PUT&value=50&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true";
    take_off_location = "44,26";
    lat1 = 44
    long1 = 26

    lat2 = 44
    long2 = 26

    lat3 = 44
    long3 = 26

    lat4 = 44
    long4 = 26

    lat5 = 44
    long5 = 26

    current_location = "44,26";

    # air_pressure = round(random.uniform(0.9, 1.2), 2)
    # current_speed =round(random.uniform(8.33, 16.66), 2)
    # wind_speed = round(random.uniform(5.33, 20.66), 2)
    # air_temperature = round(random.uniform(-5.33, 37.66), 2)

    nitrogen_level = 78.084;
    oxygen_level = 20.946;
    argon_level = 0.9340;
    co2_level = 0.041500;
    neon_level = 0.001818;
    helium_level = 0.000524;
    methane_level = 0.000187;
    krypton_level = 0.000114;

    things = ["Baloon1", "Baloon2", "Baloon3", "Baloon4", "Baloon5"]
    # for thing in things:
    #     url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/take_off_location?method=PUT&value={take_off_location}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
    #     r = requests.get(url)
    #     print(r)

    # property_name = "current_location"
    # property_val = "66,90,89"
    # url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/{property_name}?method=PUT&value={property_val}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
    # r = requests.get(url)
    # print(r)
    while 1:
        for thing in things:
            if thing is "Baloon1":
                lat1 += round(random.uniform(-2, 2), 1)
                long1 += round(random.uniform(-2, 2), 1)
                current_location = str(lat1) + "," + str(long1)
            if thing is "Baloon2":
                lat2 += round(random.uniform(-2, 2), 1)
                long2 += round(random.uniform(-2, 2), 1)
                current_location = str(lat2) + "," + str(long2)
            if thing is "Baloon3":
                lat3 += round(random.uniform(-2, 2), 1)
                long3 += round(random.uniform(-2, 2), 1)
                current_location = str(lat3) + "," + str(long3)
            if thing is "Baloon4":
                lat4 += round(random.uniform(-2, 2), 1)
                long4 += round(random.uniform(-2, 2), 1)
                current_location = str(lat4) + "," + str(long4)
            if thing is "Baloon5":
                lat5 += round(random.uniform(-2, 2), 1)
                long5 += round(random.uniform(-2, 2), 1)
                current_location = str(lat5) + "," + str(long5)

            altitude = round(random.uniform(9.1, 39), 2)

            air_pressure = round(random.uniform(0.9, 1.2), 2)
            current_speed = round(random.uniform(8.33, 16.66), 2)
            wind_speed = round(random.uniform(5.33, 20.66), 2)
            air_temperature = round(random.uniform(-5.33, 37.66), 2)

            nitrogen_level = round(random.uniform(78.084, 80), 6)
            oxygen_level = round(random.uniform(20.946, 23), 6)
            argon_level = round(random.uniform(0.9340, 0.95), 6)
            co2_level = round(random.uniform(0.041500, 0.05), 6)
            neon_level = round(random.uniform(0.001818, 0.00182), 6)
            helium_level = round(random.uniform(0.000524, 0.00053), 6)
            methane_level = round(random.uniform(0.000187, 0.00019), 6)
            krypton_level = round(random.uniform(0.000114, 0.000117), 6)
            s = nitrogen_level + oxygen_level + argon_level + co2_level + neon_level + helium_level + methane_level + krypton_level -100
            nitrogen_level-=s

            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/nitrogen_level?method=PUT&value={nitrogen_level}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/oxygen_level?method=PUT&value={oxygen_level}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/argon_level?method=PUT&value={argon_level}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/co2_level?method=PUT&value={co2_level}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/neon_level?method=PUT&value={neon_level}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/helium_level?method=PUT&value={helium_level}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/methane_level?method=PUT&value={methane_level}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/krypton_level?method=PUT&value={krypton_level}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)

            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/air_pressure?method=PUT&value={air_pressure}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/current_speed?method=PUT&value={current_speed}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/wind_speed?method=PUT&value={wind_speed}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/air_temperature?method=PUT&value={air_temperature}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)

            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/altitude?method=PUT&value={altitude}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)
            url = f"https://PP-2103221158HN.devportal.ptc.io:443/Thingworx/Things/{thing}/Properties/current_location?method=PUT&value={current_location}&appKey=9149a3e4-b8b9-47f7-a31c-fc297567a612&x-thingworx-session=true"
            r = requests.get(url)
            print(r)

        sleep(30)
        print("ok")
