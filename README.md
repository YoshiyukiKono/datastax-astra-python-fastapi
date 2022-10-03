# datastax-astra-python-fastapi

## On this repository

DataStax Astra DBをご利用になる際には、

## Preparation

## My Local Environment

```
conda create -n datastax -y python=3 pip
conda activate datastax
```

```
python --version
Python 3.10.4
pip --version
pip 21.2.4 from C:\Users\yoshi\Anaconda3\envs\datastax\lib\site-packages\pip (python 3.10)
```

## Python Package
```
pip install fastapi
pip install uvicorn[standard]
```

## Data

### keyspace: `test`

### Table: `member`
```
CREATE TABLE test.member (
    id text PRIMARY KEY,
    first_name text,
    last_name text
) 
```

## Configure

```
```

## Usage

```
uvicorn astra_main:app --reload
```

Open the following link 

http://12.0.0.1/8000/docs

### 
