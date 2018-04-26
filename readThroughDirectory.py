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

                    # convert to numpy array in new function
    print imageDictionary
    return imageDictionary