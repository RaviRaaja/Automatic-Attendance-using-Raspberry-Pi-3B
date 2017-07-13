# Automatic-Attendance-using-Raspberry-Pi-3B
Automatic Attendance system using raspberry pi model B3
## Data set generation 
Run datasetgen.py to generate data set of faces from you webcam.
## Training the model
Run datatrain.py to train captured face features and serialized .yum file.
## Validation of model using raspberry pi
Run facedetector.py to validate model , webcam will search for the trained faces.
This model can further improved using Convolutional Neural Network for generating more features.
For more number of users use SQLite database to store features of the faces.
