# OpenCV-Real-Time-Face-Recognition-Using-SQLite-Database
In this project, using Open CV modules and classes, a real time face detection and recognition application is made which takes a face as input, trains it using HaarCascade Frontal_face_default Classifier and then recognises it correctly if  multiple random faces are given as input. The images are stored to and retrieved from SQLite Database created in SQLite Studio.



Use Python 2.7 for running all the files.


1st run datasetcreator.py
it will create the dataset and load it into sqlite database
while giving input
enter id:1
enter name:"Sayantan" //name give in " "
enter age:22
enter gender:"M" //gender give in " "

after that run trainer.py to train the images
for id=1, 2 and so on images will be trained

finally run detector.py
