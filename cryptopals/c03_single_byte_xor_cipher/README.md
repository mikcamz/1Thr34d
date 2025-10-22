The explaination is pretty straight forward. BUt there is a miss point

THey don't give us the answer to check if our code is right or not but giving a hint that take the message that have the most english characters.

So here is the plan :

Since Ascii characters only range from 0 to 127 [[https://www.eso.org/~ndelmott/ascii.html]]

we create a loop for guessing from 0 to 127, the we iterate and decrypt the message, then for each message, we evaluate the score by counting the number of alpha characters and take out the message that have highest score
