from openstack import connection
import os
import errno
from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
import sys

auth = v3.Password(auth_url='https://home.jcloud.sjtu.edu.cn:5000/v3',
                   username='Jason',
                   password='200414Lhx',
                   project_name='jimmyyao18_project',
                   user_domain_name='Default',
                   project_domain_name='Default'
                  )

sess = session.Session(auth=auth)
sess.get('https://home.jcloud.sjtu.edu.cn:5000/v3')

conn = connection.Connection(
                    session = sess,
                    region_name='RegionOne',
                    identity_interface='internal',
                    )
conn.authorize()

def stop(conn):
    if(len(sys.argv)<2):
        print("Error")
    else:
        server = conn.compute.find_server(sys.argv[1])
        conn.compute.stop_server(server)

stop(conn)

