
# Fortinet Automation
**Netsec automation for Fortinet

Main folder contains python scripts and jinja templates to automate the creation of fw address objects.
I used a similar script for a customer' firewall migration to generate about 440 lines of cli code in 2 seconds.
Combine this for example with the HTTP requests library in python to make API calls to the fortigate using JSON/RPC.

**Update 30/12/2021

I added the FortiOS API/ directory.
This contains python scripts that use the requests library to perform API calls against a Fortigate' RESTAPI interface.
The two scripts will first retrieve a list of existing address or service objects to ensure no unnecessary calls are made
for objects that already exist.

Examples of how to call the script and the expected output included.

No specific libraries required except those that are by default included in python 3.8.10
