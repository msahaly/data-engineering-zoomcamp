# General list of commands used 

[Linux Commands](#linux-Commands)  
        - [Run Containers](#run-containers)  
        - [List Containers](#list-containers)  
        - [Let's Build our Container](#let's-build-our-container)  
        - [Upgrade our container to use UV as well](#upgrade-our-container-to-use-uv-as-well)  

[Docker Commands](#docker-commands)  
[Python Commands](#python-commands)  
[POSTGRES](#postgres)  
        - [RUN postgres container (DB SERVER)](#run-postgres-container-(db-server))  
        - [Connect to POSTGRES using python sqlalchemy](#connect-to-postgres-using-python-sqlalchemy)  
        
[Recommended Commands!](#recommended-commands)  
[Dockerize and run ingestdata pipeline](#dockerize-and-run-ingestdata-pipeline)  
        - [Create Network](#create-network)  
        - [Run posgres server on the network and give it a name](#run-posgres-server-on-the-network-and-give-it-a-name)  
        - [Dockerize the pipeline to connect to the postgres server over the network](#dockerize-the-pipeline-to-connect-to-the-postgres-server-over-the-network)   
        - [pgAdmin](#pgadmin)  

         



## Linux Commands

>   ### Remove application from linux (Google-CHROME for example)
```sh
        # Remove Application from linux (Google-CHROME for example)
        # Check size of Chrome's configuration and cache
        du -sh ~/.config/google-chrome ~/.cache/google-chrome

        # 1. Remove the browser and its system-level dependencies
        sudo apt purge google-chrome-stable -y

        # 2. Clean up any leftover dependencies that were only needed for Chrome
        sudo apt autoremove -y

        # 1. Remove the local configuration (bookmarks, history, extensions)
        rm -rf ~/.config/google-chrome

        # 2. Remove the cache (temporary images and site data)
        rm -rf ~/.cache/google-chrome

        #Remove the Repository (Keep your 'apt update' clean)
        sudo rm /etc/apt/sources.list.d/google-chrome.list

        # This should return nothing (Verification)
        whereis google-chrome
 ```   

 ```sh
        # Stop a service
        sudo systemctl stop docker

        # disk free." It reports how much disk space is being used and how much is available on all your mounted file systems.
        df -h
 ```

-------------
## DOCKER Commands

>   ### Run Containers
```sh
        # Just Run containers
        docker run python:3.13.11-slim

        # Make them interactive
        docker run -it  python:3.13.11-slim

        # Sepcify entry point script to run - bash for this example 
        docker run -it --entrypoint=bash  python:3.13.11-slim

        ## Add localfiles to the run container from $(pwd)/test:/app/test.
        docker run -it --entrypoint=bash -v $(pwd)/test:/app/test python:3.13.11-slim

        ## Remove once exit.
        docker run -it --entrypoint=bash -v $(pwd)/test:/app/test --rm python:3.13.11-slim

```

>   ### List Containers
```bash
        # List all 
        docker ps -a

        # List all container IDs 
        docker ps -aq

        # Remove all containers that worked previously Using their IDs
        docker rm `docker ps -aq` 

```

>   ### Let's Build our Container 
>   ### Let's dockerize our pipeline with its UV python and dependencies)

```dockerfile
        # Create Dockerfile
        FROM python:3.13.11-slim

        # Install dependencies
        RUN pip install pandas pyarrow

        # Set work directory
        WORKDIR /code

        # Copy pipeline.py file into the WORKDIR
        COPY pipeline.py .

        # Add entrypoint to automatically start the pipeline when container starts
        ENTRYPOINT ["python", "pipeline.py"]

```

<img width="322" height="240" alt="image" src="https://github.com/user-attachments/assets/dd1ed060-6c53-4532-a9db-e8c239c3b55c" />

```bash
        # Save the file and build the docker Image (-t tag/name)
        docker build -t test:pandas .

        # WITHOUT ENTRY POINT IN Dockerfile
        # Run the docker container now (If it has NO ENTRYPOINT in Dockerfile)
        docker run test:pandas
        docker run -it --entrypoint=bash --rm test:pandas

        # Now you are in the /code dir with the pipeline.py file there altready
        # Run the pipeline now and it shall work and show data and also export .parquet file
        python pipeline.py 12

        #WITH ENTRY POINT IN Dockerfile
        # Run the container (If it has the ENTRYPOINT in Dockerfile)
        docker run -it --rm test:pandas 12

```

>   ### Upgrade our container to use UV as well
```dockerfile
        # Copy uv binary from official uv image (multi-stage build pattern)
        COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

        # Add virtual environment to PATH so we can use installed packages
        ENV PATH="/app/.venv/bin:$PATH"

        # Copy dependency files first (better layer caching)
        COPY "pyproject.toml" "uv.lock" ".python-version" ./
        
        # Install dependencies from lock file (ensures reproducible builds)
        RUN uv sync --locked

        # Final Dockerfile looks like this
        FROM python:3.13.11-slim
        COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
        WORKDIR /code 
        ENV PATH="/code/.venv/bin:$PATH"
        COPY "pyproject.toml" "uv.lock" ".python-version" ./
        RUN uv sync --locked
        COPY pipeline.py /code/pipeline.py
        ENTRYPOINT ["python", "pipeline.py"]
```
<img width="525" height="311" alt="image" src="https://github.com/user-attachments/assets/4c41fdf2-0eab-4765-a0aa-3b592f13a502" />

        # Now to Run build and run 
        docker build -t test:pandas .
        docker run -it --rm test:pandas 12




-------------
## Python Commands

    #install pandas 
        pip install pandas

-------------
## POSTGRES
>   ### RUN postgres container (DB SERVER)
```bash

        # With named volume
        docker run -it --rm \
        -e POSTGRES_USER="root" \
        -e POSTGRES_PASSWORD="root" \
        -e POSTGRES_DB="ny_taxi" \
        -v ny_taxi_postgres_data:/var/lib/postgresql \
        -p 5432:5432 \
        postgres:18

        # Or with bind mount:
        mkdir ny_taxi_postgres_data

        docker run -it \
        -e POSTGRES_USER="root" \
        -e POSTGRES_PASSWORD="root" \
        -e POSTGRES_DB="ny_taxi" \
        -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql \
        -p 5432:5432 \
        postgres:18

        # Install/Add pgcli 
        uv add --dev pgcli

        # Run pgcli to connect to postgres DB server
        uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
```
>   ### Connect to POSTGRES using python sqlalchemy

```sql
        # Connect to postgresql server using python instead of pgcli using sqlalchemy
        !uv add sqlalchemy
        from sqlalchemy import create_engine

        prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
        url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'
        df = pd.read_csv(url, nrows=100)
        
        # Display first rows
        print(df.head())
        
        # Check data types
        print(df.dtypes)
        
        # Check data shape
        print(df.shape)

        # Create engine //root=user, root@ = passwordm localhost=server, :5432=pory, /ny_taxi=db
        engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

        #Check the schema that pandas intend to use = create table = for your df
        print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))

        # Insert data into table - if table exists, replace it (Note: we initialized it with 0 rows in df.head(0))
        df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

        # Insert/Appending data (100,000 rows appended)
        df.head(100000).to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

        # Slize DF into chunks (of 100,000 rows each)
        df_iter = pd.read_csv(
                url,
                dtype=dtype,
                parse_dates=parse_dates,
                iterator=True,
                chunksize=100000
                )
        
        # To watch/monitor progress over iterable
        !uv add tqdm
        from tqdm import tqdm

        # To insert data (Chuncked) into DB table using loop (tqdm is used around iterable to show action)
        for df_chunk in tqdm(df_iter):
        df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append') 
```
>   ### Named volume vs Bind mount:

        Named volume (name:/path): Managed by Docker, easier
        Bind mount (/host/path:/container/path): Direct mapping to host filesystem, more control

>   ### PostGres Commands
```sql
        # list tables
        \dt

        #list datatypes
        \dT
```

-------------
## Recommended Commands 

>   ### Select virtual Environment python 
        source ~/projects/zoomcamp/de_env/bin/activate,

        deactivate

        which python

>   ### UV virtual environment

```markdown
        # Initialize new paython version using UV inside project folder 
        # Note: It will create .env/ nad pyproject.toml
        uv init --python 3.13 

        # Check the UV version of python
        uv run python -V

        # Check which python in uv
        uv run which python

        # Add dependencies to the UV version of python
        # Note: It will update the pyproject.toml dependencies array
        uv add pandas pyarrow


        # Run the UV python 
        uv run python pipeline.py 

        # Run the UV python with ARGUMENTS
        uv run python pipeline.py 12

        # Set default python to be UV python: Click ctrl+shft+P then >python - choose add enterpreter path - /workspaces/data-engineering-zoomcamp/pipeline/.venv/bin/python - then open new terminal and notice bottom right version of python it will be the uv one
        the run as follows normally
        python pipeline.py 12

        # Add Jupyter 
        uv add --dev jupyter

        # Run Jupyter 
        uv run jupyter notebook

        # Add pgcli
        uv add --dev pgcli

        # Run pgcli
        uv run pgcli -h localhost -p 5432 -u root -d ny_taxi
 

```

>   ### Connect to POSTGRES using python sqlalchemy
```sql

        # Connect to postgresql server using python instead of pgcli using sqlalchemy
        !uv add sqlalchemy
        from sqlalchemy import create_engine

        # Create engine //root=user, root@ = passwordm localhost=server, :5432=pory, /ny_taxi=db
        engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

        #Check the schema that pandas intend to use = create table = for your df
        print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))

        # Insert data into table - if table exists, replace it (Note: we initialized it with 0 rows in df.head(0))
        df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

        # Insert/Appending data (100,000 rows appended)
        df.head(100000).to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

        # Slize DF into chunks (of 100,000 rows each)
        df_iter = pd.read_csv(
                url,
                dtype=dtype,
                parse_dates=parse_dates,
                iterator=True,
                chunksize=100000
                )
        
        # To watch/monitor progress over iterable
        !uv add tqdm
        from tqdm import tqdm

        # To insert data (Chuncked) into DB table using loop (tqdm is used around iterable to show action)
        for df_chunk in tqdm(df_iter):
        df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append') 
```
```bash
        #Convert notebook.ipyno to python script and rename it
        uv run jupyter nbconvert --to=script notebook.ipynb
        mv notebook.py ingest_data.py
```
>   ### Doker Volumes
```bash
        # This will show you docker volumns
        # Example is: [-v ny_taxi_postgres_data:/var/lib/postgresql] when running postgresql
        # It shall list "ny_taxi_postgres_data" from previous example (usually /var/lib/docker/volumes/)
        docker volume ls

        # Inspect the volume details To see exactly where on your Ubuntu/Debian disk this data is physically stored:
        docker volume inspect ny_taxi_postgres_data
```
 

## Dockerize and run ingestdata pipeline
>   ### Create Network
```bash
        # Create a netowrk 
        docker network create pg-network
```
>   ### Run posgres server on the network and give it a name 
```bash
        # Add nework and name to the postgres server container
        docker run -it \
        -e POSTGRES_USER="root" \
        -e POSTGRES_PASSWORD="root" \
        -e POSTGRES_DB="ny_taxi" \
        -v ny_taxi_postgres_data:/var/lib/postgresql \
        -p 5432:5432 \
        --network=pg-network \
        --name pgdatabase \
        postgres:18
```
>   ### Dockerize the pipeline to connect to the postgres server over the network
```bash
        # Use the name and network in ingest_data pipeline to connect to the postgres server by changing the hostname
        docker run -it --rm \
        --network=pg-network \
        ingest-data:v001\
        --pg-user=root \
        --pg-pass=root \
        --pg-host=pgdatabase \
        --pg-port=5432 \
        --pg-db=ny_taxi \
        --target-table=yellow_taxi_trips_2021 \
        --year=2021 \
        --month=1 \
        --chunksize=100000
```

>   ### pgAdmin
```bash 
        # In another terminal, run pgAdmin on the same network
        docker run -it \
        -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
        -e PGADMIN_DEFAULT_PASSWORD="root" \
        -v pgadmin_data:/var/lib/pgadmin \
        -p 8085:80 \
        --network=pg-network \
        --name pgadmin \
        dpage/pgadmin4
```

## Docker-Compose 
>  ### Create docker-compose.yaml 
```bash
        # Create docker-compose.yaml file 
        services:
        pgdatabase:
        image: postgres:18
        environment:
        - POSTGRES_USER=root
        - POSTGRES_PASSWORD=root
        - POSTGRES_DB=ny_taxi
        volumes:
        - "ny_taxi_postgres_data:/var/lib/postgresql:rw"
        ports:
        - "5432:5432"
        pgadmin:
        image: dpage/pgadmin4
        environment:
        - PGADMIN_DEFAULT_EMAIL=admin@admin.com
        - PGADMIN_DEFAULT_PASSWORD=root
        volumes:
        - "pgadmin_data:/var/lib/pgadmin"
        ports:
        - "8085:80"

        volumes:
        ny_taxi_postgres_data:
        pgadmin_data:
```

>   ### docker-compose commands
```bash
        # Run docker-compose
        docker-compose up

        # Shutting down containers Ctrl+C Or
        docker-compose down

        # Run containers in the background (Free up terminal)
        docker-compose up -d

        # View logs
        docker-compose logs

        # Stop and remove volumes
        docker-compose down -v

        # check the network link:
        docker network ls

        # Run ingest pipeline again for that network (it's pipeline_default for network name)
        docker run -it \
        --network=pipeline_default \
        taxi_ingest:v001 \
        --pg-user=root \
        --pg-pass=root \
        --pg-host=pgdatabase \
        --pg-port=5432 \
        --pg-db=ny_taxi \
        --target-table=yellow_taxi_trips_2021_2 \
        --year=2021 \
        --month=2 \
        --chunksize=100000

        # List all containers
        docker ps -a

        # Remove specific container
        docker rm <container_id>

        # Remove all stopped containers
        docker container prune
```
>   ### docker images
```bash
        # List all images
        docker images

        # Remove specific image
        docker rmi taxi_ingest:v001
        docker rmi test:pandas

        # Remove all unused images
        docker image prune -a
```  
>   ### docker volumes
```bash
        # List volumes
        docker volume ls

        # Remove specific volumes
        docker volume rm ny_taxi_postgres_data
        docker volume rm pgadmin_data

        # Remove all unused volumes
        docker volume prune
```

>   ### docker networks
```bash
        # List networks
        docker network ls

        # Remove specific network
        docker network rm pg-network

        # Remove all unused networks
        docker network prune
```

>   ### Complete cleanup (removes everything):
```bash
        # ⚠️ Warning: This removes ALL Docker resources!
        docker system prune -a --volumes
```

>   ### CClean up local files:
```bash
        # Remove parquet files
        rm *.parquet

        # Remove Python cache
        rm -rf __pycache__ .pytest_cache

        # Remove virtual environment (if using venv)
        rm -rf .venv
```