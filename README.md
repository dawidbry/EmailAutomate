The project was created for real needs at work related to sending requests for documentation to SOX audit, which takes place twice a year. Each time, approximately **240 e-mails** are sent with a request to send documentation to the indicated control by a given Control Owner and on a specified date and for a specific period of the financial year. This script allowed us to automate the sending of such a large number of repetitive emails.


File **automation_script.py** contains the code that creates the body (in html), subject etc. of the email and allows you to send emails with requests to test controls that are handled by the Control class.

File **controls_file.py** contains the code in which the **class Control** was created, which retrieves data from the file: **controls.csv** (each row in this file contains data for another control)


*control - business setting, or organizational control, involves the processes and procedures that regulate, guide, and protect an organization which is tested during SOX Audit
