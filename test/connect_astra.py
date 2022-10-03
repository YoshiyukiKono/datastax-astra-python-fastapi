from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': './exclude/secure-connect-<<YOUR DB NAME>>.zip'
}
auth_provider = PlainTextAuthProvider('<<CLIENT ID>>', '<<CLIENT SECRET>>')
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
