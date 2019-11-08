clients = "pablo,ricardo,"

def create_client(client_name):
    global clients

    clients += client_name
    add_comma()

def list_client():
    global clients

    print(clients)

def add_comma ():
    global clients

    clients += ","


if __name__ == '__main__':
    list_client()
    create_client("David")
    list_client()
    
