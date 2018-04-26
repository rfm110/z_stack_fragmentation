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