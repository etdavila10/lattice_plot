# lattice_plot_b2.py
# Plotting the Weyl Alternation Diagrams for Lie Algebra b_2

from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import os, sys

######### Checking for files in the directory ##################################
os.chdir(sys.path[0])

if (not os.path.isdir('images')):
    os.mkdir('images')
if (not os.path.isdir('images/b2_images')):
    os.mkdir('images/b2_images')
################################################################################

############## \mu = n\alpha_1 + m\alpha_2 #####################################
n_input = input('value for n?\n')

while True:
    m_input = input('value for m?\n(has to be even)\n')
    if int(m_input) % 2 == 0:
        break
    print('Try again\n')

n = int(n_input)
m = int(m_input)
################################################################################

############ Conversion from standard basis to omega basis #####################
def omega_axis(x, y):
    return (np.sqrt(2)/2.) * x + (np.sqrt(2)/2. * y), (np.sqrt(2)/2.) * x
################################################################################

######### inequality names based off paper #####################################

j_1 = lambda x, y: (2 * y - m)/2. + x - n
j_2 = lambda x, y: x + 2 * y - n - m
j_3 = lambda x, y: (2 * y - m)/2. - n - 1
j_4 = lambda x, y: x - n - m - 1
j_5 = lambda x, y: -x - n - m - 3.
j_6 = lambda x, y: (-2 * y - m)/2. - n - 2.
j_7 = lambda x, y: (-2 * y - m)/2. - x - n - 3
j_8 = lambda x, y: -x - 2 * y - n - m - 4
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
        plt.plot(line[0], line[1], color='black', linewidth=.8, alpha=.4)

    # Creates the lines parallel to omega_1 axis
    for i in range(-50,50):
        vals = np.zeros(len(xvals))
        vals += i
        line = omega_axis(xvals,vals)
        plt.plot(line[0], line[1], color='black', linewidth=.8, alpha=.4)

    # Drawing the omega axes
    line = omega_axis(xvals, np.zeros(len(xvals)))
    plt.plot(line[0], line[1], color='black', linewidth=2)
    line = omega_axis(np.zeros(len(xvals)), xvals)
    plt.plot(line[0], line[1], color='black', linewidth=2)

    # Labeling the axes
    plt.text(15.2, -0.2, r'$\omega_2$', fontsize=20)
    plt.text(15.2, 15, r'$\omega_1$', fontsize=20)
################################################################################

# Choosing the size of the markers
size = 10

# Choosing Colors for each section

one = 'brown'
s1 = 'orange'
s2 = 'yellow'
s2s1 = 'maroon'
s1s2 = 'cyan'
s1s2s1 = 'gray'
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

################# Plotting s_2 ###############################################
xvals = np.arange(-50, 50)
yvals = np.arange(-40, 40)

s2_xvals = []
s2_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_2 conditions
        if j_1(xval, yval) >= 0 and j_4(xval, yval) >= 0:
            s2_xvals.append(xval)
            s2_yvals.append(2*yval)

s2_xvals, s2_yvals = omega_axis(np.array(s2_xvals), np.array(s2_yvals))
plt.plot(s2_xvals, s2_yvals, 'o', ms=size, c=s2)
##############################################################################

################## Plotting s_1s_2 ############################################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

s1s2_xvals = []
s1s2_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_1s_2 conditions
        if j_6(xval, yval) >= 0 and j_4(xval, yval) >= 0:
            s1s2_xvals.append(xval)
            s1s2_yvals.append(2*yval)

s1s2_xvals, s1s2_yvals = omega_axis(np.array(s1s2_xvals), np.array(s1s2_yvals))
plt.plot(s1s2_xvals, s1s2_yvals, 'o', ms=size, c=s1s2)
###############################################################################

################### Plotting s_2s_1s_2 #########################################
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

s2s1s2_xvals = []
s2s1s2_yvals = []

for xval in xvals:
    for yval in yvals:
        # s_2s_1s_2 conditions
        if j_6(xval, yval) >= 0 and j_8(xval, yval) >= 0:
            s2s1s2_xvals.append(xval)
            s2s1s2_yvals.append(2*yval)

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
        if j_7(xval, yval) >= 0 and j_8(xval, yval) >= 0:
            s2s1s2s1_xvals.append(xval)
            s2s1s2s1_yvals.append(2*yval)

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
        if j_7(xval, yval) >= 0 and j_5(xval, yval) >= 0:
            s1s2s1_xvals.append(xval)
            s1s2s1_yvals.append(2*yval)

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
        if j_3(xval, yval) >= 0 and j_5(xval, yval) >= 0:
            s2s1_xvals.append(xval)
            s2s1_yvals.append(2*yval)

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
        if j_3(xval, yval) >= 0 and j_2(xval, yval) >= 0:
            s1_xvals.append(xval)
            s1_yvals.append(2*yval)

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
        if j_1(xval, yval) >= 0 and j_2(xval, yval) >= 0:
            one_xvals.append(xval)
            one_yvals.append(2*yval)

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
        conditions = j_1(xval, yval) >= 0 and j_3(xval, yval) >= 0 and \
            j_4(xval, yval) < 0 and j_5(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_2(xval, yval) >= 0 and j_4(xval, yval) >= 0 and \
            j_3(xval, yval) < 0 and j_6(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_2(xval, yval) >= 0 and j_5(xval, yval) >= 0 and \
            j_1(xval, yval) < 0 and j_7(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_1(xval, yval) >= 0 and j_6(xval, yval) >= 0 and \
            j_2(xval, yval) < 0 and j_8(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_3(xval, yval) >= 0 and j_7(xval, yval) >= 0 and \
            j_2(xval, yval) < 0 and j_8(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_4(xval, yval) >= 0 and j_8(xval, yval) >= 0 and \
            j_1(xval, yval) < 0 and j_7(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_5(xval, yval) >= 0 and j_8(xval, yval) >= 0 and \
            j_6(xval, yval) < 0 and j_3(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_6(xval, yval) >= 0 and j_7(xval, yval) >= 0 and \
            j_5(xval, yval) < 0 and j_4(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_1(xval, yval) >= 0 and j_5(xval, yval) >= 0 and \
            j_4(xval, yval) < 0 and j_7(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_3(xval, yval) >= 0 and j_4(xval, yval) >= 0 and \
            j_5(xval, yval) < 0 and j_6(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_2(xval, yval) >= 0 and j_6(xval, yval) >= 0 and \
            j_3(xval, yval) < 0 and j_8(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_1(xval, yval) >= 0 and j_8(xval, yval) >= 0 and \
            j_2(xval, yval) < 0 and j_7(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_7(xval, yval) >= 0 and j_4(xval, yval) >= 0 and \
            j_5(xval, yval) < 0 and j_1(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_6(xval, yval) >= 0 and j_5(xval, yval) >= 0 and \
            j_4(xval, yval) < 0 and j_3(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_3(xval, yval) >= 0 and j_8(xval, yval) >= 0 and \
            j_2(xval, yval) < 0 and j_6(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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
        conditions = j_7(xval, yval) >= 0 and j_2(xval, yval) >= 0 and \
            j_8(xval, yval) < 0 and j_1(xval, yval) < 0

        if conditions:
            new_xvals.append(xval)
            new_yvals.append(2*yval)

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

################################################################################
# Saving the images
file = 'images/b2_images/lattice_n{}_m{}.pdf'.format(n, m)
plt.savefig(file, dpi=300, bbox_inches='tight')
print('{} was saved!'.format(file))
plt.show()
