# stroop_task_python
Stroop task with Python

# Introduction
In psychology, the Stroop effect is the delay in reaction time between congruent and
incongruent stimuli. The effect has been used to create a psychological test (the Stroop test) that
is widely used in clinical practice and investigation.

A basic task that demonstrates this effect occurs when there is a mismatch between the name of a
color (e.g., "blue", "green", or "red") and the color it is printed on (i.e., the word "red" printed in
blue ink instead of red ink). When asked to name the color of the word it takes longer and is
more prone to errors when the color of the ink does not match the name of the color.

- Congruent (Compatible): The color of the word and the meaning is the same
- Incongruent (Incompatible): The color of the word and the meaning is different

You can read more in the above [pdf file](./stroop_task.pdf).

### The detail of the task
- The task requires button presses.
- There are 40 trials.
- Each stimulus is presented for 500 milliseconds.
- Participants should respond with type {‘g’, ‘b’, ‘y’, ‘r’} letters for {green, blue, yellow, red} colors respectively.
- After each trial you should show the ‘correct’ and ‘wrong’ feedback to the participants.
- At the end of the task, you should show feedback about participants’ response times in the compatible and incompatible condition.
- The Stroop effect is reported as the average response time in incompatible trials minus compatible trials.
- You need to collect this information for your data analysis.
1. name of the word (e.g., "yellow")
2. the color the word is printed in (e.g., "red")
3. Stroop color match (1=compatible, 0=incompatible)
4. the pressed key
5. Status (1=correct, 2=wrong, 3=timeout)
6. Response time (milliseconds)

### Your Output should be as the following:
- Your speed in correct trials:
- Congruent: ? ms
- Incongruent: ? ms
- Your Stroop effect is congruent minus congruent: ? ms

# Requirements and Running
Install the required packages using the requirements.txt file:
```
pip3 install requirements.txt
```
You can run the code via the above [py file](./stroop_task.py).

# Acknowledgments

**Reference:**
https://www.psytoolkit.org/experiment-library/stroop.html

**Demo:**
https://www.psytoolkit.org/experiment-library/experiment_stroop.html

# Author

**Developed** by [Farrokh Karimi](https://farrokhkarimi.github.io/)
