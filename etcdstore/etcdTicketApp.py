#!/usr/bin/python3
"""Russell Zachary Feeser Using etcd to design a RESTful ticket server"""

import requests

ETCD = "http://127.0.0.1:2379/v2/keys/tickets"

## read all available tickets
## use a GET on a directory to return all results
def gettickets():
    resp = requests.get(ETCD)
    resp = resp.json()
    # if the resp dict contains an errorCode
    if resp.get("errorCode"):
        return False
    # if no errorCode assume there are tickets in system
    else:
        ticketlist = []
        ## if someone manually deletes all entries from the directory /tickets/
        ## then it will still test true (no errorCode), but won't have entry for "nodes"
        if resp.get("node").get("nodes"):
        ## after studying resp dict, resp["node"]["nodes"] appears to be a list
        ## of ticket entries. We cycle through this
            for ticket in resp.get("node").get("nodes"):
                ## add a ticket number to ticketlist
                ticketlist.append(ticket.get("key").lstrip("/tickets/"))
            return ticketlist
        else:
            return False


## get a specific ticket
## pass in the ticket to GET
def getoneticket(ticketid):
    resp = requests.get(f"{ETCD}/{ticketid}")
    resp = resp.json()
    ## if a key called errorCode is returned in the JSON
    if resp.get("errorCode"):
        # return false
        return False
    else:
        # return the VALUE associated with they KEY called 'value'
        return resp.get("node").get("value")


## create a ticket
## use a POST to create a new resource
def createticket(descofissue):
   ## sending a POST to the base URL will create a new /tickets/{ID}
   resp = requests.post(ETCD, data={'value': descofissue })
   resp = resp.json()
   ## take resp["node"]["key"].lstrip("/tickets/") which is the ticketID
   resp = resp.get("node").get("key").lstrip("/tickets/")
   return resp

## update a ticket
## pass in the ticket to PUT
def updateticket(ticketid, descofissue):
    ## first test to see if that ticket exists
    ## invoke the function getoneticket(ticketid) to test
    ## this returns a FALSE if the ticket returns and error code
    if getoneticket(ticketid):
        ## assuming getoneticket returns a value that tests TRUE
        ## the code will not issue a PUT to alter /tickets/{ticketid}
        resp = requests.put(f"{ETCD}/{ticketid}", data={'value': descofissue })
        resp = resp.json()
    else:
        return False
    ## return a tuple of (new value, old value)
    return (resp.get("node").get("value"), resp.get("prevNode").get("value"))

## delete a ticket
## pass in the ticket to DELETE
def deleteticket(ticketid):
    requests.delete(f"{ETCD}/{ticketid}")
    return

## delete ALL tickets
## use the api parameter ?dir=true&recursive=true to remove a directory
def deletealltickets():
    requests.delete(f"{ETCD}?dir=true&recursive=true")
    return

def main():

    ## Enter a while true loop (run until a break condition)
    while True:

        ## pop up a menu
        print("""
        1) Read all available tickets
        2) Get ticket
        3) Create ticket
        4) Update ticket
        5) Delete ticket
        6) Exit
        99) DANGER! Delete all tickets
        """)

        ## collect input from user
        userinput = ""
        while userinput == "":
            userinput = input("> ")

        ## user wants ALL available tickets
        if userinput == "1":
            ## getickets() returns a list or FALSE
            ticketlist = gettickets()
            ## Test what was ticketlist?
            if ticketlist:
                print()
                for ticket in ticketlist:
                    print(f"Ticket ID - {ticket}")
            else:  ## if ticketlist() returned FALSE
                print("There are no tickets in the system")

        ## user wants info on a single ticket
        elif userinput == "2":
            ticketid = input("What is the ticket ID? ")
            oneticket = getoneticket(ticketid)
            # if oneticket returns a string or FALSE
            if oneticket:
                print(f"\nFor {ticketid}:")
                print(f"    Ticket Description - {oneticket}")
            ## handles condition where FALSE is returned
            else:
                print("That ticket does not exist within the system.")

        ## user wants to create a ticket
        elif userinput == "3":
            descofissue = input("Give a short 140 char description of the issue: ")
            createdticket = createticket(descofissue)
            print(f"\nTicket {createdticket} has been created.")

        ## user wants to update a ticket
        elif userinput == "4":
            ticketid = input("Update what ticket ID? ")
            descofissue = input("What is the updated 140 char description of the issue: ")
            ## updatedticket returns a two-tuple, or FALSE
            updatedticket = updateticket(ticketid, descofissue)
            if updatedticket:
                print(f"\nFor {ticketid}:")
                print(f"    Updated Ticket Description - {updatedticket[0]}")
                print(f"    Old Ticket Description - {updatedticket[1]}")
            else: ## if updatedticket() returned FALSE
                print("That ticket does not exist within the system.")

        ## user wants to delete a ticket
        elif userinput == "5":
            ticketid = input("What is the ticket ID? ")
            deleteticket(ticketid)
            print(f"\nTicket {ticketid} has been removed from the system")

        ## user wants to exit
        elif userinput == "6":
            ## end the while True loop
            break

        elif userinput == "99":
            deletealltickets()
            print("All tickets have been removed from the system")

        ## user inputs a non valid option
        else:
            print("That is not a valid option")

    print("Thanks for using the Alta3 RESTful ticketing service")

if __name__ == "__main__":
    main()

