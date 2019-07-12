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

if '1' in elements or '0' in elements:
    # Updated
    ############## Plotting Weyl Group Element 1 ###############################
    # Plotting c_1 - n >= 0
    # (x >= n)
    y_intersect = m
    x_intersect = n

    yvals = np.linspace(y_intersect, 30, int(1e3))
    new_x, new_y = alpha_axis(yvals * 0 + n, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='purple', alpha=trans_line)

    # Plotting c_2 - m >= 0
    # (y >= m)

    xvals = np.linspace(x_intersect, 30, int(1e3))
    new_x, new_y = alpha_axis(xvals, xvals * 0 + m)
    plt.plot(new_x, new_y, linewidth=3, color='purple', alpha=trans_line)

    # # Filling in the region
    point_x1, point_y1 = alpha_axis(n, 90)
    point_x2, point_y2 = alpha_axis(90, 90)
    point_x3, point_y3 = alpha_axis(90, m)
    point_x4, point_y4 = alpha_axis(x_intersect, y_intersect)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'purple', alpha=trans)
    ############################################################################

if '3' in elements or '0' in elements:
    # Updated
    ############## Plotting Weyl Group Element s_2 #############################
    # Plotting c_1 - n >= 0
    # (x >= n)
    x_intersect = n
    y_intersect = n - m - 1

    yvals = np.linspace(y_intersect, -30, int(1e3))
    new_x, new_y = alpha_axis(yvals * 0 + n, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='blue', alpha=trans_line)

    # Plotting c_1 - c_2 - m - 1 >= 0
    # (y <= x - m - 1)

    xvals = np.linspace(x_intersect, 30, int(1e3))
    yvals = xvals - m - 1
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='blue', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(50, 50 - m - 1)
    point_x2, point_y2 = alpha_axis(100, 50)
    point_x3, point_y3 = alpha_axis(x_intersect, -50)
    point_x4, point_y4 = alpha_axis(x_intersect, y_intersect)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'blue', alpha=trans)

    ############################################################################

if '2' in elements or '0' in elements:
    # Updated
    ############## Plotting Weyl Group Element s_1 #############################
    # Plotting c_2 - m >= 0
    # (y >= m)
    intersect = 3 * m - n - 1

    xvals = np.linspace(intersect, -30, int(1e3))
    new_x, new_y = alpha_axis(xvals, xvals * 0 + m)
    plt.plot(new_x, new_y, linewidth=3, color='orange', alpha=trans_line)

    # Plotting -c_1 + 3c_2 - n - 1 >= 0
    # (y <= 1/3 * x + 1/3 * n + 1/3)

    xvals = np.linspace(intersect, 50, int(1e3))
    yvals = (1/3.) * xvals + (1/3.) * n + (1/3.)
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='orange', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(60, (1/3.) * 60 + (1/3.) * n + (1/3.))
    point_x2, point_y2 = alpha_axis(10, 100)
    point_x3, point_y3 = alpha_axis(-50, -50 * 0 + m)
    point_x4, point_y4 = alpha_axis(intersect, intersect * 0 + m)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'orange', alpha=trans)
    ############################################################################

if '4' in elements or '0' in elements:
    # Updated
    ############## Plotting Weyl Group Element s_1s_2 ##########################
    # Plotting c_1 - c_2 - m - 1 >= 0
    # (y <= x - m - 1)
    intersect = 3 * m + 3 - n - 4

    xvals = np.linspace(intersect, -30, int(1e3))
    yvals = xvals - m - 1
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='red', alpha=trans_line)

    # Plotting 2c_1 - 3c_2 - n - 4 >= 0
    # (y <= 2/3 * x - 1/3 * n - 4/3)

    xvals = np.linspace(intersect, 50, int(1e3))
    yvals = (2/3.) * xvals - (1/3.) * n - (4/3.)
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='red', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(-50, -50 - m - 1)
    point_x2, point_y2 = alpha_axis(100, 50)
    point_x3, point_y3 = alpha_axis(50, (2/3.) * 50 - (1/3.) * n - (4/3.))
    point_x4, point_y4 = alpha_axis(intersect, intersect - m - 1)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'red', alpha=trans)
    ############################################################################

if '7' in elements  or '0' in elements:
    # Updated
    ############# Plotting Weyl Group Element s_2s_1s_2 ############################
    # Plotting c_1 - 2c_2 - m - 4 >= 0
    # (y <= (1/2)x - (1/2)m - 2)
    intersect = 2 * n - 3 * m - 4

    xvals = np.linspace(intersect, 50, int(1e3))
    yvals = (1/2.) * xvals - (1/2.) * m - 2
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='olive', alpha=trans_line)

    # Plotting 2c_1 - 3c_2 - n - 4 >= 0
    # (y <= 2/3 * x - 1/3 * n - 4/3)

    xvals = np.linspace(intersect, -50, int(1e3))
    yvals = (2/3.) * xvals - (1/3.) * n - (4/3.)
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='olive', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(100, (1/2.) * 100 - (1/2.) * m - 2)
    point_x2, point_y2 = alpha_axis(100, -50)
    point_x3, point_y3 = alpha_axis(-50, (2/3.) * -50 - (1/3.) * n - (4/3.))
    point_x4, point_y4 = alpha_axis(intersect, (1/2.) * intersect - (1/2.) * m - 2)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'olive', alpha=trans)
    ############################################################################

if '5' in elements or '0' in elements:
    # Updated
    ############## Plotting Weyl Group Element s_2s_1 ##########################
    # Plotting -c_1 + 3c_2 - n - 1 >= 0
    # (y <= 1/3 * x + 1/3 * n + 1/3)
    intersect = 2 * n - 3 * m - 4

    xvals = np.linspace(intersect, -50, int(1e3))
    yvals = (1/3.) * xvals + (1/3.) * n + (1/3.)
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='green', alpha=trans_line)

    # Plotting -c_1 + 2c_2 - m - 2 >= 0
    # (y <= 1/2 * x + 1/2 * m + 1)

    xvals = np.linspace(intersect, 50, int(1e3))
    yvals = (1/2.) * xvals + (1/2.) * m + 1
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='green', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(-50, (1/3.) * -50 + (1/3.) * n + (1/3.))
    point_x2, point_y2 = alpha_axis(-50, 50)
    point_x3, point_y3 = alpha_axis(50, (1/2.) * 50 + (1/2.) * m + 1)
    point_x4, point_y4 = alpha_axis(intersect, (1/2.) * intersect + (1/2.) * m + 1)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'green', alpha=trans)
    ############################################################################

if '6' in elements or '0' in elements:
    # Updated
    ############## Plotting Weyl Group Element s_1s_2s_1 #######################
    # Plotting -c_1 + 2c_2 - m - 2 >= 0
    # (y <= 1/2 * x + 1/2 * m + 1)
    intersect = -2 * n - 12 + 3 * m + 6

    xvals = np.linspace(intersect, -50, int(1e3))
    yvals = (1/2.) * xvals + (1/2.) * m + 1
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='black', alpha=trans_line)

    # Plotting -2c_1 + 3c_2 - 6 - n >= 0
    # (y <= 2/3 * x + 1/3 * n + 2)

    xvals = np.linspace(intersect, 50, int(1e3))
    yvals = (2/3.) * xvals + (1/3.) * n + 2
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='black', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(-50, (1/2.) * -50 + (1/2.) * m + 1)
    point_x2, point_y2 = alpha_axis(-150, -70)
    point_x3, point_y3 = alpha_axis(150, (2/3.) * 150 + (1/3.) * n + 2)
    point_x4, point_y4 = alpha_axis(intersect, (1/2.) * intersect + (1/2.) * m + 1)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'black', alpha=trans)
    ############################################################################

if '9' in elements or '0' in elements:
    # Updated
    ############## Plotting Weyl Group Element s_2s_1s_2s_1 ####################
    # Plotting -c_1 + c_2 - m - 5 >= 0
    # (y <= x + m + 5)
    intersect = n + 6 - 3 * m - 15

    xvals = np.linspace(intersect, 50, int(1e3))
    yvals = xvals + m + 5
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='gold', alpha=trans_line)

    # Plotting -2c_1 + 3c_2 - 6 - n >= 0
    # (y <= 2/3 * x + 1/3 * n + 2)

    xvals = np.linspace(intersect, -50, int(1e3))
    yvals = (2/3.) * xvals + (1/3.) * n + 2
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='gold', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(90, 90 + m + 5)
    point_x2, point_y2 = alpha_axis(-50, 0)
    point_x3, point_y3 = alpha_axis(-150, (2/3.) * -150 + (1/3.) * n + 2)
    point_x4, point_y4 = alpha_axis(intersect, intersect + m + 5)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'gold', alpha=trans)
    ############################################################################

if 'a' in elements or '0' in elements:
    # Updated
    ########### Plotting Weyl Group Element s_1s_2s_1s_2s_1 ####################
    # Plotting -c_1 + c_2 - m - 5 >= 0
    # (y <= x + m + 5)
    x_intersect = -n - 10
    y_intersect = m + 5 - n - 10

    xvals = np.linspace(x_intersect, -50, int(1e3))
    yvals = xvals + m + 5
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='crimson', alpha=trans_line)

    # Plotting -c_1 - n - 10 >= 0
    # (x <= -n - 10)

    yvals = np.linspace(y_intersect, 50, int(1e3))
    new_x, new_y = alpha_axis(yvals * 0 - n - 10, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='crimson', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(- n - 10,50)
    point_x2, point_y2 = alpha_axis(-190, -90)
    point_x3, point_y3 = alpha_axis(-50, (-50) + m + 5)
    point_x4, point_y4 = alpha_axis(x_intersect, y_intersect)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'crimson', alpha=trans)
    ############################################################################

if 'c' in elements or '0' in elements:
    # Updated
    ########### Plotting Weyl Group Element s_1s_2s_1s_2s_1s_2 #################
    # Plotting -c_2 - m - 6 >= 0
    # (y <= -m - 6)
    x_intersect = -n - 10
    y_intersect = - m - 6

    xvals = np.linspace(x_intersect, -50, int(1e3))
    yvals = xvals * 0 - m - 6
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='navy', alpha=trans_line)

    # Plotting -c_1 - n - 10 >= 0
    # (x <= -n - 10)

    yvals = np.linspace(y_intersect, -50, int(1e3))
    new_x, new_y = alpha_axis(yvals * 0 - n - 10, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='navy', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(-50, -m - 6)
    point_x2, point_y2 = alpha_axis(-150, -50)
    point_x3, point_y3 = alpha_axis(-n - 10, -50)
    point_x4, point_y4 = alpha_axis(x_intersect, y_intersect)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'navy', alpha=trans)
    ############################################################################

if 'b' in elements or '0' in elements:
    # Updated
    ########### Plotting Weyl Group Element s_2s_1s_2s_1s_2 ####################
    # Plotting -c_2 - m - 6 >= 0
    # (y <= -m - 6)
    intersect = -3 * m - 18 + n + 9

    xvals = np.linspace(intersect, 50, int(1e3))
    yvals = xvals * 0 - m - 6
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='darkviolet', alpha=trans_line)

    # Plotting c_1 -3c_2 - n - 9 >= 0
    # (y <= (1/3) * x - (1/3) * n - 3)

    xvals = np.linspace(intersect, -50, int(1e3))
    yvals = (1/3.) * xvals - (1/3.) * n - 3
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='darkviolet', alpha=trans_line)

    # Filling in the region
    point_x1, point_y1 = alpha_axis(-100, (1/3.) * -100 - (1/3.) * n - 3)
    point_x2, point_y2 = alpha_axis(50, -50)
    point_x3, point_y3 = alpha_axis(50, 50 * 0 - m - 6)
    point_x4, point_y4 = alpha_axis(intersect, (1/3.) * intersect - (1/3.) * n - 3)

    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'darkviolet', alpha=trans)
    ################################################################################

if '8' in elements or '0' in elements:
    # Updated
    ############ Plotting Weyl Group Element s_1s_2s_1s_2 ##########################
    # Plotting c_1 - 3c_2 - n - 9 >= 0
    # (y <= (1/3) * x - (1/3) * n - 3)
    # Solving for the intersection gives us x = 3 * m + 12 - 2*n - 18
    intersect = 3 * m + 12 - 2*n - 18

    xvals = np.linspace(intersect, 50, int(1e3))
    yvals = (1/3) * xvals - (1/3) * n - 3
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='coral', alpha=trans_line)

    # Plotting c_1 - 2c_2 - m - 4 >= 0
    # (y <= (1/2) * x - (1/2) * m - 2

    xvals = np.linspace(intersect, -70, int(1e3))
    yvals = (1/2.) * xvals - (1/2.) * m - 2
    new_x, new_y = alpha_axis(xvals, yvals)
    plt.plot(new_x, new_y, linewidth=3, color='coral', alpha=trans_line)

    # Filling in the region
    # These points will give me the four point of the rectangle that is being bounded
    # by the two conditions of the Weyl Group Element
    point_x1, point_y1 = alpha_axis(-70, (1/2.) * -70 - (1/2.) * m - 2)
    point_x2, point_y2 = alpha_axis(50, -50)
    point_x3, point_y3 = alpha_axis(50, (1/3) * 50 - (1/3) * n - 3)
    point_x4, point_y4 = alpha_axis(intersect, (1/2. * intersect - (1/2.) * m - 2))

    # Generates the Rectangle and shades in the region
    fill([point_x1, point_x2, point_x3, point_x4],
         [point_y1, point_y2, point_y3, point_y4], 'coral', alpha=trans)
    ################################################################################

# Extras for clean plotting
plt.xlim(-bound - .5, bound - .5)
plt.ylim(-bound - 2.6, bound - 2.6)
plt.axis('off')
plt.gcf().set_size_inches(10,10)

file = 'lattice_{}.png'.format(elements[0])
# plt.savefig(file, dpi=300, bbox_inches='tight')
# print('{} was saved!'.format(file))
plt.show()
