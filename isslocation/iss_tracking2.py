#!/usr/bin/python3

# standard library imports
import turtle
import urllib.request
import json

## Trace the ISS - earth-orbital space station
EOSS = 'http://api.open-notify.org/iss-now.json'

def main():
    ## Call the webserv
    trackiss = urllib.request.urlopen(EOSS)

    ## put into file object
    ztrack = trackiss.read()

    ## JSON 2 Python data structure
    result = json.loads(ztrack.decode('utf-8'))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(result)
    input('\nISS data retrieved & converted. Press any key to continue')

    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    print('\nLatitude: ', lat)
    print('Longitude: ', lon)

    screen = turtle.Screen()  # create a screen object
    screen.setup(720, 360)  # set the resolution

    screen.setworldcoordinates(-180,-90,180,90)

    screen.bgpic('iss_map.gif')

    ## My location
    yellowlat = 47.6
    yellowlon = -122.3
    mylocation = turtle.Turtle()
    mylocation.penup()
    mylocation.color('yellow')
    mylocation.goto(yellowlon, yellowlat)
    mylocation.dot(5)
    mylocation.hideturtle()

    ## ISS Sprite
    screen.register_shape('spriteiss.gif')
    iss = turtle.Turtle()
    iss.shape('spriteiss.gif')
    iss.setheading(90)

    lon = round(float(lon))
    lat = round(float(lat))
    iss.penup()
    iss.goto(lon, lat)
    turtle.mainloop()

if __name__ == "__main__":
    main()
