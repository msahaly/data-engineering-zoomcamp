# General list of commands used 


## Linux Commands

>   ### Remove application from linux (Google-CHROME for example)

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
    

-------------
>   ### Run Containers

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

>   ### List Containers
        # List all 
        docker ps -a

        # List all container IDs 
        docker ps -aq

        # Remove all containers that worked previously Using their IDs
        docker rm `docker ps -aq` 

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

