---
toc: true
comments: true
layout: post
title: FINAL DATA STRUCTURES PROJECT
description: CSP
type: tangibles
courses: { compsci: {week: 3} }
---


# Collections 

- This is my blog about my python model and SQLite Database

- Show your unique collection/table in database, display rows and columns in the table of the SQLite database from VSCode using SQLite3 Editor.

- This image shows the sqlite database containing the name of the image. the imageFunc, imageBase64

<a href="https://ibb.co/yYLx7rn"><img src="https://i.ibb.co/NmwGbM6/fdb-1.png" alt="fdb-1" border="0"></a>

-  Show your unique code that was created to initialize table and create test data from VSCode model.

- This code is used to create the name formatting imageName, imageFunc, and ImageBase64 with the class Images(Base):

<a href="https://ibb.co/Z1xvqqK"><img src="https://i.ibb.co/vvkf00m/fdb-2.png" alt="fdb-2" border="0"></a>

# Lists and Dictionaries

- This is my blog about my python API code and use of List and Dictionaries.

- Show a list as extracted from database as Python objects in VSCode using Debugger.

- This shows the list in vscode with the image encrypted in base64 and the test inputted.

<a href="https://ibb.co/T4chSPc"><img src="https://i.ibb.co/v31zGL1/fdb-3.png" alt="fdb-3" border="0"></a>

- Show two distinct examples of dictionaries, show Keys/Values using debugger in VSCode.

- This is the dictionary for image, the text, and a list of the image data and the file name along with the meme text.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/v3yzsmD/fdb-4.png" alt="fdb-4" border="0"></a>

# APIs and JSON

-  Show Python API code definition for request and response using GET, POST, UPDATE methods in VSCode. Discuss algorithmic condition used to direct request to appropriate Python method based on request method.

- Adding the CRUD resource in the backend.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/g9TsKQf/fdb4-5.png" alt="fdb4-5" border="0"></a>

- fetching the memes from the localhost backend with 'get_database'
<a href="https://ibb.co/WK8nDW1"><img src="https://i.ibb.co/bdw1Hgn/fdb-5.png" alt="fdb-5" border="0"></a>

- function for the meme with 'post' and with the JSON utilinzg the base64toImage function.
<a href="https://ibb.co/PWwqPhb"><img src="https://i.ibb.co/my6f2qY/fdb-5-5.png" alt="fdb-5-5" border="0"></a>

-  Show algorithmic conditions used to validate data on a POST condition in VSCode.

- if statement checking the condition 'data['addToHistory]'
<a href="https://ibb.co/v12SDHW"><img src="https://i.ibb.co/G7gqF0D/fdb-6.png" alt="fdb-6" border="0"></a>

-  Show URL request and Body requirements for GET, POST, and UPDATE methods in Postman.

<a href="https://ibb.co/MPS5BYC"><img src="https://i.ibb.co/6DwJX3W/fdb-final.png" alt="fdb-final" border="0"></a>


- Show the JSON response data for 200 success conditions on GET, POST, and UPDATE methods in Postman.
 
<a href="https://imgbb.com/"><img src="https://i.ibb.co/bRtbFS5/fdb-7.png" alt="fdb-7" border="0"></a> 

- Show the JSON response for error for 400 when missing body on a POST request in Postman.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/JtPsYfR/fdb-8.png" alt="fdb-8" border="0"></a>
 
- Show the JSON response for error for 404 when providing an unknown user ID to a UPDATE request in Postman.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/fvHZ4pN/fdb-9.png" alt="fdb-9" border="0"></a>

# Frontend

- My blog of Python API code and use of Postman to request and respond with JSON

-  Show response of JSON objects from fetch of GET, POST, and UPDATE methods in Chrome inspect.

- shows the list of images as a result of the GET, POST, and UPDATE actions:



<a href="https://ibb.co/pQpnhvT"><img src="https://i.ibb.co/r3JvdGh/fdb-10.png" alt="fdb-10" border="0"></a>

- Show a demo (GET) of obtaining an Array of JSON objects that are formatted into the browsers screen in the Chrome browser.

- The displayed gallery of images shows all the images from the backend database

<a href="https://ibb.co/DwSTjp6"><img src="https://i.ibb.co/9yCSdtf/fdb-11.png" alt="fdb-11" border="0"></a>

- Describe fetch and method that obtained the Array of JSON objects in JavaScript code.

- This code shows the fetchDatabase function that fetchs from the api to get the images and eventually get them displayed on the frontend. 
<a href="https://imgbb.com/"><img src="https://i.ibb.co/sHK9cMq/fdb-12.png" alt="fdb-12" border="0"></a>

-  Show code that performs iteration and formatting of data into HTML in JavaScript code.

- The displayImages function shows how the function uses the .forEach to cycle through all the images and display the images on the gallery page.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/zZMgyfY/fdb-13.png" alt="fdb-13" border="0"></a>

- Show a demo (POST or UPDATE) gathering and sending input and receiving a response that show update. Repeat this demo showing both success and failure in the Chrome browser.

- success:

- meme succesfully generated and then will be adde to the frontend gallery.
<a href="https://ibb.co/4KFFNvm"><img src="https://i.ibb.co/XjWWJ02/fdb-14.png" alt="fdb-14" border="0"></a>

- failure:

- if you try to add a file that isn't some sort of image you get an error in the terminal.s
<a href="https://ibb.co/x3QC3jr"><img src="https://i.ibb.co/XVT2VsG/fdb-15.png" alt="fdb-15" border="0"></a>

-  Show and describe code that handles success. Describe how code shows success to the user in the Chrome Browser screen in JavaScript code:

- if succesfull the image goes to the displayImages function which displays the image on the website,.
<a href="https://imgbb.com/"><img src="https://i.ibb.co/9Vyp5Dr/fdb-16.png" alt="fdb-16" border="0"></a>

- Show and describe code that handles failure. Describe how the code shows failure to the user in the Chrome Browser screen in JavaScript code:

- cheking for different errors based off the response status.
<a href="https://imgbb.com/"><img src="https://i.ibb.co/8rGFnYx/fdb-17.png" alt="fdb-17" border="0"></a>

# EXTRA: Algorithm Analysis

- This is my Machine Learning Algorithm Analysis

-  Show algorithms and preparation of data for analysis. This includes cleaning, encoding, and one-hot encoding.

- This is the spliting into the testing and traing parts with the different attributes.

<a href="https://ibb.co/sH4XZCg"><img src="https://i.ibb.co/tX619zH/fdb-18.png" alt="fdb-18" border="0"></a>

<a href="https://ibb.co/MMfYNJy"><img src="https://i.ibb.co/kQJRcPV/fdb-19.png" alt="fdb-19" border="0"></a>

-  Show algorithms and preparation for predictions.
- saving the model files and then predicting it by loading it and making display.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/fnNLpPy/fdb-20.png" alt="fdb-20" border="0"></a>

<a href="https://imgbb.com/"><img src="https://i.ibb.co/HFgfJM7/fdb-21.png" alt="fdb-21" border="0"></a>

-  Discuss concepts and understanding of Linear Regression algorithms.

Linear regression is a method used to understand the relationship between two variables, where one variable (the independent variable) is used to predict the value of another variable (the dependent variable).

Basically prediciting a single model by using a linear relation with that single predition and multiple other factors.

-  Discuss concepts and understanding of Decision Tree analysis algorithms.

A machine learning, a decision tree is a supervised learning algorithm that uses a tree-like model to categorize or predict based on previous questions. The model is trained and tested on data that contains the desired categorization.








