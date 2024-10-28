import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://face-attendance-realtime-b4030-default-rtdb.firebaseio.com/'
})


ref = db.reference('Students')

data = {
    "12344":
        {
            "name": "Harsha C",
            "Major": "Management",
            "starting_year": 2017,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-10-11 15:54:34"
        },

    "12345":
        {
            "name": "Elon Musk",
            "Major": "Entrepreneurship",
            "starting_year": 2021,
            "total_attendance": 3,
            "standing": "A",
            "year": 3,
            "last_attendance_time": "2024-10-15 02:36:11"
        },

    "12346":
        {
            "name": "Mahesh B",
            "Major": "Acting",
            "starting_year": 2018,
            "total_attendance": 2,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2023-10-13 20:00:34"
        },

    "12347":
        {
            "name": "Prasannaw Maddipati",
            "Major": "Data Science",
            "starting_year": 2021,
            "total_attendance": 9,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-10-16 21:54:34"
        }

}

for key,value in data.items():
    ref.child(key).set(value)