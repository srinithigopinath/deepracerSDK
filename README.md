#Deep Racer SDK 

#### The Deep Racer SDK is a python wrapper on AWS deepracer. This allows you to use the deepracer as a standalone car to experiment and apply some interesting use cases. My ultimate goal for this project is to use the AWS deepracer to develop an app and control it through HID devices like Joy Stick for example. I also plan to use the onboard sensors on the AWS Deep Racer to create my own machine learning models to drive the car autonomously

#### For more information on the Deep Racer, please visit [AWS Deep racer](https://aws.amazon.com/deepracer/)

####The AWS Deep Racer consists of a compute module, a motor controller for controlling the car, a servo to control the steering, LED lights as visual indicators, and an array of sensors for autonomous navigation. The model I tested with has solely a camera, but this can also be extended to add a lidar and an additional camera for stereo-scopic vision. AWS Deep Racer comes with out of the box services running on the compute model. These services use robot operating system and a python/django based webserver running on it to serve API requests. My project creates a wrapper on top of this API so that Deep Racer can be used in python projects. 

## How to Install the Project

#### Please follow the steps to setup your deepracer using this link [Deep Racer Start Up Guide](https://d1.awsstatic.com/deepracer/AWS-DeepRacer-Getting-Started-Guide.pdf)

####After this set up, your Deep Racer will be calibrated and connected to your wifi network. The IP address of your Deep Racer is important for initializing the library. In your set up, you can also change your password from the default password given. Your password is also important for this library. 

####The following python libraries are required: 

| Required Libraries      | Description |
| ----------- | ----------- |
| requests-html |  Used to make calls to the API running in the compute module of the AWS Deep Racer      |

```
pip install requests-html

```
#### Once you have installed the above library, do the following: 

```
pip install deepracer-python

```

## How to use the library 

#### Initialization 
```
from Deepracer import deepracer as d
deep_racer = d.Deepracer(base_url='your ip address', password='your password')
```
This initialization connects the library to the deepracer 

####Log In 

```
deep_racer.login()
```
This step validates your login, which is required before you can issue any additional control commands. This method will return true if the log in is successful or false if the log in is unsuccessful. 

####Changing the LED colors

```
deep_racer.set_calibration_mode()
deep_racer.set_led_color(255, 0, 0)

```

This step allows you to change your LED lights. Before being able to change your lights, you must call the `set_callibration_mode` method. Then, enter the parameters for the color you desire. Parameters can be between 0-255 and represent the values for red, green, and blue. 

####Setting the Drive Mode 

```
 drive_status = deep_racer.set_drive_mode_to_manual()
 start_status = deep_racer.start()
 let_us_drive = deepracer.manual_drive_forward(0, 1, 1) 
```

These methods mimick the order in which the DeepRacer APIs are called. To use the driving methods, you must first set the drive mode to manual. Then, you must call the start method. To drive forward, you can call the `manual_drive_forward` method and enter parameter values between 0 and 1. These values represent the angle, max speed, and throttle. 

#####Reversing the Drive mode 

```
 let_us_drive = deepracer.manual_drive_reverse(0, 1, 1) 
```
After setting the drive mode to manual and calling the start method, you can make the Deep Racer move in reverse using this method. Similarily, the parameters are between 0-1 and represent angle, max speed, and throttle. 

####Stopping the Deep Racer 


```
 deep_racer.stop()
```

To stop the DeepRacer, call the stop method. 