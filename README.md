# Max Triangle Total Test
---

### Total for triangle.txt: 6541 (WRONG!)
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

On undertanding the problem further my next solution was built to consider two lines at the same time.  While of course this solves triangle_test_2 example on avoiding local maximum, for a triangle with a 100 lines it wouldnt work, and actually gave me a lower title.  This leads me onto the idea for my next solution, which would mean I would have to dynamically consider the lines according to whats there, with probably a bottom up, rather than a top down solution that I have here.  Unfortunately with my current level of knowledge I am unable to put together a solution for this, once the challenge is over I fully intend to go and understand this.

### Total time to write solution: 6.5hrs
---

### Total time to run: Av 0.040 secs
---

### How to run

```
python3 max_triangle_total.py <filename of triangle text>
```
##
