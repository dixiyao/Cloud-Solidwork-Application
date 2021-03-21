from openstack import connection
import os
import errno
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
import sys
import pandas as pd

auth = v3.Password(auth_url='https://home.jcloud.sjtu.edu.cn:5000/v3',
                   username='Jason',
                   password='200414Lhx',
                   project_name='jimmyyao18_project',
                   user_domain_name='Default',
                   project_domain_name='Default'
                  )

sess = session.Session(auth=auth)


conn = connection.Connection(
    session = sess,
    region_name='RegionOne',
    identity_interface='public',
    )
conn.authorize()

def list_servers(conn):
    print("List Servers:")

    for server in conn.compute.servers():
        print(dict(server)['name'])

def list_images(conn):
    print("List Images:")

    for image in conn.compute.images():
        print(dict(image)['name'])

def list_flavors(conn):
    print("List Flavors:")

    for flavor in conn.compute.flavors():
        print(dict(flavor)['name'])
        #print(flavor)


def list_networks(conn):
    print("List Networks:")

    for network in conn.network.networks():
        print(dict(network)['name'])
        print(network)

def create_keypair(conn):
    keypair = conn.compute.find_keypair('solidworks')
        
    if not keypair:
        print("Create Key Pair:")
                        
        keypair = conn.compute.create_keypair(name='solidworks')
                                
        print(keypair)
                                        
        try:
            os.mkdir('./ssh_dir')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise e
                                                                                                        
        with open('./ssh_dir/private_keypair_file', 'w') as f:
                f.write("%s" % keypair.private_key)
                                                                                                                                
        os.chmod('./ssh_dir/private_keypair_file', 0o400)
                
        return keypair

def create_server(conn):
    print("Create Server:")

    image = conn.compute.find_image("solidworks_19pro")
    flavor = conn.compute.find_flavor("research.4C.16G")
    network = conn.network.find_network("ydx")
    keypair = create_keypair(conn)

    server = conn.compute.create_server(
        name=sys.argv[1], image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], key_name='solidworks')

    server = conn.compute.wait_for_server(server)

    #conn.compute.change_server_password(server,'123456')

    print("ssh -i {key} root@{ip}".format(
        key='./ssh_dir/private_keypair_file',
        ip=server.access_ipv4))
    
    return server

def create_float_ip(conn):
    floatip = conn.network.create_ip(
        floating_network_id = '0145335c-c9b0-40bd-bc4b-73cd530ef934'
            )
    print("floating_ip:")
    address=floatip.floating_ip_address
    print(address)
    
    return floatip,address

def add_float_ip(conn, server, floatip):
    conn.compute.add_floating_ip_to_server(server, floatip.floating_ip_address)

def main():
    list_servers(conn)
    #list_images(conn)
    #list_flavors(conn) 
    #list_networks(conn)
    #list_serverste_keypair(conn)
    server = create_server(conn)
    floatip,address = create_float_ip(conn)
    add_float_ip(conn, server, floatip)

    file = open(r'D:\SJTU\2020_2021aki\GKC\pages\tmp\tmp_address.txt', 'w')
    file.write(str(address))
    file.close()

    file = open(r'D:\SJTU\2020_2021aki\GKC\pages\tmp\current_ip.txt', 'w')
    file.write(str(address))
    file.close()

    file = open(r'D:\SJTU\2020_2021aki\GKC\pages\tmp\current_username.txt', 'w')
    file.write(sys.argv[1])
    file.close()

    file = open(r'D:\SJTU\2020_2021aki\GKC\pages\tmp\current_userpassword.txt', 'w')
    file.write('Unknown')
    file.close()

    file = open(r'D:\SJTU\2020_2021aki\GKC\pages\tmp\current_account.txt', 'r')
    account = file.read()
    file.close()

    df = pd.read_csv(r'D:\SJTU\2020_2021aki\GKC\pages\inf\user_data.txt')
    for i in range(len(df)):
        if str(df.iloc[i].account) == account:
            df.iloc[i].ip = str(address)
            df.iloc[i].username = sys.argv[1]
            df.iloc[i].userpassword = 'Unknown'
            break

    df.to_csv(r'D:\SJTU\2020_2021aki\GKC\pages\inf\user_data.txt', index=False)
    

if __name__=="__main__":
    main()

