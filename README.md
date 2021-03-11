# Application querying MAC address vendor lookup

This is a simple command line application querying the https://macaddress.io/ MAC address lookup API
in order to return the name of the company that the given MAC address is associated with.

## Usage:

1. Clone this repository.
2. Create an account in the MAC address vendor lookup API:  https://macaddress.io/
3. Get your API_KEY that gives you access to query the API.
4. Copy the file *config_sample.py* and rename it to *config.py*.
5. In the global variable API_KEY value paste your own key from the API.
6. Build the docker from the attached file.

    _Example command:_
    
    <code>docker build -t yourdockerusername/cisco_task . </code>

7. Run the container in the interactive mode with the terminal attached. 

    _Example command:_
                        
    <code>docker run -p 8888:5000 -ti  yourdockerusername/cisco_task </code>
    
8. Input the MAC Address you need to check.
9. Enter your answer whether you want to continue or close the tool (Yes/No).


## Technical information:
* language: Python 3.8
* docker engine: v20.10.5

## Additional security:
1. Uploading private API_KEY to the public repository is highly dangerous, 
because it can be used by third parties for unwanted activities.
Because of this danger, the first launch of this application requires 
the creation of a config.py file and the provision of a custom API key.
The repository contains the *.gitignore* file which prevent the committing 
of this config.py file back to the repository.

2. In this demo application I assume that the server being queried 
(https://macaddress.io/) is safe. However, using public services like this
always involves the risk of some unwanted attack. Therefore, in a production setting, 
it is recommended to take into account the possible filtering of the received content.