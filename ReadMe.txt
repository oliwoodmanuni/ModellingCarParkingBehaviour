!READ ME!

Dear user,

There are three python files in the GitHub:
	1) CarParkModel.py
	2) car_arrivals_data_analysis.py
	3) CarParkAnalysis.py

1 & 2 are both called by 3. For this reason, you need to download all the files but only edit 'CarParkAnalysis.py'.

When CarParkAnalysis.py is run, from CarParkModel.py it pulls:
	1) time_to_park - time taken for each car to park
	2) spaces - where each car is parked
	3) avg_time_to_park - the average time it has taken all the cars in the car park to park 
	4) flow_rate - the average flow rate within the car park

In CarParkModel.py the function is written as so:

	'def model(Capacity, data_poisson, ratio, end_zone, time_parking)'

Giving 5 parameters that can be varied within CarParkAnalysis.py:
	1) Capacity  - number of cars in the car park
	2) data_poisson - calculated from the number of cars in the car park and the arrival time
	3) ratio - ratio of each driver type represented as [x, y, z, a], where the sum of the ratios should equal to 1
		a) x = first free space
		b) y = end parking
		c) z = random
		d) a = eloy
	4) end_zone - the amount of the end zone that `EC` drivers aim for (this is calculated by 100/end_zone)
	5) time_parking - time taken to park in the bay in time steps (1 time step equals 2 seconds)

Along with 2 additional parameters within the CarParkAnalysis.py file:
	1) num_runs - number of times the simulation will run (the number of car parks tested on)
	2) arrival_time - the period within which all the cars arrive

An example of how to use the code is saved within the 'CarParkAnalysis.py' file with comments. 

The code is designed to be edited by changing the parameters and storing the outputs which can be used for graphs.

Thank you for reading :)
