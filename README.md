# Driver-Drowsiness-Alert-System
A simple algorithm to detect drowsiness of the drivers developed using OpenCV pretrained Haar Cascades to help prevent potential accidents.

* Link to download trained Keras model:<br>
https://drive.google.com/file/d/1IuC1spVSu7PGoi5zzFYAMG794VTa9Ixy/view?usp=sharing

Description
===============
* Utilize OpenCV's Haar cascades to build a simple drowsiness detection system.
* The algorithm first detect eyes positions, and then I preprocessed the region of interest (eyes), convert the eye images gray scale from BGR and resize to 24 by 24 image.
* The preprocessed region of interest then was fed into a Keras model with trained weight to classify whether the driver's eyes were open or closed.
* If both the drivers' eyes are closed for a certain amount of time, the system rings the alert.
* Weakness: The system does not work well with glasses, since the glasses are often confused with the eyebrows.

Result:
===============
Real-time testing result: https://www.youtube.com/watch?v=WvR4zn9WeRg&feature=youtu.be

Purpose:
===============
* Alert the driver immediately after he or she starts falling asleep, thus improving safety and reduce potential accidents.
* Maybe parents can use this system to alert their children whenever the children fall asleep while studying.

# License and Responsibility:
* The program and the code source are open for public use for any purpose without the need of licensing.
* The development of the system is served only for my purpose of learning OpenCV environment.
* I will not take any legal or non-legal responsibility if any accident or damage is resulted from this program.
