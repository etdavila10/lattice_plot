# lattice_plot_c2.py
# Plotting the Weyl Alternation Diagrams for Lie Algebra c_2

from pylab import *
import matplotlib.pyplot as plt
import numpy as np

############## \mu = n\alpha_1 + m\alpha_2 #####################################
while True:
    n_input = input('value for n?\n(has to be even)\n')
    if int(n_input) % 2 == 0:
        break
    print('Try again\n')

m_input = input('value for m?\n')

n = int(n_input)
m = int(m_input)
################################################################################

############ Conversion from standard basis to omega basis #####################
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

################### Plotting the Grid ##########################################
# CHANGE THIS TO FALSE IF YOU DO NOT WANT THE GRID/AXES LINES
grid = True

plt.figure()
if grid:
    # Creates an array from -50 to 50 with 1000 elements
    xvals = np.linspace(-50, 50, int(1e3))

    # Creates the lines parallel to omega_2 axis
    for i in range(-50,50):
        vals = np.zeros(len(xvals))
        vals += i
        line = omega_axis(vals, xvals)
        plt.plot(line[0], line[1], color='black', linewidth=.8)

    # Creates the lines parallel to omega_1 axis
    for i in range(-50,50):
        vals = np.zeros(len(xvals))
        vals += i
        line = omega_axis(xvals,vals)
        plt.plot(line[0], line[1], color='black', linewidth=.8)

    # Drawing the omega axes
    plt.plot(xvals, np.zeros(len(xvals)), color='black', linewidth=3)
    line = omega_axis(np.zeros(len(xvals)), xvals)
    plt.plot(line[0], line[1], color='black', linewidth=3)

    # Labeling the axes
    plt.text(15.2, -0.2, r'$\omega_1$', fontsize=20)
    plt.text(15.2, 15, r'$\omega_2$', fontsize=20)
################################################################################

# Choosing the size of the markers
size = 10

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
plt.plot(s2_xvals, s2_yvals, 'o', ms=size, c=s2)
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
plt.plot(s1s2_xvals, s1s2_yvals, 'o', ms=size, c=s1s2)
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
plt.plot(s2s1s2_xvals, s2s1s2_yvals, 'o', ms=size, c=s2s1s2)
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
plt.plot(s2s1s2s1_xvals, s2s1s2s1_yvals, 'o', ms=size, c=s2s1s2s1)
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
plt.plot(s1s2s1_xvals, s1s2s1_yvals, 'o', ms=size, c=s1s2s1)
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
plt.plot(s2s1_xvals, s2s1_yvals, 'o', ms=size, c=s2s1)
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
plt.plot(s1_xvals, s1_yvals, 'o', ms=size, c=s1)
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
plt.plot(one_xvals, one_yvals, 'o', ms=size, c=one)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=one_s1)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=one_s2)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s1_s21)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s2_s12)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s21_s121)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s12_s212)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s121_s2121)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s212_s2121)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=one_s1_s21)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=one_s1_s2)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=one_s2_s12)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s2_s12_s212)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s12_s212_s2121)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s212_s2121_s121)
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s2121_s121_s21)
################################################################################

########### Plotting A(\l, \mu) = \{s1, s1s2s1, s2s1} ##########################
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
plt.plot(new_xvals, new_yvals, 'o', ms=size, c=s1_s121_s21)
################################################################################

################################################################################
# Extras for clean plotting
bound = 15
plt.xlim(-bound, bound)
plt.ylim(-bound, bound)
plt.axis('off')
plt.gcf().set_size_inches(10,10)

file = 'images/c2_images/lattice_n{}_m{}.pdf'.format(n, m)
plt.savefig(file, dpi=300, bbox_inches='tight')
print('{} was saved!'.format(file))
plt.show()
