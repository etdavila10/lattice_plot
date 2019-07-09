# Plot inequalities from lattice points paper

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

############## \mu = n\alpha_1 + m\alpha_2 #####################################
n_input = input('value for n?\n')
m_input = input('value for m?\n')

# elements = input(
# '''Which Weyl Group elements would you like to plot?
# (Type each symbol with a space in between each)
# 0. all elements
# 1. 1
# 2. s_1
# 3. s_2
# 4. s_1s_2
# 5. s_2s_1
# 6. s_1s_2s_1
# 7. s_2s_1s_2
# 8. s_1s_2s_1s_2
# 9. s_2s_1s_2s_1
# a. s_1s_2s_1s_2s_1
# b. s_2s_1s_2s_1s_2
# c. s_1s_2s_1s_2s_1s_2
# ''').split(' ')

n = int(n_input)
m = int(m_input)

# Whether or not you want the grid lines or not
grid = True

# Bounds for the size of the resulting plot
bound = 15

# Conversion from standard basis to our alpha basis
def alpha_axis(xvals,yvals):
    return xvals - (1.5 * yvals), (np.sqrt(3)/2.) * yvals

# element_list = ['1','2','3','4','5','6','7','8','9','a','b','c']
# for element in element_list:
    # elements = [element]
elements = ['0']
plt.figure()
if grid:
    # Creates an array from -50 to 50 with 1000 points in it
    xvals = np.linspace(-70, 70, int(1e3))

    # Creates the lines parallel to alpha_2 axis
    for i in range(-70,70):
        vals = np.zeros(len(xvals))
        vals += i
        line = alpha_axis(vals, xvals)
        plt.plot(line[0], line[1], color='black', linewidth=.8)

    # Creates the lines parallel to alpha_1 axis
    for i in range(-70,70):
        vals = np.zeros(len(xvals))
        vals += i
        line = alpha_axis(xvals,vals)
        plt.plot(line[0], line[1], color='black', linewidth=.8)

    # Drawing the alpha axes
    plt.plot(xvals, np.zeros(len(xvals)), color='black', linewidth=3)
    line = alpha_axis(np.zeros(len(xvals)), xvals)
    plt.plot(line[0], line[1], color='black', linewidth=3)
    plt.text(14.8, 0, r'$\alpha_1$', fontsize=16)
    plt.text(-16.7, 9, r'$\alpha_2$', fontsize=16)
################################################################################

# Transparency
trans = .4
trans_line = .7

# Extras for clean plotting
plt.xlim(-bound - .5, bound - .5)
plt.ylim(-bound - 2.6, bound - 2.6)
plt.axis('off')
plt.gcf().set_size_inches(10,10)

file = 'lattice_{}.png'.format(elements[0])
# plt.savefig(file, dpi=300, bbox_inches='tight')
# print('{} was saved!'.format(file))
plt.show()
