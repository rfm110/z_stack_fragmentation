# imports
import os
import numpy as np
from PIL import Image
import scipy.misc
import pandas as pd



import PIL.Image
from skimage import io
# traverse through directories, store TIFF as numpy arrays, find channels

# TODO: Questions for Gordon
# How are we naming channels, just labeling by number?


def readThroughDirectory(mainSource):
    """Read through directory and find TIFF images
       Return dictionary containing TIFF images
    """
    imageDictionary = {}
    for currentLocation, subdirectories, files in os.walk(mainSource):
        if files:
            for image in files:
                if ('.TIF' in image or '.tif' in image):
                    #how to label image?
                    imageCodename = image
                    imageDictionary[imageCodename] = currentLocation

                    # convert to numpy array in new funciton
    print imageDictionary
    return imageDictionary
# TODO: This needs to be formatted properly!


def tiffToNumpyArray(imageDictionary, **kwargs):
    """Convert TIFF image into a numpy array
       Return numpy array and its shape
    """
    # for key, values in imageDictionary.iteritems():
    #     openImage = io.imread(key)
    #     if you don't need pathname, convert dictionary to list
    imageArray = io.imread(imageDictionary)

    print imageArray.shape[0]
    arrayShape = imageArray.shape
    # TODO: this needs to be completed, get help on importing tifffile to PyCharm / adding to anaconda
    return imageArray, arrayShape

def separateChannels(imageArray, arrayShape):
    """Separate z-stacks based on channel (2 total)
       Return the two arrays corresponding to each channel
    """
    # initialize new arrays for the separate channels
    arrayChannel1 = None
    arrayChannel2 = None
    print imageArray.shape

    splitArray = np.split(imageArray, 130, axis=0)

    counter = 0
    # print 'splitArray is', splitArray
    for i in splitArray:
        counter += 1
        if (counter % 2 == 0):
            if (counter == 2):
                arrayChannel2 = i
            else:
                arrayChannel2 = np.concatenate((arrayChannel2, i), axis = 0)
        else:
            if (counter == 1):
                arrayChannel1 = i
            else:
                arrayChannel1 = np.concatenate((arrayChannel1, i), axis = 0)

    # TODO: remove me once tested
    print
    print 'channel 1 array'
    print arrayChannel1.shape
    print "~~~~~~~~~~~~~~~~~~~~~~~~"
    print 'channel 2 array'
    print arrayChannel2.shape
    return arrayChannel1, arrayChannel2

def numpyArrayToTiff(array1, array2):
    # TODO: FIX ME
    # the following is going to cause a lot of problems
    # be more concise/ find better way to name files
    # for now I will name files by myself, while I am testing
    fileName1 = raw_input('What would you like to name the first file? ')
    fileName1 = raw_input('What would you like to name the first file? ')
    byte1 = array1.nbytes
    byt2 = array2.nbytes
    # image1 = Image.fromarray(array1)
    # image2 = Image.fromarray(array2)

    image1 = scipy.misc.imsave('one.tiff', array1)


    return None


def extractZSlice(array1, array2):
    #  if the following is not appropriate, move the two to parameters provided to the function
    channelToExtract = raw_input('Please enter 1 or 2 for the channel you want to extract ')
    levelToExtract = raw_input('Please enter the z stack level to be extracted ')
    if channelToExtract == 1:
        return array1[levelToExtract-1]
    if channelToExtract == 2:
        return array2[levelToExtract-1]


def findIndices(array1):
    # TODO: something to consider, are the z values always even, i mean i would think so but confirm this
    channel = raw_input('Please enter 1 or 2 for channel ')
    availableIndices = []
    totalZSlices = array1.shape[0]
    if channel == 1:
        availableIndices.append(0)
        for i in (2, totalZSlices, 2):
            availableIndices.append(i)
    else:
        for i in (1, totalZSlices, 2):
            availableIndices.append(i)
    print availableIndices
    return availableIndices















    # arrayChannel1 = np.zeros([arrayShape[0], arrayShape[1], arrayShape[2]], dtype = int)
    # print arrayChannel1
    #
    # print arrayChannel1.shape
    # arrayChannel2 = np.zeros(shape = arrayShape)

    # for i in (0, arrayShape[0]):
    #     if (i % 2 == 0):
    #         zSlice = arrayShape[1][i]
    #         print zSlice











def csvWriter():


    """Writes collected data to a csv file"""
    pass

# TODO: convert numpy to tiff

mainSource ='/Users/rubabmalik786/Downloads/W_RR112614_A_R3_S03_008 (1).tif'
imageArray = io.imread(mainSource)
shape = imageArray.shape
# getImages = readThroughDirectory(mainSource)
imageArray, arrayShape = tiffToNumpyArray(mainSource)
array1, array2 = separateChannels(imageArray, arrayShape)
# image1, image2 = numpyArrayToTiff(array1, array2)
ZStackAtParticularLevel = extractZSlice(array1,array2)



