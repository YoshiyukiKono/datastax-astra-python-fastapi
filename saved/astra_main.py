from fastapi import FastAPI
from pydantic import BaseModel

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': './exclude/secure-connect-netlify.zip'
}
auth_provider = PlainTextAuthProvider('WGXMvkZitjTUJFlkDZKEjhph', 'bOSCbHGLu-6HQg5_KEluRCYMD_E.-STR1dMin,EE00xrsHoysy-MaHxPj5uRu33qRZW-v3idJbWA06osSJNNLS6yt+w1,K-lB-tuFv78YK9lmsrKGFW+WECM2UFZ48_A')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

class Member(BaseModel):
    first_name: str
    last_name: str
    id: str

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    print('kono test')
    return {"item_name": item.name, "item_id": item_id}

@app.get("/members/{member_id}")
async def read_member(member_id: str):
    #row = session.execute("""select first_name, last_name from test.member where id = %s""",(member_id)).one()
    row = session.execute("select first_name, last_name from test.member where id = '" + member_id + "'").one()
    #row = session.execute("select first_name, last_name from test.member where id = '123'").one()
    if row:
        return {"member_id": member_id, "first_name":row[0], "last_name": row[1]}
    else:
        return {"member_id": member_id}

@app.put("/members/{member_id}")
def update_member(member_id: str, member: Member):
    print('put member')
    session.execute("""
        insert into test.member (id, first_name, last_name)
        values (%s, %s, %s)
        """,
        (member_id, member.first_name, member.last_name)
    )
    return {"member_id": member_id}



