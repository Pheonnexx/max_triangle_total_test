# Max Triangle Total Test
---

### Total for triangle.txt: 7319
---

### Outline of approach
---
My testing experience always makes me read through something more than once.  On the second or third read through I had realised that when moving down the line you were only able to take the max number from the same or adjacent indexes.  This is were the complexity of the challenge was.

My code ideas always start on the nearest notepad I have to hand.  So after bullet pointing the challenge I wrote how I would initially structure my response in pseudo code.

Rather than write the whole thing in one go I follow a step by step approach making sure that I get each bit, from reading the file, to splitting the lines up into a list of integers, return what I am expecting.

*One particular sticking point about the challenge is when I go through each item in a line_list, I would rather just select using my index_range, but I simply couldn't get it to set the index correctly afterwards without resorting to google.  After an hour I moved on.

Testing was done with smaller example provided (triangle_test.txt)

and a secondary example of how to avoid local maximum (triangle_test_2.txt)

edit:

On the second attempt of getting this right, I felt that to avoid the local maximum issue I should looking two steps ahead rather than one.  Looking at the four possibilities of the initial line and then its next children would produce.

*This issue had to be solved to move on to the current solution, after a couple hours break I solved it almost immediately much to my delight.

### Total time to write solution: 4.5hrs
---

### Total time to run: Av 0.040 secs
---

### How to run

```
python3 max_triangle_total.py <filename of triangle text>
```
##