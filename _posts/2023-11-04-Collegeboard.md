---
toc: true
comments: true
layout: post
title: Second Collegeboard MC relfection
description: Second Collegeboard MC relfection
type: tangibles
courses: { compsci: {week: 9} }
---

[link to incorrect questions](https://apclassroom.collegeboard.org/103/assessments/results/55303670/performance)

## Learning Journey.
In preparation for taking this Collegeboard Practice MC I focused my review on the team teaching topics that we covered this trimester. These topics include, The Internet, Routing, Computing, Beneficial and Harmful Effects, Digital Divide, Computing Bias, Undecided Problems, Crowdsourcing, Legal and Ethical Concerns, Safe Computing. I went over the given team teach lessons for all these topics and re-did the popcorn asks and made a point to read all of the given information. I also reviewd the homework we did for all of these topics to make sure I was prepared. After reviewing for a while I was prepared and took the MC.

## Reflection
Overall I feel good about my results for the MC. I was able to answer the majority of the questions correctly and a lot of the questions I got wrong were simply because of my own small mistakes. For the next time (and to get ready for the actual AP test) I need to make sure to read the questions more carefully because sometimes I miss given details in the problems or opitions. I also need to practice the robot problems. I find them easy but I waste a lot of time on them so I need to be more efficient. Now having taken this test and identified my weakness I need to make sure to review these concepts to be better prepared for next time.

## Question 1
Question: Consider the following program. Which of the following expressions represents the value stored in the variable x as a result of executing the program?


Selected Answer: A
Correct Answer: C

Explanation: My answers works only if the loop header was 3 times. Option C is the correct answers because it correctly shows the x-value being set to 2 and then being multipled my 3 4 times. It's multipled 4 times becuase the for loop that the x3 is set in is set to repeat 4 times in total.

## Question 6
Question: The question below uses a robot in a grid of squares. The robot is represented as a triangle, which is initially in the bottom left square of the grid and facing right.The following programs are each intended to move the robot to the gray square. Program II uses the procedure GoalReached, which returns true if the robot is in the gray square and returns false otherwise.Which of the following statements best describes the correctness of the programs?


Selected Answer: B 
Correct Answer: C

Explanation: My answer of B is incorrect becuase Program 1 also gets the robot to the correct square by moving forward, rotating left, forward twice again, then rotating right. Because this method works Program 1 also works making B invalid.  Hence because Program 1 works and Program 2 also works, Option C is the only answer that accounts for both being correct. 
## Question 11
Question:A color in a computing application is represented by an RGB triplet that describes the amount of red, green, and blue, respectively, used to create the desired color. A selection of colors and their corresponding RGB triplets are shown in the following table. Each value is represented in decimal (base 10).According to information in the table, what color is represented by the binary RGB triplet (11111111, 11111111, 11110000) ?


Selected Answer: B
Correct Answer:A
Explanation: The color would not be light yellow because yewllow has a different RGB triplet of (11111111, 11111111, 11100000).11111111 is 255 (Twice) and 11110000 is equal to 240. The only color that matches this is Option A.

## Question 15
Question: Consider the two programs below. Which of the following best compares the values displayed by programs A and B?

Selected Answer: C
Correct Answer: A
Explanation: Program A and Program displaying the same number of values but different values is incorrect. While i is different in both programs A prints i while incrementing it's value while B continuously prints i. The correct opition is that program A and B display identical in the same order because of the outputs being the same 1 2 3 4 5 6 7 8 9 10.


## Question 23
Question: A flowchart is a way to visually represent an algorithm. The flowchart below is used by an application to set the Boolean variable available to true under certain conditions. The flowchart uses the Boolean variable weekday and the integer variable miles. Which of the following statements is equivalent to the algorithm in the flowchart?

Selected Answer: B
Correct Answer: D
Explanation: B is incorrect because hte expression that is true whenever weekday is true and miles is at least of over 20. This algorithm requires both conditions to be true for the overall thing to be true. Opition D is correct it correcrly sets it true when weekday is true and miles is less than 20. If both of these are not true then the overall thing is set to false. This code line correctly shows this.

## Question 42
Question:A programmer wants to determine whether a score is within 10 points of a given target. For example, if the target is 50, then the scores 40, 44, 50, 58, and 60 are all within 10 points of the target, while 38 and 61 are not.Which of the following Boolean expressions will evaluate to true if and only if score is within 10 points of target ?

Selected Answer: A
Correct Answer: D
Explanation: According to collegeboard, "Incorrect. This Boolean expression does not work as intended. For example, if score is 44 and target is 50, then (score ≤ target + 10) evaluates to true and (target + 10 ≤ score) evaluates to false. Therefore this Boolean expression will evaluate to false when it should evaluate to true." and its correct bceause "This Boolean expression is true if and only if score is between target - 10 and target + 10, inclusive. Therefore, it evaluates to true if and only if score is in the desired range."



## Question 45
Question: Consider a game in which a player flips a fair coin three times. If all three coin flips have the same result (either all heads or all tails) the player wins. Otherwise, the player loses.Which of the following code segments best simulates the behavior of the game?

Selected Answer: B
Correct Answer:C

Explanation: Answer B is incorrect because the variable is either 1 2 3 or 4 so the player according to the code would win about every 2 out of 4 timess. (0 or 3). D is correct beucase in this code the three coins are simulated by 1 and 0. If the sum is either 0 or 3 (all wins or all losses) then the player wins. 

## Question 52
Question:A biologist wrote a program to simulate the population of a sample of bacteria. The program uses the following procedures.
Code for the simulation is shown below.Which of the following are true statements about the simulation?

Selected Answer: B
Correct Answer: A

Explanation: II is incorrect beacause the simulation does not display Which of the following are true statements about the simulation? Option I is correct because the simulations continues until either 24 hours pass of the population reaches 0. 

## Question 67
Question: The procedure NumOccurrences is intended to count and return the number of times targetWord appears in the list wordList. The procedure does not work as intended.For which of the following code segments will the call to NumOccurrences NOT return the intended value?

Selected Answer: B
Correct Answer: A, B

Explanation: B is correct because for the code segment given the count is increasted to 1 but reset to 0 when the code moves to the next list element. This would mean 0 would be returned instead of 1. In A count becomes 1 when "birch" is found. However it breaks the code bevcause the 1 gets reset to 0 when the code segmenent moves to the next list element it's 0. Therefore A is just as correct as B.
