# File name: model_client_small.py
# This file is used to test the model deployment. It sends a request to the model server and prints the response.
# The tests in this file represent a small workload.

import requests

t1 = "I like salads."
t2 = "Hello world."
t3 = "The quick brown fox jumps over the lazy dog."
t4 = "She sells seashells by the seashore."
t5 = "The sun is shining and the birds are singing."
t6 = "The cat in the hat is wearing a red and white striped hat."
t7 = "The sky is blue and the grass is green."
t8 = '"The quick brown fox jumps over the lazy dog" is a pangram that contains all the letters of the English alphabet.'
t9 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
t10 = "City of stars, are you shining just for me?"
t11 = "The early bird catches the worm."
t12 = "I scream, you scream, we all scream for ice cream!"
t13 = "The pen is mightier than the sword."
t14 = "A picture is worth a thousand words."
t15 = "When in Rome, do as the Romans do."
t16 = "An apple a day keeps the doctor away."
t17 = "You can't judge a book by its cover."
t18 = "Actions speak louder than words."
t19 = "All's fair in love and war."
t20 = "Beauty is in the eye of the beholder."
t21 = "The grass is always greener on the other side."
t22 = "The customer is always right."
t23 = "Don't judge a man until you have walked a mile in his shoes."
t24 = "Honesty is the best policy."
t25 = "If at first you don't succeed, try, try again."
t26 = "Laughter is the best medicine."
t27 = "Life is like a box of chocolates; you never know what you're going to get."
t28 = "Money can't buy happiness."
t29 = "Practice makes perfect."
t30 = "There's no place like home."
t31 = "The early bird gets the worm."
t32 = "I'm on top of the world!"
t33 = "It's raining cats and dogs outside."
t34 = "Life is too short to waste time on things that don't matter."
t35 = "Love conquers all."
t36 = "Nothing ventured, nothing gained."
t37 = "One man's trash is another man's treasure."
t38 = "The proof of the pudding is in the eating."
t39 = "There's no such thing as a free lunch."
t40 = "Time heals all wounds."

r1 = requests.post("http://127.0.0.1:8000/", json=t1)
print(r1.text)

r2 = requests.post("http://127.0.0.1:8000/", json=t2)
print(r2.text)

r3 = requests.post("http://127.0.0.1:8000/", json=t3)
print(r3.text)

r4 = requests.post("http://127.0.0.1:8000/", json=t4)
print(r4.text)

r5 = requests.post("http://127.0.0.1:8000/", json=t5)
print(r5.text)

r6 = requests.post("http://127.0.0.1:8000/", json=t6)
print(r6.text)

r7 = requests.post("http://127.0.0.1:8000/", json=t7)
print(r7.text)

r8 = requests.post("http://127.0.0.1:8000/", json=t8)
print(r8.text)

r9 = requests.post("http://127.0.0.1:8000/", json=t9)
print(r9.text)

r10 = requests.post("http://127.0.0.1:8000/", json=t10)
print(r10.text)

r11 = requests.post("http://127.0.0.1:8000/", json=t11)
print(r11.text)

r12 = requests.post("http://127.0.0.1:8000/", json=t12)
print(r12.text)

r13 = requests.post("http://127.0.0.1:8000/", json=t13)
print(r13.text)

r14 = requests.post("http://127.0.0.1:8000/", json=t14)
print(r14.text)

r15 = requests.post("http://127.0.0.1:8000/", json=t15)
print(r15.text)

r16 = requests.post("http://127.0.0.1:8000/", json=t16)
print(r16.text)

r17 = requests.post("http://127.0.0.1:8000/", json=t17)
print(r17.text)

r18 = requests.post("http://127.0.0.1:8000/", json=t18)
print(r18.text)

r19 = requests.post("http://127.0.0.1:8000/", json=t19)
print(r19.text)

r20 = requests.post("http://127.0.0.1:8000/", json=t20)
print(r20.text)

r21 = requests.post("http://127.0.0.1:8000/", json=t21)
print(r21.text)

r22 = requests.post("http://127.0.0.1:8000/", json=t22)
print(r22.text)

r23 = requests.post("http://127.0.0.1:8000/", json=t23)
print(r23.text)

r24 = requests.post("http://127.0.0.1:8000/", json=t24)
print(r24.text)

r25 = requests.post("http://127.0.0.1:8000/", json=t25)
print(r25.text)

r26 = requests.post("http://127.0.0.1:8000/", json=t26)
print(r26.text)

r27 = requests.post("http://127.0.0.1:8000/", json=t27)
print(r27.text)

r28 = requests.post("http://127.0.0.1:8000/", json=t28)
print(r28.text)

r29 = requests.post("http://127.0.0.1:8000/", json=t29)
print(r29.text)

r30 = requests.post("http://127.0.0.1:8000/", json=t30)
print(r30.text)

r31 = requests.post("http://127.0.0.1:8000/", json=t31)
print(r31.text)

r32 = requests.post("http://127.0.0.1:8000/", json=t32)
print(r32.text)

r33 = requests.post("http://127.0.0.1:8000/", json=t33)
print(r33.text)

r34 = requests.post("http://127.0.0.1:8000/", json=t34)
print(r34.text)

r35 = requests.post("http://127.0.0.1:8000/", json=t35)
print(r35.text)

r36 = requests.post("http://127.0.0.1:8000/", json=t36)
print(r36.text)

r37 = requests.post("http://127.0.0.1:8000/", json=t37)
print(r37.text)

r38 = requests.post("http://127.0.0.1:8000/", json=t38)
print(r38.text)

r39 = requests.post("http://127.0.0.1:8000/", json=t39)
print(r39.text)

r40 = requests.post("http://127.0.0.1:8000/", json=t40)
print(r40.text)