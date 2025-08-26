✅ Working

🔨 Tools: python 3.x, numpy==2.3.2, opencv_python==4.12.0.88, pyautogui==0.9.54, pygetwindow==0.0.9, pywin32==311

⚠️ Warning: This program uses local files

History -  It was overkill for that time, was my 2nd project in python, i dint know a lot of things about how the computer works and i learned a lot of this project, today i remember it like the most hard project i made (in solitary).
It was my first time optimizing a program, because i was a whole week looking for a way to pass the 0.5 fps treshold, so one day i found on stackoverflow a way to optimize it.

How it works - it takes multiple screenshots per fame of a window using system calls, so the images are converted onto bitmaps, who are converted onto numpy arrays to faster processing, so because bitmaps are
a resource of the os it can be deleted as if it were cache cleansing, the numpy array is deleted by the pyton's garbage collector, this images are taken as a parameter in anothe function (clickpoint.py), 
function who by using openCV matchs the images from screenshots and a local file, it works by using the imread built in function which has the library opencv, this function make matrix from pixels and 
compare them, i dont gonna enter into details about this lib, if its of your interest heres a link for the documentation: "https://opencv.org/blog/read-display-and-write-an-image-using-opencv/"- So, 
when the images are compared, if its a match it makes a rectangle marking it with the coords who are extracted by opencv and processed by numpy

