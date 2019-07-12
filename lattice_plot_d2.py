# Plot inequalities from lattice points paper

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

############## \mu = n\alpha_1 + m\alpha_2 #####################################
while True:
    n_input = input('value for n?\n(has to be even)\n')
    if int(n_input) % 2 == 0:
        break
    print('Try again\n')
while True:
    m_input = input('value for m?\n(has to be even)\n')
    if int(m_input) % 2 == 0:
        break
    print('Try again\n')

n = int(n_input)
m = int(m_input)
################################################################################

################################################################################
# Conversion from standard basis to our alpha basis
def omega_axis(xvals,yvals):
    return (1/2. * xvals, 1/2. * yvals)
################################################################################

################################################################################
# CHANGE THIS TO FALSE IF YOU DO NOT WANT THE GRID LINES
grid = True
plt.figure()
if grid:
    # Creates an array from -70 to 70 with 1000 points in it
    xvals = np.linspace(-70, 70, int(1e3))

    # Creates the lines parallel to omega_2 axis
    for i in range(-70,70):
        vals = np.zeros(len(xvals))
        vals += i
        line = omega_axis(vals, xvals)
        plt.plot(line[0], line[1], color='black', linewidth=.8)

    # Creates the lines parallel to omega_1 axis
    for i in range(-70,70):
        vals = np.zeros(len(xvals))
        vals += i
        line = omega_axis(xvals,vals)
        plt.plot(line[0], line[1], color='black', linewidth=.8)

    # Drawing the omega axes
    plt.plot(xvals, np.zeros(len(xvals)), color='black', linewidth=3)
    line = omega_axis(np.zeros(len(xvals)), xvals)
    plt.plot(line[0], line[1], color='black', linewidth=3)
    plt.text(15.1, -.3, r'$\omega_1$', fontsize=20)
    plt.text(-.4, 15.3, r'$\omega_2$', fontsize=20)
################################################################################

# Size of the markers
size = 10

###################### Plotting 1 ##############################################
xvals = np.arange(0,50)
yvals = np.arange(0,50)

one_xvals = []
one_yvals = []

for xval in xvals:
    for yval in yvals:
        if (2 * xval - n)/2. >= 0 and (2 * yval - m)/2. >= 0:
            one_xvals.append(2 * xval)
            one_yvals.append(2 * yval)

one_xvals, one_yvals = omega_axis(np.array(one_xvals), np.array(one_yvals))
plt.plot(one_xvals, one_yvals, 'o', color='red', ms=size)
################################################################################

###################### Plotting s1 #############################################
xvals = np.arange(-50, 0)
yvals = np.arange(0, 50)

s1_xvals = []
s1_yvals = []

for xval in xvals:
    for yval in yvals:
        if (-2 * xval - n - 2)/2. >= 0 and (2 * yval - m)/2. >= 0:
            s1_xvals.append(2 * xval)
            s1_yvals.append(2 * yval)

s1_xvals, s1_yvals = omega_axis(np.array(s1_xvals), np.array(s1_yvals))
plt.plot(s1_xvals, s1_yvals, 'o', color='blue', ms=size)
################################################################################

###################### Plotting s2 #############################################
xvals = np.arange(0, 50)
yvals = np.arange(-50, 0)

s2_xvals = []
s2_yvals = []

for xval in xvals:
    for yval in yvals:
        if (2 * xval - n)/2. >= 0 and (-2 * yval - m - 2)/2. >= 0:
            s2_xvals.append(2 * xval)
            s2_yvals.append(2 * yval)

s2_xvals, s2_yvals = omega_axis(np.array(s2_xvals), np.array(s2_yvals))
plt.plot(s2_xvals, s2_yvals, 'o', color='green', ms=size)
################################################################################

###################### Plotting s2s1 ###########################################
xvals = np.arange(-50, 0)
yvals = np.arange(-50, 0)

s2s1_xvals = []
s2s1_yvals = []

for xval in xvals:
    for yval in yvals:
        if (-2 * xval - n - 2)/2. >= 0 and (-2 * yval - m - 2)/2. >= 0:
            s2s1_xvals.append(2 * xval)
            s2s1_yvals.append(2 * yval)

s2s1_xvals, s2s1_yvals = omega_axis(np.array(s2s1_xvals), np.array(s2s1_yvals))
plt.plot(s2s1_xvals, s2s1_yvals, 'o', color='brown', ms=size)
################################################################################

# Bounds for the size of the resulting plot
bound = 15
# Extras for clean plotting
plt.xlim(-bound, bound)
plt.ylim(-bound, bound)
plt.axis('off')
plt.gcf().set_size_inches(10,10)

file = 'images/d2_images/lattice_n{}_m{}.pdf'.format(n, m)
plt.savefig(file, dpi=300, bbox_inches='tight')
print('{} was saved!'.format(file))
plt.show()
