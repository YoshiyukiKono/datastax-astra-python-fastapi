from fastapi import FastAPI
from pydantic import BaseModel

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': './exclude/secure-connect-<<YOUR DB NAME>>.zip'
}
auth_provider = PlainTextAuthProvider('<<CLIENT ID>>', '<<CLIENT SECRET>>')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

app = FastAPI()

class Member(BaseModel):
    first_name: str
    last_name: str
    id: str

@app.get("/")
async def read_root():
    return {"Status": "On"}


@app.get("/members/{member_id}")
async def read_member(member_id: str):

    row = session.execute("select first_name, last_name from test.member where id = %s",[member_id]).one()

    if row:
        return {"member_id": member_id, "first_name":row[0], "last_name": row[1]}
    else:
        return {"member_id": member_id}

@app.put("/members/upsert/{member_id}")
def upsert_member(member_id: str, member: Member):
    print('put member')
    session.execute("""
        insert into test.member (id, first_name, last_name)
        values (%s, %s, %s)
        """,
        (member_id, member.first_name, member.last_name)
    )
    return {"member_id": member_id}

@app.get("/members/delete/{member_id}")
async def delete_member(member_id: str):

    row = session.execute("delete from test.member where id = %s",[member_id]).one()

    return {"deleted": member_id}

