# Sparse Matrix Operator
## Programming Assignment 2: Sparse Matrix
### Task Description: 
Using any programming language of your choice.
1. Load two sparse matrices from an input file.
2. Perform addition, subtraction, and multiplication on the matrices.


## Features
Loads two sparse matrices from an input file
performs addition
performs subtraction
performs multiplication
depending on what operation you want to perform

## Requirements
Python compiler (interpreter): depending on your machine's specifications, python or python3 is required for this program.
Use python --version to check the version of python on your machine.

## How to Use

## Installation

You'll need to go ahead and clone the project repository from Github. This will contain the simple shell program and all of its dependencies.

```
git clone https://github.com/yusufmolumo/DSA-HW02---Sparse-Matrix.git
```
After cloning the repo, navigate using the absolute path: dsa/hw02/code/src/
using this as the argument to the cd command, in the src directory lies the program.

This is still a demo, so all input files to be handled by the program must be in the same directory as the program source file, which is the src directory.

To compile and run the program, run the following command in your terminal:
python(3) -u <program_file-name>
The python interpreter you use is dependent on the version installed on your machine; for me, this will look like this:
python3 -u [SparseMatrix.py]

Pls note that square brackets won't be used when running the program, this has been included for emphatic basis.

## Example

Say we have an input file easy_sample_input_02.txt with the following content:

rows=1
cols=2
(0, 1, 3)
(0, 2, 4)

and another file, easy_sample_input_03.txt with the following content:

rows=1
cols=2
(0, 1, 5)
(0, 2, 10)

run the program:
python(3) -u SparseMatrix.py 
It prompts you to enter the file name of the first and second files
'path to file'

## Output
*addition*
rows=1
cols=2
(0, 1, 8)
(0, 2, 14)

*subtraction*
rows=1
cols=2
(0, 1, -2)
(0, 1, -6)

*multiplication*
In this case, multiplication is not feasible as the value for cols for the first matrix is not equal to the value for rows in the second matrix.

I have given you an output example; however, depending on the operation you chose, it would ask you to name your file or, if no name is given, store the info using a default file name.

## Handling Different Input Scenarios
### Whitespace Handling:
Lines with only whitespace characters are skipped
Leading and trailing whitespaces around integers are ignored.

### Empty Lines:
Lines that are empty or contain only whitespace are skipped.


# Author
Yusuf Molumo <y.molumo@alustudent.com>
