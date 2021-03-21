from openstack import connection
import os
import errno
import sys

conn = connection.Connection(
        auth_url='https://home.jcloud.sjtu.edu.cn:5000/v3',
        username='Jason',
        password='200414Lhx',
        project_name='jimmyyao18_project',
        user_domain_name='Default',
        project_domain_name='Default',
        region_name='RegionOne',
        identity_interface='public'
        )
conn.authorize()

def delete(conn):
    if(len(sys.argv)<3):
        print("Error")
    else:
        server = conn.compute.find_server(sys.argv[1])
        conn.compute.delete_server(server)
        ip = conn.network.find_ip(sys.argv[2])
        conn.network.delete_ip(ip)
        
delete(conn)
