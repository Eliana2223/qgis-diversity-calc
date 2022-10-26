import math

def dc_summarizePoly(poly, lyrPoint, fldSpecies):
    ##############################################
    #
    #     This function takes as inputs the following parameters:
    #          poly       = a single polygon QgsFeature
    #          lyrPoint   = a QgsVectorLayer containing points. Each
    #                       point represents a single observation of a 
    #                       species.
    #          fldSpecies = a string containing the name of the field
    #                       in the points layer that contains the name
    #                       of the species
    #
    #     The purpose of the function is to summarize the number of
    #     observations of each species inside the polygon in the form
    #     of a dictionary containing species as keys and the number of
    #     observations as values.
    
    dctPoly = {}
    
    # loop through all the points that intersect the polygons bounding box
    for obs in lyrPoint.getFeatures(poly.geometry().boundingBox()):
        # check to see if the pont is actually inside the polygon
        if poly.geometry().contains(obs.geometry()):
           # get the name of the species as a string variable
           sSpecies = obs.attribute(fldSpecies)
           # check to see if the species already has an entry in the dictionary
           if sSpecies in dctPoly.keys():
               # if it does, increase the count to 1
               dctPoly[sSpecies] += 1
           else:
               # if there s no entry for the species, create it and set its
               # intal value to 1
               dctPoly[sSpecies] = 1
               
    return dctPoly
    
def dc_mergedictionaries(dMain, cat, dPoly):
    ####################################################################
    #
    #     This function takes as inputs the following parameters:
    #          dMain = a dictonary with categories as the key and another
    #                  dictionary containing summary information as the value
    #          cat = a string containing the name of the category to be merged
    #          dPoly = a dctonary containing summary information for a polygon
    #                  (created by the dc_processPoly function). The keys are the
    #                  names of the species occuring in the polygon and the values
    #                  are the number of observations of that species in the polygon
    #
    #      The purpose of the functon is to merge the species counts from dPoly into
    #      the appropiate summary nformaton in dMain.
    
    # check to see if the category exsts in the dMain dictionary
    if cat in dMain.keys():
       #if it does then loop through the summary data in dPoly
       for species, obs in dPoly.tems():
             # check to see if there is already an entry for the species in this category
            if species in dMain[cat].keys():
                # if there s then add the number of observations in the summary data
                dMain[cat][species] += obs
            else:
                # if there isn´t then create a new entry for the species and set the
                # number of observations as the initial value                
                dMain[cat][species] = obs
    else:
        # if it doesn´t then create an entry for the category with the summary
        # dictonary as the initial value
        dMain[cat] = dPoly
        
    return dMain
    
def dc_richness(dict):
    ###################################################################
    #
    #     This function takes as nputs the following parameters:
    #            dict = a dictionary contaning summary information for a polygon
    #                   The keys are the names of the species occurng in the polygon
    #                   and the values are the number of observations of that speces
    #                   in the polygon
    #
    #     The purpose of the functon is to calculate species richness from the dict
    #     provided above, which s just the total number of species observed or the
    #     length of the dctionaries

    return len(dict)

def dc_shannons(dict):
    ###################################################################
    #
    #     This function takes as nputs the following parameters:
    #           dict = a dictionary contaning summary information for a polygon
    #                   The keys are the names of the species occurng in the polygon
    #                   and the values are the number of observations of that speces
    #                   in the polygon
    #
    #     The purpose of the unction is to calculate shannons diversity index from
    #     the dict provided above.

    # First calculate the total number of observations
    total = sum(dict.values())

    #set the initial value to 0
    shannons = 0;

    #loop throuh all the speces counts in the dctionary
    for count in dict.values():
        #calculate proportion of total observations
        prop = count/total

        shannons += prop*math.log(prop)
    return abs(shannons);

def dc_simpsons(dict):
    ###################################################################
    #
    #     This function takes as nputs the following parameters:
    #           dict = a dictionary contaning summary information for a polygon
    #                   The keys are the names of the species occurng in the polygon
    #                   and the values are the number of observations of that speces
    #                   in the polygon
    #
    #     The purpose of the function is to calculate simpsons dversity index from
    #     the dict provided above.

    #frst calculate the total number of observations
    total = sum(dict.values())

    #set the initial value to 0
    simpsons = 0;

    #loop through all the speces counts in the dictionary
    for count in dict.values():
        #calculate proportion of total observations 
        prop = count/total

        simpsons += prop*prop
    return simpsons


def dc_evenness(dict):
    #################################################################
    #
    #     This function takes as nputs the following parameters:
    #           dict = a dictionary contaning summary information for a polygon
    #                   The keys are the names of the species occurng in the polygon
    #                   and the values are the number of observations of that speces
    #                   in the polygon
    #
    #     The purpose of the function is to calculate species eveness index from
    #     the dict provided above.  Evenness will be 1 when all the species have the
    #     same number of observations and lower values as some species have greater
    #     numbers of observations than others
    
    #maximum value that shannons index can be is the log of the total number of species (richness)
    max = math.log(dc_richness(dict))
    return dc_shannons(dict)/max

def dc_resultString(dict):    
    result = ""
    for category, summary in dct.items():
        result += "{}: {}  {:2.3f}  {:2.3f}  {:2.3f}\n".format(category, dc_richness(summary), dc_shannons(summary), dc_simpsons(summary), dc_evenness(summary))
    return result
    