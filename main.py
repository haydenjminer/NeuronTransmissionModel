
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

full_time = np.linspace(0,1, 1001)
def brain_signal_f(x):
    return np.where(
        x < 0.1,
        0,
        np.minimum(1, (x-0.1)/0.3)
    )


def spikes_and_contractions(times):
    spike_count = 0
    last_spike = -np.inf
    muscle_contractions = 0
    for t in times:
        absolute_refractory_time = 0.002
        relative_refractory_time = 0.005
        membrane_threshold_a = 0.5
        membrane_threshold_b = 0.75
        signal = brain_signal_f(t)
        spike = False
        if t - last_spike > absolute_refractory_time and signal > membrane_threshold_b:
            spike = True
            spike_count += 1
            last_spike = t
        elif t - last_spike > relative_refractory_time and signal > membrane_threshold_a:
            spike = True
            spike_count += 1
            last_spike = t
        else:
            spike = False

        if spike:
            muscle_contractions += 1

    return muscle_contractions

isp = np.array_split(full_time,10)

def midpoint_interval(interval):
    return (interval[0]+interval[-1])/2

x_intervals = [midpoint_interval(isp[0]), midpoint_interval(isp[1]), midpoint_interval(isp[2]),
               midpoint_interval(isp[3]), midpoint_interval(isp[4]), midpoint_interval(isp[5]),
               midpoint_interval(isp[6]), midpoint_interval(isp[7]), midpoint_interval(isp[8]),
               midpoint_interval(isp[9])]

contractions = [spikes_and_contractions(isp[0]), spikes_and_contractions(isp[1]), spikes_and_contractions(isp[2]),
                spikes_and_contractions(isp[3]), spikes_and_contractions(isp[4]), spikes_and_contractions(isp[5]),
                spikes_and_contractions(isp[6]), spikes_and_contractions(isp[7]), spikes_and_contractions(isp[8]),
                spikes_and_contractions(isp[9])]


plt.bar(x_intervals, contractions, width=0.085,)
plt.xlabel("Time Intervals: 10 0.1 Second Intervals")
plt.ylabel("Contractions")
plt.show()































