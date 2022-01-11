"""Alta3 Research | RZFeeser
   Visualizing tracking the ISS with open API data"""

#!/usr/bin/python3

# python3 -m pip install requests
import requests

# standard library imports
import turtle

## Trace the ISS - earth-orbital space station
EOSS = 'http://api.open-notify.org/iss-now.json'


# define a location on the map with a dot
def mapdot(yellowlat, yellowlon):
    mylocation = turtle.Turtle()
    mylocation.penup()
    mylocation.color('yellow')
    mylocation.goto(yellowlon, yellowlat)
    mylocation.dot(5)
    mylocation.hideturtle()
    return mylocation

# determine where the ISS is
def location():
    ## Call the webserv
    trackiss = requests.get(EOSS)

    # was a legal response code returned?
    if trackiss.status_code == 200:
        ## put into file object
        result = trackiss.json()
        ## determine latitude and longitude
        location = result.get('iss_position')  # preference for using the dict.get() method over key recall with []
        lat = location.get('latitude')
        lon = location.get('longitude')
        return (lat, lon)
    else:
        return None  # return None if the location cannot be determined


def main():
    loc = location()

    # stop execution of main if we cannot track the ISS
    if not loc:
        print("Unable to track ISS")
        return

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(loc)
    input('\nISS data retrieved & converted. Press any key to continue')
    lat,lon = loc
    print('\nLatitude: ', lat)
    print('Longitude: ', lon)

    ## prep the screen
    screen = turtle.Screen()  # create a screen object
    screen.setup(720, 360)  # set the resolution
    screen.setworldcoordinates(-180, -90, 180, 90) # describe the resolution as 2x as long as it is tall
    screen.bgpic('iss_map.gif')  # set the background image

    ## place a yellow dot at the location of the city we are currently in
    mapdot(47.6, -122.3)  # place got at this lat and lon

    ## Position the ISS Sprite
    screen.register_shape('spriteiss.gif')
    iss = turtle.Turtle()
    iss.shape('spriteiss.gif')
    iss.setheading(90)

    lon = round(float(lon))
    lat = round(float(lat))
    iss.penup()
    iss.goto(lon, lat)
    turtle.mainloop()

# call the main function
if __name__ == "__main__":
    main()
