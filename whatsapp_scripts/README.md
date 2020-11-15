# Whatsapp scripts

## Additional requirements
```
pip install pyautogui
```

Make sure that you have whatsapp desktop app installed and linked with your mobile with QR code scanned in your system, otherwise the script wont work as per the requirement.

## 1) bulk.py<br/>
```
python bulk.py
```
From a csv file, saved in the current directory all the information is taken and then the corresponding messages are sent to the contacts.</br>

<p><b>Structure of csv file</b></p>

| Name     |    Contact         |  Message     |
|----------|:------------------:|-------------:|
| Asif     | +919685\*\*\*7\*\* | Message 1    |
| Rohan    | +919876\*\*\*6\*\* | Message 2    |
| Sahil    | +919856\*\*\*3\*\* | Message 3    |



## 2) spam.py<br/>
```
python spam.py
```
Inputs of target contact number,message,spam length are taken from the user, and then specified number of messages are sent to the target contact.

<br/>
<br/>

Note: The script may or may not work in all kinds of systems. As pyautogui takes the display type of buttons into consideration which maybe different in different machines.
