# FastForwardAC
A Python Program (in v.3.5) to output a feed-forward AC to find marginals

## Contents
**src**: Python code to run the program

**ac**: Sample .ac files used for testing

## Running the Code
The program was written in Python 3.x. To be safe, specify that you are running python3. 

You can run the program in this format: 
> python3 (name of python program) (name of .ac file) 

If the .ac file is not specified, the program will prompt you for a name during runtime.

### example: Finding marginals for the first node in verysimple.ac
> python3 ac_to_ac.py verysimple.ac

As the program runs, you will be prompted to enter a node index. This corresponds to the line number of the node in the original .ac file.
> Find marginal of leaf node index: 0 

The program will generate an .ac file that calculates the partial derivative of node index 0 (first node in file). 
