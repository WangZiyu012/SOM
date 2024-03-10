I build the self-organizing map and apply it to a customer data in this repo.

the data is something customer filled in the files

goal: return the people most likely to be fraud(outlayer)

do SOM: do customer segamentation, one of which will be the customers who potentially will cheate.

input: customer data (15 attributes)

BMU: the most similiar neuron to the customer

update: use gausian function to update the weights of the neighbors of the winning neurons to move them closer to the data. we do this step for all the input data.

recursion: repeat the update step, each step the output space decreases and lose dimensions, finally reach a point where the output space stops decreasing.

evaluate whether the neuron is outlayer: compute MID, which has the biggest MID

implementation: split into 2 sets X, Y: all 14 attributes for one, and whether proved for another one..
1dwpwiojdiowdsws

amend