# NagarPalika-DataHack

### Application
A chatbot for Telegram to improve the User Experience for patients.
The application contains a portal for the doctor to fill in the details of the medicine and time it should be taken. It then serves as a reminder for the user to take their medicine at specified times. 

### Data Visualisation
With the data stored, we can easily get to know effectiveness of a medicine (by taking into account several factors such as how much time it takes for the patient to be cured), outbreaks of a certain disease, tracking user's history. Also, taking feedback from a user, we can help pharmaceutical companies to size up their competition. 

### Technologies used
* Python (for communicating with Telegram) 
* SQLite (for storage)
* nodejs (for building the database)
* d3.js (for visualizations)
* Telegram API, Open Govt Data, John Snow Datasets

## Setup
#### Bot
It can be found in `docbot` folder.<br>
Run `python docbot.py` to run.
#### Form
It is in the root directory.<br>
Run `node server.js` and open `localhost:1185`
### Data Visualizations
Can be found in the `visualizations` directory.
