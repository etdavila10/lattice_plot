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

# Transparency
trans = 1
size = 100

# Choosing Colors for each section

one = 'brown'
s1 = 'orange'
s2 = 'yellow'
s2s1 = 'maroon'
s1s2 = 'cyan'
s1s2s1 = 'magenta'
s2s1s2 = 'red'
s2s1s2s1 = 'aquamarine'

one_s1 = 'crimson'
one_s2 = 'pink'
s1_s21 = 'limegreen'
s2_s12 = 'greenyellow'
s21_s121 = 'blue'
s12_s212 = 'fuchsia'
s121_s2121 = 'gold'
s212_s2121 = 'dodgerblue'

one_s1_s21 = 'turquoise'
one_s1_s2 = 'violet'
one_s2_s12 = 'green'
s2_s12_s212 = 'darkorange'
s12_s212_s2121 = 'navy'
s212_s2121_s121 = 'mediumaquamarine'
s2121_s121_s21 = 'mediumslateblue'
s1_s121_s21 = 'orangered'

################### Plotting s_2 ###############################################
xvals = np.arange(0, 50)
yvals = np.arange(-40, 40)

s2_xvals = []
s2_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_2 conditions
        if l_1(xval, yval) >= 0 and l_4(xval, yval) >= 0:
            s2_xvals.append(2*xval)
            s2_yvals.append(yval)

s2_xvals, s2_yvals = omega_axis(np.array(s2_xvals), np.array(s2_yvals))
plt.scatter(s2_xvals, s2_yvals, s=size, c=s2)
################################################################################

################### Plotting s_1s_2 ############################################
xvals = np.arange(0, 50)
yvals = np.arange(-25, 0)

s1s2_xvals = []
s1s2_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_1s_2 conditions
        if l_6(xval, yval) >= 0 and l_4(xval, yval) >= 0:
            s1s2_xvals.append(2 * xval)
            s1s2_yvals.append(yval)

s1s2_xvals, s1s2_yvals = omega_axis(np.array(s1s2_xvals), np.array(s1s2_yvals))
plt.scatter(s1s2_xvals, s1s2_yvals, s=size, c=s1s2)
################################################################################

################### Plotting s_2s_1s_2 #########################################
xvals = np.arange(-20, 50)
yvals = np.arange(-25, 0)

s2s1s2_xvals = []
s2s1s2_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_2s_1s_2 conditions
        if l_6(xval, yval) >= 0 and l_8(xval, yval) >= 0:
            s2s1s2_xvals.append(2*xval)
            s2s1s2_yvals.append(yval)

s2s1s2_xvals, s2s1s2_yvals = omega_axis(np.array(s2s1s2_xvals), np.array(s2s1s2_yvals))
plt.scatter(s2s1s2_xvals, s2s1s2_yvals,s=size, c=s2s1s2)
################################################################################

################### Plotting s_2s_1s_2s_1 ######################################
xvals = np.arange(-40, 40)
yvals = np.arange(-50, 40)

s2s1s2s1_xvals = []
s2s1s2s1_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_2s_1s_2s_1 conditions
        if l_7(xval, yval) >= 0 and l_8(xval, yval) >= 0:
            s2s1s2s1_xvals.append(2 * xval)
            s2s1s2s1_yvals.append(yval)

s2s1s2s1_xvals, s2s1s2s1_yvals = omega_axis(np.array(s2s1s2s1_xvals), np.array(s2s1s2s1_yvals))
plt.scatter(s2s1s2s1_xvals, s2s1s2s1_yvals, s=size, c=s2s1s2s1)
################################################################################

################### Plotting s_1s_2s_1 #########################################
xvals = np.arange(-40, 40)
yvals = np.arange(-50, 40)

s1s2s1_xvals = []
s1s2s1_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_1s_2s_1 conditions
        if l_7(xval, yval) >= 0 and l_5(xval, yval) >= 0:
            s1s2s1_xvals.append(2 * xval)
            s1s2s1_yvals.append(yval)

s1s2s1_xvals, s1s2s1_yvals = omega_axis(np.array(s1s2s1_xvals), np.array(s1s2s1_yvals))
plt.scatter(s1s2s1_xvals, s1s2s1_yvals, s=size, c=s1s2s1)
################################################################################

################### Plotting s_2s_1 #########################################
xvals = np.arange(-40, 40)
yvals = np.arange(-50, 40)

s2s1_xvals = []
s2s1_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_2s_1 conditions
        if l_3(xval, yval) >= 0 and l_5(xval, yval) >= 0:
            s2s1_xvals.append(2 * xval)
            s2s1_yvals.append(yval)

s2s1_xvals, s2s1_yvals = omega_axis(np.array(s2s1_xvals), np.array(s2s1_yvals))
plt.scatter(s2s1_xvals, s2s1_yvals, s=size, c=s2s1)
################################################################################

################### Plotting s_1 #########################################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

s1_xvals = []
s1_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_1 conditions
        if l_3(xval, yval) >= 0 and l_2(xval, yval) >= 0:
            s1_xvals.append(2 * xval)
            s1_yvals.append(yval)

s1_xvals, s1_yvals = omega_axis(np.array(s1_xvals), np.array(s1_yvals))
plt.scatter(s1_xvals, s1_yvals, s=size, c=s1)
################################################################################

################### Plotting one #########################################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

one_xvals = []
one_yvals = []

for xval in xvals:
    for yval in yvals:
        # one conditions
        if l_1(xval, yval) >= 0 and l_2(xval, yval) >= 0:
            one_xvals.append(2 * xval)
            one_yvals.append(yval)

one_xvals, one_yvals = omega_axis(np.array(one_xvals), np.array(one_yvals))
plt.scatter(one_xvals, one_yvals, s=size, c=one)
################################################################################

########### Plotting A(\l, \mu) = \{one, s1\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_1(xval, yval) >= 0 and l_3(xval, yval) >= 0 and \
            l_4(xval, yval) < 0 and l_5(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=one_s1)
################################################################################

########### Plotting A(\l, \mu) = \{one, s2\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_2(xval, yval) >= 0 and l_4(xval, yval) >= 0 and \
            l_3(xval, yval) < 0 and l_6(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=one_s2)
################################################################################

########### Plotting A(\l, \mu) = \{s1, s21\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_2(xval, yval) >= 0 and l_5(xval, yval) >= 0 and \
            l_1(xval, yval) < 0 and l_7(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s1_s21)
################################################################################

########### Plotting A(\l, \mu) = \{s2, s12\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_1(xval, yval) >= 0 and l_6(xval, yval) >= 0 and \
            l_2(xval, yval) < 0 and l_8(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s2_s12)
################################################################################

########### Plotting A(\l, \mu) = \{s21, s121\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_3(xval, yval) >= 0 and l_7(xval, yval) >= 0 and \
            l_2(xval, yval) < 0 and l_8(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s21_s121)
################################################################################

########### Plotting A(\l, \mu) = \{s12, s212\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_4(xval, yval) >= 0 and l_8(xval, yval) >= 0 and \
            l_1(xval, yval) < 0 and l_7(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s12_s212)
################################################################################

########### Plotting A(\l, \mu) = \{s121, s2121\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_5(xval, yval) >= 0 and l_8(xval, yval) >= 0 and \
            l_6(xval, yval) < 0 and l_3(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s121_s2121)
################################################################################

########### Plotting A(\l, \mu) = \{s212, s2121\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_6(xval, yval) >= 0 and l_7(xval, yval) >= 0 and \
            l_5(xval, yval) < 0 and l_4(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s212_s2121)
################################################################################

########### Plotting A(\l, \mu) = \{one, s1, s2s1\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_1(xval, yval) >= 0 and l_5(xval, yval) >= 0 and \
            l_4(xval, yval) < 0 and l_7(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=one_s1_s21)
################################################################################

########### Plotting A(\l, \mu) = \{one, s1, s2\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_3(xval, yval) >= 0 and l_4(xval, yval) >= 0 and \
            l_5(xval, yval) < 0 and l_6(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=one_s1_s2)
################################################################################

########### Plotting A(\l, \mu) = \{one, s2, s1s2\} ############################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_2(xval, yval) >= 0 and l_6(xval, yval) >= 0 and \
            l_3(xval, yval) < 0 and l_8(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=one_s2_s12)
################################################################################

########### Plotting A(\l, \mu) = \{s2, s1s2, s2s1s2} ##########################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_1(xval, yval) >= 0 and l_8(xval, yval) >= 0 and \
            l_2(xval, yval) < 0 and l_7(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s2_s12_s212)
################################################################################

########### Plotting A(\l, \mu) = \{s1s2, s2s1s2, s2s1s2s1} ####################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_7(xval, yval) >= 0 and l_4(xval, yval) >= 0 and \
            l_5(xval, yval) < 0 and l_1(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s12_s212_s2121)
################################################################################

########### Plotting A(\l, \mu) = \{s2s1s2, s2s1s2s1, s1s2s1} ##################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_6(xval, yval) >= 0 and l_5(xval, yval) >= 0 and \
            l_4(xval, yval) < 0 and l_3(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s212_s2121_s121)
################################################################################

########### Plotting A(\l, \mu) = \{s2s1s2s1, s1s2s1, s2s1} ##################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_3(xval, yval) >= 0 and l_8(xval, yval) >= 0 and \
            l_2(xval, yval) < 0 and l_6(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s2121_s121_s21)
################################################################################

########### Plotting A(\l, \mu) = \{s1, s1s2s1, s2s1} ##################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

new_xvals = []
new_yvals = []

for xval in xvals:
    for yval in yvals:
        conditions = l_7(xval, yval) >= 0 and l_2(xval, yval) >= 0 and \
            l_8(xval, yval) < 0 and l_1(xval, yval) < 0

        if conditions:
            new_xvals.append(2 * xval)
            new_yvals.append(yval)

new_xvals, new_yvals = omega_axis(np.array(new_xvals), np.array(new_yvals))
plt.scatter(new_xvals, new_yvals, s=size, c=s1_s121_s21)
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
