import socket
from Script import square, add_list, rem_list
from PartieDeBelote import partieDeBelote

host = ''
port = 5005

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((host, port))
tcp_socket.listen(5)

connection, info = tcp_socket.accept()

received = connection.recv(1024)
while received != b"end":
    mode = str(received.decode())[0]
    if mode == "p":
        connection.send("Combien de points maximum ?")
        points_max = 0
        while points_max <= 0:
            pt_max = connection.recv(1024)
            try:
                points_max = int(pt_max.decode())
            except:
                connection.send("Vous n'avez pas entré un nombre")
    elif mode == "t":
        connection.send("Nombre de tours de jeu ?")
        tours_max = 0
        while tours_max <= 0:
            tours = connection.recv(1024)
            try:
                tours_max = int(tours.decode())
            except:
                connection.send("Vous n'avez pas entré un nombre")

    
    print(received.decode())
    if received.decode() == "script":
        connection.send("Which script do you want to use?\n1. Get the square of a number\n2. Play with a list".encode())
        number = connection.recv(1024)
        b = int(number.decode())
        if b == 1:
            script = "Square"
        elif b == 2:
            script = "Liste"
        else:
            script = "Retour"

        if script == "Square":
            received = connection.recv(1024)
            a = int(received.decode())
            message = str(a) + " * " + str(a) + " = " + str(square(a))
            print(message)
            connection.send(message.encode())
            received = connection.recv(1024)
        elif script == "Liste":
            message = "The current list is: " + str(l)
            connection.send(message.encode())
            
            to_do = int(connection.recv(1024).decode())
            if to_do == 1:
                list_length = int(connection.recv(1024).decode())
                for i in range(list_length):
                    num_r = connection.recv(1024)
                    num = int(num_r.decode())
                    add_list(l, num)
            elif to_do == 2:
                to_rem = int(connection.recv(1024).decode())
                rem_list(l, to_rem)
            else:
                break

            message = "The result: " + str(l)
            print(message)
            connection.send(message.encode())
            received = connection.recv(1024)
        elif script == "Retour":
            received = connection.recv(1024)
    elif received.decode() == "end":
        break

print("Closing host...")
connection.close()
tcp_socket.close()
print("Host closed.")
