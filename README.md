## Raspberry Pi Resources for Beginners
The Raspberry Pi is the tech equivalent of Harry Potter's magic wand. With knowledge and a little imagination, you can use it to work wonders. Here are a few resources to help you get started.

<br>
<img src="https://github.com/vbookshelf/Raspberry-Pi-Resources-for-Beginners/blob/main/images/rpi.jpg" width="500"></img>
<i>Raspberry Pi Zero W<br>Photo by Harrison Broadbent on Unsplash</i><br>

<br>

### What is a Raspberry Pi?

- Raspberry Pi Foundation<br>
What is a Raspberry Pi?<br>
https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/

- DroneBot Workshop<br>
What is a Raspberry Pi?<br>
https://dronebotworkshop.com/what-is-a-raspberry-pi/

- opensource.com<br>
What is a Raspberry Pi?<br>
https://opensource.com/resources/raspberry-pi

<br>

### How to set up your new Raspberry Pi

- Raspberry Pi Foundation<br>
Setting up your Raspberry Pi<br>
(Includes info on all the cables and things you're going to need.)<br>
https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/1

- Raspberry Pi Foundation<br>
How to set up and use your brand-new Raspberry Pi<br>
(Includes info on how to burn the OS onto an SD card using Etcher.)<br>
https://www.raspberrypi.com/news/how-to-set-up-and-use-your-brand-new-raspberry-pi/

- Murtaza's Workshop<br>
SETUP TO PROJECT in 20 mins | Raspberry Pi Tutorials for Beginners (2020)<br>
a) Compares the Raspberry Pi and the Arduino<br>
b) Shows how to set up and use the VNC Viewer<br>
c) Shows how to add the Raspberry Pi's temperature to the task bar [10:20]<br>
https://www.youtube.com/watch?v=B_8ZcPeaxcc


- Crosstalk Solutions<br>
Raspberry Pi 4 Getting Started<br>
https://www.youtube.com/watch?v=BpJCAafw2qE

<br>

### How to connect to your Raspberry Pi remotely
Normally you would need to connect a monitor, mouse and keyboard to a Raspberry Pi in order to use it. However, there are two more convenient ways to connect remotely. By setting up a virtual desktop you'll be able to access your raspberry Pi's GUI (Graphical User Interface) from your Mac or PC. You can also connect to your Raspberry Pi's command line using SSH. Keep in mind that installing Putty is only required on Windows PC's and not on a Mac.

- Caroline Dunn<br>
How to Remote Desktop to your Raspberry Pi with VNC Viewer<br>
https://www.youtube.com/watch?v=NWBmYnNvN3A

- ExplainingComputers<br>
Raspberry Pi Robotics #4: SSH Network Control<br>
This video explains how to set connect via SSH from a PC by using Putty.<br>
It also explains how to set up SSH on a tablet.<br>
https://www.youtube.com/watch?v=44yNbFictEg

- Maker Tutor<br>
How to SSH Raspberry Pi Remote access from MAC / Windows<br>
https://www.youtube.com/watch?v=kPeb5IvZW_k

- Raspberry Pi Documentation<br>
Remote Access<br>
https://www.raspberrypi.com/documentation/computers/remote-access.html

<br>

#### Notes

1- The VNC Viewer is what you will need. It's free. There is a fee for VNC Connect, but you don't need to download that for the setup.
This is the link to download the VNC Viewer:<br>
https://www.realvnc.com/en/connect/download/viewer/

2- Raspbian has been renamed Raspberry Pi OS.

3- How to connect from a Mac to the Raspberry Pi command line via SSH:<br>

a) First enable SSH from the Raspberry Pi desktop by clicking:<br>
Preferences --> Raspberry Pi Configuration --> Interfaces<br>
Under SSH select "Enable"

b) To get the Raspberry Pi's IP address, open a terminal on the Raspberry Pi desktop and type:<br>

$ hostname -I<br> (That's a capital I for indigo.)

c)To connect to the raspberry Pi from your Mac, open a terminal window, on your Mac, and type:<br>

$ ssh pi@<raspberry_pi_ip_address><br>
<i>Example: ssh pi@192.168.1.100</i><br>

Type "yes" if prompted.<br>
Enter the password for the Raspberry Pi.<br>
You should now see the Raspberry Pi command line.

c) The Raspberry Pi's IP address will change ech time it connects to your network.<br>
To set things up so that the address always stays the same, you will need to configure your router.<br>
The steps are different for different routers. Please refer to the advice given in the above video by Caroline Dunn.


<br>

### How to use the GPIO Pins

- Raspberry Pi Foundation<br>
Physical Computing with Python<br>
GPIO Pins<br>
https://projects.raspberrypi.org/en/projects/physical-computing/1

- ExplainingComputers<br>
Simple Guide to the Raspberry Pi GPIO Header<br>
https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/

- Pi My Life Up<br>
Raspberry Pi GPIO Tutorial: The Basics Explained<br>
https://www.youtube.com/watch?v=6PuK9fh3aL8

- GPIO Zero docs<br>
https://gpiozero.readthedocs.io/en/stable/

<br>

### How to connect and use a Raspberry Pi camera
This video explains how to use a pi camera from the Raspberry Pi command line and in python code. Sample code is included in this repo.

- DoneBot Workshop<br>
Raspberry Pi Cameras - The BIG Picture<br>
https://www.youtube.com/watch?v=MVgr302PNwY


<br>

### How to use a Raspberry Pi camera with OpenCV (cv2)

This tutorial explains how to use the Raspberry Pi camera with OpenCV. 
- Adrian Rosebrock<br>
Accessing the Raspberry Pi Camera with OpenCV and Python<br>
https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

#### Notes
- The tutorial says to install picamera[array] but I discovered that this was already installed on the Raspberry Pi.
- Sample code from the tutorial is included in this repo in the using-pi-camera-w-opencv-sample-code folder.
- Using picamera with OpenCV works, but what I've found is that, when running the code from the tutorial, the frame rate is 10 fps instead of 30 fps.

<br>


### Project Ideas
Now that you have everything set up here are some things that you can build:

- ExplainingComputers<br>
Raspberry Pi Zero W Surveillance Camera<br>
https://www.youtube.com/watch?v=rhIzfRmKHnQ

- ExplainingComputers<br>
Raspberry Pi Plant Watering<br>
(Includes info on using the Raspberry Pi for time lapse photography.)<br>
https://www.explainingcomputers.com/pi_watering.html

- ExplainingComputers<br>
Raspberry Pi Devastator Robot<br>
https://www.explainingcomputers.com/pi_devastator_videos.html

- The MagPi magazine tutorials<br>
https://magpi.raspberrypi.com/articles/category/tutorials

- Instructables<br>
Living Portrait Scare for Halloween Using a Raspberry Pi, PIR and Python<br>
https://www.instructables.com/Raspberry-Pi-Based-Living-Portrait-Player-Intro/


- Turn your Raspberry Pi into a Web Server<br>
Make Tech Easier<br>
https://www.youtube.com/watch?v=9pn1KKhxwdM


- All3DP<br>
The Pi's the Limit<br>
50 Cool Raspberry Pi Projects for October 2021<br>
https://all3dp.com/1/best-raspberry-pi-projects/



<br>


### Other

- The MagPi<br>
The official Raspberry Pi magazine.<br>
https://magpi.raspberrypi.com/

- If you're excited about getting into electronics, but you don't know where to start, then you might find the resources in the following repo helpful.<br>
vbookshelf<br>
Robotics Resources for Beginners<br>
https://github.com/vbookshelf/Robotics-Resources-for-Beginners

- Pi Spy<br>
Install Arduino IDE on Raspberry Pi<br>
https://www.youtube.com/watch?v=xWCwJXz4B4I


<br>



