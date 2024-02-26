---
toc: true
comments: true
layout: post
title: Ronit Thomas Tri 2 Individual Review
description: CSP
type: tangibles
courses: { compsci: {week: 3} }
---

# Condensed Project Overview:

We had the idea of creating a meme creator. With the rise of internent in the 21st Century, memes have become more popular than ever and we wanted to provide a way for a user to upload an image of their choice, customize with text, and then get a meme which they can simply download. 

# My Feature:

My feature is a meme gallery that updates when a new meme is added to the database is created and is available to all users to preview and download memes. 

[Link to where I got my Collegboard Requirments](https://apcentral.collegeboard.org/media/pdf/ap-csp-student-task-directions.pdf)


# Component A: Program Code
should specific images of code by added for all?

| Collegeboard Requirements | Me |
|------------------|------------------|
| Instructions for input from one of the following: the user, a device, an online datas stream, a file.  | Our Project takes in an image which is a file along with text from the user in the form of the top and bottom text of their meme.  |
| Use of at least one list (or other collection type) to represent a collectino of data that is stored and used to manage program complexity and help fulfill the users purpose.  | An example of a collection of data that is stored is of the collection of memes on the backend that gets updated when a new memes is made. It helps fulfill our program's purpose because we use the data of all of these memes on the gallery page so users can download any of them. I am storing all collections in and SQLite table and using JSON collection to pass data from frontend to and from the backend|
| At least one procedure that contirubted to the program's intened purpose where you have defined: the name, return type, one or more parameters:  | This procedure has a name(post), a return(response), and parameters(self): <a href="https://ibb.co/pjDPHxs"><img src="https://i.ibb.co/d49cNr3/procedure.png" alt="procedure" border="0"></a>  |
| An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure  | This function shows the sequencing, selection, and iteration through a list of meme images: <a href="https://ibb.co/Zg02DK5"><img src="https://i.ibb.co/3FnRZW2/sequencing.png" alt="sequencing" border="0"></a>  |
| Calls to your student-developed prodcedure:  | calling queryImages: <a href="https://imgbb.com/"><img src="https://i.ibb.co/SnW6Kyf/calling.png" alt="calling" border="0"></a>  |
| Instructions for output (tactile, audible, visual, or ) based on input and program functionality  | This code is the fetch that displays the image based off the users inputted image and top+bottom text: <a href="https://ibb.co/Q8WJmkJ"><img src="https://i.ibb.co/28zFKSF/fetch.png" alt="fetch" border="0"></a>  |




# Component B: Video

[Link to Video](https://drive.google.com/file/d/1ZfDdQ5x0vMFbANHlCg8nE2eyQTTgQG3Z/view?usp=sharing)


| Collegboard Requirements | My Video |
|------------------|------------------|
| Input to program  | Seen in video, uploading meme and entering text  |
| At least one aspect of the functionality of your program| The Gallery functionality which displays the database of memes  |
| Output produced by program:  | The meme being created but more specically for my feature being added into the gallery succesfully.  |
| My video does not have: | any distinguishing information and voice narration  |
| My video is | a .webmb, less than 1 minute in length, less than 30MB in file size.  |