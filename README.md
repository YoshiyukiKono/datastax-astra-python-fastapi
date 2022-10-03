# datastax-astra-python-fastapi

## Environment

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
