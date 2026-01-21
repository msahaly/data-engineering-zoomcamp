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
