# lattice_plot_g2_dots.py
# Plotting the Weyl Alternation Diagrams for Lie Algebra g_2

import matplotlib.pyplot as plt
import numpy as np
import os, sys

######### Checking for files in the directory ##################################
os.chdir(sys.path[0])

if (not os.path.isdir('images')):
    os.mkdir('images')
if (not os.path.isdir('images/g2_images')):
    os.mkdir('images/g2_images')
################################################################################

############## \mu = n\alpha_1 + m\alpha_2 #####################################
n_input = input('value for n?\n')
m_input = input('value for m?\n')

n = int(n_input)
m = int(m_input)

# Whether or not you want the grid lines or not
grid = True

# Bounds for the size of the resulting plot
bound = 10

# Conversion from standard basis to our alpha basis
def alpha_axis(xvals,yvals):
    return xvals - (1.5 * yvals), (np.sqrt(3)/2.) * yvals

plt.figure()
if grid:
    # Creates an array from -50 to 50 with 1000 points in it
    xvals = np.linspace(-70, 70, int(1e3))

    # Creates the lines parallel to alpha_2 axis
    for i in range(-70,70):
        vals = np.zeros(len(xvals))
        vals += i
        line = alpha_axis(vals, xvals)
        plt.plot(line[0], line[1], color='black', linewidth=.8, alpha=.4)

    # Creates the lines parallel to alpha_1 axis
    for i in range(-70,70):
        vals = np.zeros(len(xvals))
        vals += i
        line = alpha_axis(xvals,vals)
        plt.plot(line[0], line[1], color='black', linewidth=.8, alpha=.4)

    # Drawing the alpha axes
    plt.plot(xvals, np.zeros(len(xvals)), color='black', linewidth=2)
    line = alpha_axis(np.zeros(len(xvals)), xvals)
    plt.plot(line[0], line[1], color='black', linewidth=2)
    plt.text(14.8, 0, r'$\alpha_1$', fontsize=20)
    plt.text(-16.7, 9, r'$\alpha_2$', fontsize=20)
################################################################################

k_1 = lambda x, y: x - n
k_2 = lambda x, y: y - m
k_3 = lambda x, y: -1*x + 3*y - n - 1
k_4 = lambda x, y: x - y - m - 1
k_5 = lambda x, y: 2*x - 3*y - n - 4
k_6 = lambda x, y: -1*x + 2*y - m - 2
k_7 = lambda x, y: -1*x - n - 10
k_8 = lambda x, y: -1*y - m - 6
k_9 = lambda x, y: x - 3 * y - n - 9
k_10 = lambda x, y: -1*x + y - m - 5
k_11 = lambda x, y: -2 * x + 3 * y - n - 6
k_12 = lambda x, y: x - 2*y - m - 4

# Transparency
trans = .6
trans_line = .7

# Since the points are transparent we must have a solid white background for each point

xvals = np.arange(-50, 50)
yvals = np.arange(-50, 50)

bg_xvals = []
bg_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_1(xval,yval) >= 0 and k_2(xval,yval) >= 0 or \
           k_3(xval,yval) >= 0 and k_2(xval,yval) >= 0 or \
           k_1(xval,yval) >= 0 and k_4(xval,yval) >= 0 or \
           k_4(xval,yval) >= 0 and k_5(xval,yval) >= 0 or \
           k_3(xval,yval) >= 0 and k_6(xval,yval) >= 0 or \
           k_11(xval,yval) >= 0 and k_6(xval,yval) >= 0 or \
           k_5(xval,yval) >= 0 and k_12(xval,yval) >= 0 or \
           k_9(xval,yval) >= 0 and k_12(xval,yval) >= 0 or \
           k_11(xval,yval) >= 0 and k_10(xval,yval) >= 0 or \
           k_7(xval,yval) >= 0 and k_10(xval,yval) >= 0 or \
           k_9(xval,yval) >= 0 and k_8(xval,yval) >= 0 or \
           k_7(xval,yval) >= 0 and k_8(xval,yval) >= 0:
            bg_xvals.append(xval)
            bg_yvals.append(yval)

bg_xvals, bg_yvals = alpha_axis(np.array(bg_xvals), np.array(bg_yvals))
plt.plot(bg_xvals, bg_yvals, 'o', ms=10, c='white')

############## Plotting Weyl Group Element 1 ###############################
# Plotting c_1 - n >= 0
# (x >= n)

xvals = np.arange(-30, 50)
yvals = np.arange(-30, 30)

one_xvals = []
one_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_1(xval, yval) >= 0 and k_2(xval, yval) >= 0:
            one_xvals.append(xval)
            one_yvals.append(yval)

one_xvals, one_yvals = alpha_axis(np.array(one_xvals), np.array(one_yvals))
plt.plot(one_xvals, one_yvals, 'o', ms=10, c='purple', alpha=trans)

############################################################################

############## Plotting Weyl Group Element s_2 #############################
# Plotting c_1 - n >= 0 and c_1 - c_2 - m - 1 >= 0

xvals = np.arange(-30, 50)
yvals = np.arange(-30, 30)

s2_xvals = []
s2_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_1(xval, yval) >= 0 and k_4(xval, yval) >= 0:
            s2_xvals.append(xval)
            s2_yvals.append(yval)

s2_xvals, s2_yvals = alpha_axis(np.array(s2_xvals), np.array(s2_yvals))
plt.plot(s2_xvals, s2_yvals, 'o', ms=10, c='blue', alpha=trans)

############################################################################

############## Plotting Weyl Group Element s_1 #############################
# Plotting c_2 - m >= 0
# (y >= m)
# Plotting -c_1 + 3c_2 - n - 1 >= 0
# (y <= 1/3 * x + 1/3 * n + 1/3)

xvals = np.arange(-30, 50)
yvals = np.arange(-30, 30)

s1_xvals = []
s1_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_3(xval, yval) >= 0 and k_2(xval, yval) >= 0:
            s1_xvals.append(xval)
            s1_yvals.append(yval)

s1_xvals, s1_yvals = alpha_axis(np.array(s1_xvals), np.array(s1_yvals))
plt.plot(s1_xvals, s1_yvals, 'o', ms=10, c='orange', alpha=trans)
############################################################################

############## Plotting Weyl Group Element s_1s_2 ##########################
# Plotting c_1 - c_2 - m - 1 >= 0
# (y <= x - m - 1)
# Plotting 2c_1 - 3c_2 - n - 4 >= 0
# (y <= 2/3 * x - 1/3 * n - 4/3)

xvals = np.arange(-30, 50)
yvals = np.arange(-30, 30)

s1s2_xvals = []
s1s2_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_4(xval, yval) >= 0 and k_5(xval, yval) >= 0:
            s1s2_xvals.append(xval)
            s1s2_yvals.append(yval)

s1s2_xvals, s1s2_yvals = alpha_axis(np.array(s1s2_xvals), np.array(s1s2_yvals))
plt.plot(s1s2_xvals, s1s2_yvals, 'o', ms=10, c='red', alpha=trans)

############################################################################

############# Plotting Weyl Group Element s_2s_1s_2 ############################
# Plotting c_1 - 2c_2 - m - 4 >= 0
# (y <= (1/2)x - (1/2)m - 2)
# Plotting 2c_1 - 3c_2 - n - 4 >= 0
# (y <= 2/3 * x - 1/3 * n - 4/3)
xvals = np.arange(-30, 50)
yvals = np.arange(-30, 30)

s2s1s2_xvals = []
s2s1s2_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_5(xval, yval) >= 0 and k_12(xval, yval) >= 0:
            s2s1s2_xvals.append(xval)
            s2s1s2_yvals.append(yval)

s2s1s2_xvals, s2s1s2_yvals = alpha_axis(np.array(s2s1s2_xvals), np.array(s2s1s2_yvals))
plt.plot(s2s1s2_xvals, s2s1s2_yvals, 'o', ms=10, c='olive', alpha=trans)

############################################################################


############## Plotting Weyl Group Element s_2s_1 ##########################
# Plotting -c_1 + 3c_2 - n - 1 >= 0
# (y <= 1/3 * x + 1/3 * n + 1/3)
# Plotting -c_1 + 2c_2 - m - 2 >= 0
# (y <= 1/2 * x + 1/2 * m + 1)

xvals = np.arange(-30, 50)
yvals = np.arange(-30, 30)

s2s1_xvals = []
s2s1_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_3(xval, yval) >= 0 and k_6(xval, yval) >= 0:
            s2s1_xvals.append(xval)
            s2s1_yvals.append(yval)

s2s1_xvals, s2s1_yvals = alpha_axis(np.array(s2s1_xvals), np.array(s2s1_yvals))
plt.plot(s2s1_xvals, s2s1_yvals, 'o', ms=10, c='green', alpha=trans)
############################################################################

############## Plotting Weyl Group Element s_1s_2s_1 #######################
# Plotting -c_1 + 2c_2 - m - 2 >= 0
# (y <= 1/2 * x + 1/2 * m + 1)
# Plotting -2c_1 + 3c_2 - 6 - n >= 0
# (y <= 2/3 * x + 1/3 * n + 2)
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 30)

s1s2s1_xvals = []
s1s2s1_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_11(xval, yval) >= 0 and k_6(xval, yval) >= 0:
            s1s2s1_xvals.append(xval)
            s1s2s1_yvals.append(yval)

s1s2s1_xvals, s1s2s1_yvals = alpha_axis(np.array(s1s2s1_xvals), np.array(s1s2s1_yvals))
plt.plot(s1s2s1_xvals, s1s2s1_yvals, 'o', ms=10, c='black', alpha=trans)

############################################################################

############## Plotting Weyl Group Element s_2s_1s_2s_1 ####################
# Plotting -c_1 + c_2 - m - 5 >= 0
# (y <= x + m + 5)

# Plotting -2c_1 + 3c_2 - 6 - n >= 0
# (y <= 2/3 * x + 1/3 * n + 2)
xvals = np.arange(-50, 50)
yvals = np.arange(-50, 30)

s2s1s2s1_xvals = []
s2s1s2s1_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_11(xval, yval) >= 0 and k_10(xval, yval) >= 0:
            s2s1s2s1_xvals.append(xval)
            s2s1s2s1_yvals.append(yval)

s2s1s2s1_xvals, s2s1s2s1_yvals = alpha_axis(np.array(s2s1s2s1_xvals), np.array(s2s1s2s1_yvals))
plt.plot(s2s1s2s1_xvals, s2s1s2s1_yvals, 'o', ms=10, c='gold', alpha=trans)

############################################################################


########### Plotting Weyl Group Element s_1s_2s_1s_2s_1 ####################
# Plotting -c_1 + c_2 - m - 5 >= 0
# (y <= x + m + 5)
# Plotting -c_1 - n - 10 >= 0
# (x <= -n - 10)

xvals = np.arange(-50, 50)
yvals = np.arange(-50, 30)

s1s2s1s2s1_xvals = []
s1s2s1s2s1_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_7(xval, yval) >= 0 and k_10(xval, yval) >= 0:
            s1s2s1s2s1_xvals.append(xval)
            s1s2s1s2s1_yvals.append(yval)

s1s2s1s2s1_xvals, s1s2s1s2s1_yvals = alpha_axis(np.array(s1s2s1s2s1_xvals), np.array(s1s2s1s2s1_yvals))
plt.plot(s1s2s1s2s1_xvals, s1s2s1s2s1_yvals, 'o', ms=10, c='crimson', alpha=trans)

############################################################################

########### Plotting Weyl Group Element s_1s_2s_1s_2s_1s_2 #################
# Plotting -c_2 - m - 6 >= 0
# (y <= -m - 6)

# Plotting -c_1 - n - 10 >= 0
# (x <= -n - 10)

xvals = np.arange(-50, 50)
yvals = np.arange(-50, 30)

s1s2s1s2s1s2_xvals = []
s1s2s1s2s1s2_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_7(xval, yval) >= 0 and k_8(xval, yval) >= 0:
            s1s2s1s2s1s2_xvals.append(xval)
            s1s2s1s2s1s2_yvals.append(yval)

s1s2s1s2s1s2_xvals, s1s2s1s2s1s2_yvals = alpha_axis(np.array(s1s2s1s2s1s2_xvals), np.array(s1s2s1s2s1s2_yvals))
plt.plot(s1s2s1s2s1s2_xvals, s1s2s1s2s1s2_yvals, 'o', ms=10, c='navy', alpha=trans)
############################################################################

########### Plotting Weyl Group Element s_2s_1s_2s_1s_2 ####################
# Plotting -c_2 - m - 6 >= 0
# (y <= -m - 6)

# Plotting c_1 -3c_2 - n - 9 >= 0
# (y <= (1/3) * x - (1/3) * n - 3)

xvals = np.arange(-50, 50)
yvals = np.arange(-50, 30)

s2s1s2s1s2_xvals = []
s2s1s2s1s2_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_9(xval, yval) >= 0 and k_8(xval, yval) >= 0:
            s2s1s2s1s2_xvals.append(xval)
            s2s1s2s1s2_yvals.append(yval)

s2s1s2s1s2_xvals, s2s1s2s1s2_yvals = alpha_axis(np.array(s2s1s2s1s2_xvals), np.array(s2s1s2s1s2_yvals))
plt.plot(s2s1s2s1s2_xvals, s2s1s2s1s2_yvals, 'o', ms=10, c='darkviolet', alpha=trans)

################################################################################

############ Plotting Weyl Group Element s_1s_2s_1s_2 ##########################
# Plotting c_1 - 3c_2 - n - 9 >= 0
# (y <= (1/3) * x - (1/3) * n - 3)

# Plotting c_1 - 2c_2 - m - 4 >= 0
# (y <= (1/2) * x - (1/2) * m - 2

xvals = np.arange(-50, 50)
yvals = np.arange(-50, 30)

s1s2s1s2_xvals = []
s1s2s1s2_yvals = []

for xval in xvals:
    for yval in yvals:
        if k_9(xval, yval) >= 0 and k_12(xval, yval) >= 0:
            s1s2s1s2_xvals.append(xval)
            s1s2s1s2_yvals.append(yval)

s1s2s1s2_xvals, s1s2s1s2_yvals = alpha_axis(np.array(s1s2s1s2_xvals), np.array(s1s2s1s2_yvals))
plt.plot(s1s2s1s2_xvals, s1s2s1s2_yvals, 'o', ms=10, c='coral', alpha=trans)

################################################################################

# Extras for clean plotting
plt.xlim(-bound - .5, bound - .5)
plt.ylim(-bound - 2.6, bound - 2.6)
plt.axis('off')
plt.gcf().set_size_inches(10,10)

file = 'images/g2_images/lattice_n{}_m{}.pdf'.format(n, m)
plt.savefig(file, dpi=300, bbox_inches='tight')
print('{} was saved!'.format(file))
plt.show()
