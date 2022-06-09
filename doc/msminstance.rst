Configure Aws Instance For Math Sans Mystere
============================================

We need an instane in the cloud to do the following:

   - host the private package index that will host our helper python package.
   - act as an SSH host where we can maintain our math sans mystere question collection under github revision control.
   - Deploy the Math Sand Mystere Django web app where teachers can submit question lists for exercise document compilation.
   - perform the exercise .pdf generation to service teacher requests.


This is the stack of applications we are going to be using:

    - Ubuntu 20.06
    - Nginx
    - uWSGI
    - Python 3.8
    - Django 4.0


     


 
