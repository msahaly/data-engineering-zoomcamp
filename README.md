# DE ZoomCamp

## How to use?!
>   ### Build and Run the pipeline 
>   #### This will display the data automatically and will create the parquet file

```bash
    # Build the docer image from the Dockerfile
    docker build -t test:pandas .

    # Run the docker image "test:pandas" passing arugmner month=12
    docker run --rm test:pandas 12 
```

===

## Run green taxi trips ?
>   #### Start the Postgresql container
```bash
        # Run Postgresql server
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
>   #### Start pgAdmin 
```bash
        # Run pgAdmin
        docker run -it \    
        -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
        -e PGADMIN_DEFAULT_PASSWORD="root" \
        -v pgadmin_data:/var/lib/pgadmin \
        -p 8085:80 \
        --network=pg-network \
        --name pgadmin \
        dpage/pgadmin4
```
>   ### Build and Run the pipeline 
```bash
        # Build the pipleline docker image
        docker build -t green-taxi:v001 .

        # Run the pipeline
        docker run -it --rm \
        --network=pg-network \
        green-taxi:v001 \
        --pg-user=root \
        --pg-pass=root \
        --pg-host=pgdatabase \
        --pg-port=5432 \
        --pg-db=ny_taxi 
```