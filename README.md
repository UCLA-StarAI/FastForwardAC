# FastForwardAC
A Python Program (v3.5) to output a feed-forward AC to find marginal probabilities

## Directories
**src**: Python code to run the program

**ac**: Sample .ac files used for testing

**test_bench**: Contains tests used to compare performance

## Source code
**ac_to_ac.py**: Outputs a feed-forward AC from an AC
**forward_c.py**: Outputs a C file to calculate marginals from a feed-forward AC
**ac_to_c_code.py**: (Slower code) Outputs C code to calculate marginars from an AC

## Running the Code
The program was written for Python 3.x. To be safe, specify that you are running python3. 

You can run the program in this format: 
> python3 (name of python program) (name of .ac file) 

If the .ac file is not specified, the program will prompt you for a name during runtime.

### example: Finding marginals for the first node in verysimple.ac
> python3 ac_to_ac.py verysimple.ac

As the program runs, you will be prompted to enter a node index. This corresponds to the line number of the node in the original .ac file.
> Find marginal of leaf node index: 0 

The program will generate an .ac file that calculates the partial derivative of node index 0 (first node in file). 

To calculate the value of this partial derivative, run the forward_c.py file
> python3 forward_c.py out.ac
