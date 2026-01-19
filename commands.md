# General list of commands used 


## Linux Commands

>   ### Remove application from linux (Google-CHROME for example)
```bash
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

-------------
## DOCKER Commands

>   ### Run Containers
```bash
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

<img width="322" height="240" alt="image" src="https://github.com/user-attachments/assets/dd1ed060-6c53-4532-a9db-e8c239c3b55c" />

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

>   ### Upgrade our container to use UV as well
```bash
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
## Recommded Commands! 

>   ### Select virtual Environment python 
        source ~/projects/zoomcamp/de_env/bin/activate,

        deactivate

        which python

>   ### UV virtual environment
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

