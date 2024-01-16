import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccount.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facialrecognition-752c6-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "2712":
        {
            "name": "Durlabh Pathak",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-03-01 00:54:34"
        },
    "1819":
        {
            "name": "Ishaan Jain",
            "major": "IT",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-03-01 00:54:34"
        },

    "2710":
        {
            "name": "MAHI JAIN",
            "major": "IT",
            "starting_year": 2020,
            "total_attendance": 5,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-03-01 00:54:34"
        },
    "2713":
        {
            "name": "Leslie Fu",
            "major": "Biological Science",
            "starting_year": 2014,
            "total_attendance": 3,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-02-28 08:54:34"
        },
    "2714":
        {
            "name": "Rachell Hofstetter",
            "major": "Game Development",
            "starting_year": 2014,
            "total_attendance": 5,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-02-28 08:56:34"
        },
    "2715":
        {
            "name": "Jodi Lee",
            "major": "Biology Science",
            "starting_year": 2016,
            "total_attendance": 8,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-03-01 01:54:34"
        },
    "2500":
        {
            "name": "Siddhant Khariwal",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-03-01 01:54:34"
        },
    "2501":
        {
            "name": "Tushar Kapoor",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-03-01 01:54:34"
        },
}

for key, value in data.items():
    ref.child(key).set(value)