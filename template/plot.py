#!/usr/bin/python
# -*- encoding: utf-8 -*-

import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

data1 = random.randn(1000).cumsum()
data2 = random.randn(1000).cumsum()
data3 = random.randn(1000).cumsum()


fig = plt.figure()
ax = fig.add_subplot(2, 3, 1)
ax.set_title('Graph Title')
ax.set_xlabel('time[sec]')
ax.set_ylabel('yscore')
plt.plot(data1, 'k--', label='data1')
plt.plot(data2, 'ro-', label='data2')
ax.legend(loc='lower left')
ax_ = ax.twinx()
ax_.set_ylabel('y\'score')
plt.plot(data3, 'b+-', label='data3')
ax_.legend(loc='upper right')

plt.savefig('output.png')
plt.show()
