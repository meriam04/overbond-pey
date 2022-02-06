# Overview
This is my solution to the overbond-eng-test for PEY. The goal was to produce a scatter plot out of an unstructured data input. 

### Disclaimer
I did not have time for automated testing, but I would have liked to run tests against the sample file and ensured that the output values matched the expected ones.

## Before Running the Code
This solution was implemented in Python, so Python should be installed in order to run it. In the case that Python is not installed, here is a link to install it:
https://www.python.org/downloads/

Additionally, the visualization was done using the MatPlotLib library. In the case that this is not already installed, please install is using the instructions here: https://matplotlib.org/stable/users/installing/index.html 

## To Run the Code
The input is designed to be a csv file, currently implemented with 'sample-input.csv' in line 16 of the code as shown below. 
  
```with open('sample-input.csv', 'r') as csvfile: ```

In order to change the input, change the path to the file in the code to be path of the desired input file. 

## The Output
The output should be a plot with the x axis as dates related to Issuance Date, and the y axis corresponds to the numerical values of either the Clean Bid, Clean Ask, or Last Price. Here is a sample plot that was produced on the given sample input: 
![sample-plot](https://user-images.githubusercontent.com/81719754/152703594-ac6b896d-3a9c-4fe7-82c2-0895e7aa6822.png)
