# Alphus

Detection of potholes using Image Processing, IR sensor, Flex sensor and ESP8266

PoHoDePre module consists of a infrared sensor, a flex sensor, a microcontroller and image processing using opencv. The module will be attached near the rear wheels of every vehicle. The infrared sensor shall keep sensing the distance between the road and the module. The data will be nearly constant except when the vehicle encounters with a pothole. In such case, there will be significant error in data in comparison to the average data when the car moves smoothly over plane road. Image processing of the potholes will be done using opencv. The contour detection, erosion and dilation followed by Canny detection will take place. The sensor data will be stored in database by means of the microcontroller. The flex sensor will indicate if the vehicle is taking a turn or not. Now for the time when the vehicle is moving straight, the data from infrared sensor will be taken and for every abnormal data indicating presence of potholes, the route will be searched in the map using GPS, and the location of the map will be stored in database to be conveyed to the municipality for checking and covering the potholes. Since many vehicles shall have the same module, the data maybe verified too.
We have also created an app through MIT Inventor app which has features like manual reporting of potholes whose weekle reports will be sent to the government, blog along with the comment section, a google map where the region with pothole is highlighted based on the pictures and location detected by the sensor and reported by the people.







The tools and Technologies used are mentioned below:
1)IR Sensor and Flex sensor : Detection of potholes , uneven roads in dry areas.
2)OpenCV and python : To detect the potholes especially during rainy season.
3)ESP8266 : To get the real-time location 
4)MIT App : For extra features and a user-friendly platform to share views and report.






A camera must be fitted under the bonet of the car to get a clear image of the potholes. The continuous process of detect, locate and report takes place. The IR sensor and Flex sensor checks for the potholes. If detected, ESP8266 comes in action to give the location over WIFI. During rainy seasons, image processing using OpenCV is carried out to detect the potholes. Geocoder library of python is used to detect the location in this case. The locations are marked purple on the Google Maps which awares the people before hand.
The app works independently where the users can report the potholes manually which are saved in an Excel file and the weekly report is sent to the government. It also provides the platform to express their views with other thousands of people facing the same issue.






Different systems for potholes already exist but here we have tried to develop a cost effective system that reduces the cost by around 2000 bucks. The hardwares are simple to understand and implement. Apart from just pothole detection, we have added certain extra features o make it more socially acceptable. Our future works includes testing the module on the Indian roads and to identify and solve the bugs in the system and adding more functionalities in the app.  



