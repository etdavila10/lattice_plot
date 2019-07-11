# Plot inequalities from lattice points paper

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

############## \mu = n\alpha_1 + m\alpha_2 #####################################
# n_input = input('value for n?\n')
# m_input = input('value for m?\n')

n = 0 #int(n_input)
m = 0 #int(m_input)

# Whether or not you want the grid lines or not
grid = True

# Bounds for the size of the resulting plot
bound = 15

# Conversion from standard basis to our alpha basis
def omega_axis(xvals,yvals):
    return (np.sqrt(2)/2.) * xvals + (np.sqrt(2)/2. * yvals), (np.sqrt(2)/2.) * yvals

################################################################################

######### inequality names based off paper #####################################

l_1 = lambda x, y: 2 * x + y - n - m
l_2 = lambda x, y: (2 * x - n)/2. + y - m
l_3 = lambda x, y: y - n - m - 1
l_4 = lambda x, y: (2 * x - n)/2. - m - 1
l_5 = lambda x, y: (-2 * x - n)/2. - m - 2
l_6 = lambda x, y: -y - n - m - 3
l_7 = lambda x, y: -2 * x - y - n - m - 4
l_8 = lambda x, y: (-2 * x - n)/2. - y - m - 3

################################################################################

plt.figure()
if grid:
    # Creates an array from -70 to 70 with 1000 points in it
    xvals = np.linspace(-70, 70, int(1e3))

    # Creates the lines parallel to omega_2 axis
    for i in range(-70,70):
        vals = np.zeros(len(xvals))
        vals += i
        line = omega_axis(vals, xvals)
        plt.plot(line[0], line[1], color='black', linewidth=.8, alpha=.5)

    # Creates the lines parallel to omega_1 axis
    for i in range(-70,70):
        vals = np.zeros(len(xvals))
        vals += i
        line = omega_axis(xvals,vals)
        plt.plot(line[0], line[1], color='black', linewidth=.8, alpha=.5)

    # Drawing the omega axes
    plt.plot(xvals, np.zeros(len(xvals)), color='black', linewidth=3)
    line = omega_axis(np.zeros(len(xvals)), xvals)
    plt.plot(line[0], line[1], color='black', linewidth=3)
    # plt.text(14.8, 0, r'$\alpha_1$', fontsize=16)
    # plt.text(-16.7, 9, r'$\alpha_2$', fontsize=16)
################################################################################

# Extras for clean plotting
plt.xlim(-bound, bound)
plt.ylim(-bound, bound)
plt.axis('off')
plt.gcf().set_size_inches(10,10)

# file = 'lattice_{}.png'.format(elements[0])
# plt.savefig(file, dpi=300, bbox_inches='tight')
# print('{} was saved!'.format(file))
plt.show()
