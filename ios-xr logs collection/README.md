# IOS-XR_logs_collection

When customer opens a TAC case for IOS-XR device, TAC engineer requests certain logs from device for analysis. These logs could include below.

   - Various show tech commands from either IOS-XR or Admin mode.
   - Crash/Core/log files from device
   - Output of various show commamnds
   
This script will automate collection of above information from IOS-XR devices and upload captured logs to case.

This tool can be used by
- Customers
- HTEs/NCEs who needs to capture and upload IOS-XR logs on behalf of customer
- TAC engineers - They can help customer to upload logs easily to case during Troubleshooting sessions.

Where this tool need to be run
- From customer Jump Server or local machine.
	

## Getting Started

- Setup virtual environment and install required libraries.  	
- Create a python file and copy script code to it.
  	

### Prerequisites

Python virtual environment and libraries (netmiko, requests, tqdm) need to be installed

### Installing

Steps to ready environment on Jump Server to run this tool.

- Login to Jump Server and create a folder for script and cd to it. You can choose any name for folder. Here I have used 'script'
	
	`[rakeshk6@dansalan ~]$ mkdir script && cd script`

- Create Python3 Virtual Environment with name venv1	
	
	`[rakeshk6@dansalan script]$ python3 -m venv venv1`
	
- Activate virtual environment:
	
	```
	[rakeshk6@dansalan script]$ source venv1/bin/activate
  	(venv1) [rakeshk6@dansalan script]$
	```
  	
- Upgrade pip
  	
  	`(venv1) [rakeshk6@dansalan script]$ python -m pip install --upgrade pip`
  	
- Install packages required for this script
  	
  	`(venv1) [rakeshk6@dansalan script]$ pip install netmiko requests tqdm`
  	
- Create a new python file with ‘vi’ utility and save the script content (link below) to this file.
	
	`(venv1) [rakeshk6@dansalan script]$ vi ios-xr_log_collection_v1.py`
	

## Deployment

This script need to be run from Jump Server or local machine. It should met following criteria
- Reachability to IOS-XR device from where logs need to be captured.
- Reachability to cxd.cisco.com

## Usage

- Run the tool and supply information as prompted.

- Below are the information required to run the script.

	- SR number - This will work as username for file upload to CXD (Customer Experience Drive).
	- Token for file Upload - This is Secure Token to upload file to CXD Drive using HTTPS put method.
	- Device IP and Credentials (Script doesn’t store any credentials for Security purpose)
	- TAC requested ‘show tech commands’ or usual ‘show commands’
   

This Script provides 5 user options to choose from:


    * To run show tech commands in "IOS-XR mode" and upload file/s to TAC case Choose: 1
    * To run show tech commands in "Admin mode" and upload file/s to TAC case Choose: 2
    * To upload already generated or saved file/s to TAC case Choose: 3
    * To run Only SHOW commands , capture output to file and upload it to TAC case Choose: 4
    * To upload existing file on Local machine/JumpHost to TAC case: 5
   

Additional notes
	- This tool will need CXD token which is a unique token for every TAC case and can be found on case notes.
	
    * Customer need to login to Cisco’s Support Case Manager using CCO ID and password.
    * Open the Case > Notes and search for ‘CXD Upload Credentials’

	Refer below link for more details.
	https://www.cisco.com/c/en/us/support/web/tac/tac-customer-file-uploads.html#cxd
	
	- Once user has supplied all required 'show' commands, user need to hit enter again to execute the script.

## Contributing

Rakesh Kumar (rakeshk6@cisco.com)

## Authors

Rakesh Kumar (rakeshk6@cisco.com)

## License

This project is licensed under ...
Details should be found in a [LICENSE](https://wwwin-github.cisco.com/AIDE/ios-xr_logs_collection/blob/master/LICENSE) file

## Acknowledgments

* Below Course on Udemy helped me to get start with Python
https://cisco.udemy.com/course/master-python-network-automation-for-network-engineers
