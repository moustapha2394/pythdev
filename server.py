import os, socket, subprocess,select

host=""
port=1234
serveur=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serveur.bind((host,port))
serveur.listen(5)
print("le serveur ecoute a present sur le port {}".format(port))
serveur_lance=True
clients_connectes=[]
while serveur_lance:
    connexion_demandees, wlist, xlist=select.select([serveur],[],[],0.05)
    for connexion in connexion_demandees:
        connexion_avec_client, infos_connexion=connexion.accept()
        clients_connectes.append(connexion_avec_client)
    clients_a_lire=[]
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes, [],[],0.05)
    except select.error:
        pass
    else:
        for client in clients_connectes:
            msg_recu=client.recv(port)
            msg_recu=msg_recu.decode()
            print("recu: {}".format(msg_recu))
            client.send(b"5/5")
            if msg_recu=="exit()":
                serveur_lance=False
for client in clients_connectes:
    client.close()
serveur.close()