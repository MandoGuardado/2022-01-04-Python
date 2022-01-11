#!/usr/bin/python3

import pandas as pd


def main():
    flightcsv = pd.read_csv("airline_flights.csv")

    # organize data by origin and destination airport
    flightcsv_tofrom = flightcsv.groupby(['ORG_AIR', 'DEST_AIR']).size()
    print(flightcsv_tofrom.head())

    # Display the number of flights between Huston (IAH)
    # and Atlanta (ATL) in both directions
    print("\nFlight from ATL to IAH and IAH to ATL")
    print(flightcsv_tofrom.loc[[("ATL", "IAH"), ("IAH", "ATL")]])

    # display first 5 entries of the flightcsv dataframe
    print(flightcsv_tofrom.head())


if __name__ == "__main__":
    main()
