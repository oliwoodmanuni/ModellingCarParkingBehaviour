import matplotlib.pyplot as plt
from car_arrivals_data_analysis import car_arrivals
from CarParkModel import model
import numpy as np

capacity = 100 # number of cars in each car park

arrival_time = 5 # time in which the cars arrive across
data_poisson = car_arrivals(capacity, arrival_time)


num_runs = 100 # number of times to run program

time = [] # variable to append values too


for i in range(0, num_runs):

    a = 0.01 * i
    b = (1-a)/3


    time_to_park, spaces, avg_time_to_park, road_save, flow_rate = model(capacity, data_poisson, [b, b, b, a], 20, 6)


    time = np.append(time, avg_time_to_park)

# Plotting
plt.figure(1)
plt.plot(time)
plt.ylabel('Mean time taken to park ($T_p$) (s)')
plt.xlabel('Proportion of Eloy Users (%)')
plt.title('How mean waiting time varies with increasing\nproportion of Eloy users')
plt.savefig('FlowRate')
plt.show()

