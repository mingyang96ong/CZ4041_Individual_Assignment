<h1>CZ4041 Machine Learning Individual Programming Exercise</h1>

<h3>Task: </h3> Implement Naive Estimator (Probability Density) <strong>without external library</strong>.

Create the 'naiveEst.py' that reads training data from 'data.txt' and generate estimated probability density of the corresponding data instance in 'data.txt' which would be stored into 'output.txt'.

<hr style = 'height: 1px;'>

<h5>Format of data.txt</h5>

The first line shows the meta information of the dataset, where n is the number of data instances, and m is the number of features or dimensions of each data instance (n and m are separated by a comma).

Starting from the 2nd row to the (n+1)<sup>th</sup> row, each row represents a data instance of m features. The m feature values of each instance are separated by space.

Example of data.txt:

n,m

X<sub>11</sub> X<sub>12</sub> ... X<sub>1m</sub>

X<sub>21</sub> X<sub>22</sub> ... X<sub>2m</sub>

...    ...   ...  ...

X<sub>n1</sub> X<sub>n2</sub> ... X<sub>nm</sub>

<hr style = 'height: 1px;'>

<h5>Format of output.txt</h5>

The format of the output file “output.txt” contains n row with each row representing estimated probability density of the corresponding data instance in “data.txt”.

Example of output.txt:

P<sub>1</sub>

P<sub>2</sub>

...

P<sub>n</sub>

<hr style = 'height: 1px;'>

<h5>Important Note</h5>

'data.txt' and 'output.txt' are assumed to be generated in the <strong>same folder</strong> of the source file, naiveEst.py. 

You are <strong>not allowed</strong> to use any <strong> external libraries </strong>.

You may refer to the 'data.txt' and 'output (expected).txt' file for the format of these two files and evaluate the results with the 'output (expected).txt'.

I have included the implementation with numpy library v1.174.