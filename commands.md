# General list of commands used 
===

## Linux Commands

### remove application from linux (Google-CHROME for example)

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
 


## Docker Commands


-------------
## Python Commands

    #install pandas 
        pip install pandas

-------------
## Recommded Commands! 
