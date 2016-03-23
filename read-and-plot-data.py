# read_and_plot_data.py
#
# This program reads an input file, splits the input into separate variables and
# plots the input data
#
# dwhipp - 23.3.2016

# Import NumPy
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Open and read input file
    # FIX 1 - Make this skip over reading in the header row of text
    data = np.loadtxt(fname='Coutand2014_AFT_ages.txt', delimiter=',')

    # Fill in arrays using slices of data
    # FIX 2 - Replace the zeros with some part of the data array
    longitude = 0 
    latitude = 0
    elevation = 0
    observed_age = 0
    std_dev = 0
    predicted_age = 0

    # Calculate goodness of fit
    # FIX 3 - Make this loop go over all of the ages that were read in
    for age in range(1):
        # FIX 4 - Make the code calculate the misfit value here
        print("This is broken")

    # FIX 5 - Make the code plot the predicted and observed ages on the same
    # plot as a function of their latitude

    # Plot measured ages with errorbars
    plt.errorbar(1,1)
    # Plot predicted ages
    plt.plot(1,1)
    # FIX 6 - Add axis labels and a title
    # Display plot
    plt.show()

main()
