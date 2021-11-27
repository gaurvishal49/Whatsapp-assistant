# Whatsapp-assistant
A powerful tool to automatically perform some tasks within whatsapp.

This tool has the following functions:
1. isonline(name) - Finds and let you know if the person ('name') is online or not.
2. stalk(name)  - Outputs a file with the times when the person ('name') came online during the code running.
3. profiledownloader(name)  - Outputs the profile photo and a text file contaning the status of the targetted person.
4. bulksend(name, msg, iteration) - send the automated text messages in bulk. using this a message ('msg') can be sent a couple of times (using iteration) or several messages (in this case 'msg' is the list of messages and iteration is set to 0) can be sent one by one.
5. savealldp()  - using this function, one can save all the DP of all the contacts at once. The images saved will be saved with the contact name as the file name.
6. schedular(name, tim, msg)  - schedules a message ('msg') to a person ('name') and sends it on the desired time ('tim'). The format of 'tim' is 'dd/mm/yyyy hr:min'.
