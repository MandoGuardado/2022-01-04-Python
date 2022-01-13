from flask import Flask, request
import requests

app = Flask(__name__)

ETCD = "http://127.0.0.1:2379/v2/keys/tickets"


# READ (return all of the tickets)
@app.route("/tickets", methods=["GET"])
def get_tickets():
    resp = requests.get(ETCD)
    resp = resp.json()
    # if the resp dict contains an errorCode
    if resp.get("errorCode"):
        return {"msg": f"Error Code: {resp['errorCode']}"}
    # if no errorCode assume there are tickets in system
    else:
        all_tickets = []
        # If someone manually deletes all entries from the directory /tickets/
        # then it will still test true (no errorCode), but won't have entry for "nodes"
        if resp.get("node").get("nodes"):
            # after studying resp dict, resp["node"]["nodes"] appears to be a list
            # of ticket entries. We cycle through this
            for ticket in resp.get("node").get("nodes"):
                # add a ticket number to all_tickets
                all_tickets.append(ticket.get("key").lstrip("/tickets/"))
            return {"tickets": all_tickets}
        else:
            return {"msg": "No Tickets Found! Good Work!"}


# READ (return a specified ticket)
@app.route("/tickets/<ticket_id>")
def get_one_ticket(ticket_id):
    resp = requests.get(f"{ETCD}/{ticket_id}")
    resp = resp.json()
    # if a key called errorCode is returned in the JSON
    if resp.get("errorCode"):
        # return false
        return {"msg": "Ticket Not Found"}
    else:
        # return the VALUE associated with they KEY called 'value'
        print(resp)
        return resp.get("node").get("value")


# CREATE (use POST to create a new ticket resource)
@app.route("/tickets", methods=["POST"])
def create_ticket():
    data = request.json
    print(data)
    value = data["value"]
    # sending a POST to the base URL will create a new /tickets/{ID}
    resp = requests.post(ETCD, data={"value": value})
    resp = resp.json()
    resp = resp.get("node").get("key").lstrip("/tickets/")
    return resp


# UPDATE (PUT the ticket's new info in place)
@app.route("/tickets", methods=["PUT"])
def update_ticket():
    # first test to see if that ticket exists
    data = request.json
    ticket_id = data["ticket_id"]
    msg = data["msg"]
    print(data)
    print(ticket_id)
    print(msg)
    if get_one_ticket(ticket_id):
        # assuming get_one_ticket returns a value that tests TRUE
        # the code will now issue a PUT to alter /tickets/{ticket_id}
        resp = requests.put(f"{ETCD}/{ticket_id}", data={'value': msg})
        resp = resp.json()
    else:
        return {"msg": f"Unable to update ticket # {ticket_id}"}
    # return a tuple of (new value, old value)
    return resp.get("node").get("value"), resp.get("prevNode").get("value")


# DELETE (remove a specified ticket resource)
@app.route("/tickets", methods=["DELETE"])
def delete_ticket():
    ticket_id = request.args.get("ticket_id")
    if ticket_id:
        requests.delete(f"{ETCD}/{ticket_id}")
        return f"The following ticket was deleted: {ticket_id}"
    else:
        return f"Unable to delete the ticket"


# DELETE (remove ALL ticket resources)
@app.route("/remove_all_tickets", methods=["DELETE"])
def delete_all_tickets():
    requests.delete(f"{ETCD}?dir=true&recursive=true")
    return {"msg": "You just removed everything. I hope you are happy now"}


if __name__ == "__main__":
    app.run(debug=True, port=2224, host="0.0.0.0")

