import pandas as pd

df = pd.DataFrame({
    'FCFS': [44.87, 91.59, 122.603],
    'SJF':  [33.29, 65.98, 88.09],
    'RR 2': [51.16, 114.11, 156.876],
    'RR 5': [52.29, 114.415, 156.453]
}, index = [5, 10, 15])

plot = df.plot()
#plot = df.plot(y='FCFS')
#plot = df.plot(y='SJF')
#plot = df.plot(y='RR 2')
#plot = df.plot(y='RR 5')
plot.set_xlabel('Number of jobs')
plot.set_ylabel('Mean of Average Turnaround Time')