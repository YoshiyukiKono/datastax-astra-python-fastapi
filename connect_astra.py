from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': './exclude/secure-connect-netlify.zip'
}
auth_provider = PlainTextAuthProvider('WGXMvkZitjTUJFlkDZKEjhph', 'bOSCbHGLu-6HQg5_KEluRCYMD_E.-STR1dMin,EE00xrsHoysy-MaHxPj5uRu33qRZW-v3idJbWA06osSJNNLS6yt+w1,K-lB-tuFv78YK9lmsrKGFW+WECM2UFZ48_A')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")

session.execute("""
  insert into test.member (id, first_name, last_name)
  values (%s, %s, %s)
  """,
  ('AZ123', 'Taro', 'Sato')
)
#session.execute("insert into test.member (id, first_name, last_name) values ('123','Yoshiyuki','Kono')").one()
