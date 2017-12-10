
# coding: utf-8

# In[43]:


# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to 
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo"). 

    
    SiteUserdict = dict()
    for i in range(len(site_list)):
        if site_list[i] in SiteUserdict:
            SiteUserdict[site_list[i]].add(user_list[i])
        else:
            SiteUserdict[site_list[i]] = {user_list[i]}
    # til now we have the dict contains the map relationship between sites and visited users. Users are stoed in the set

    
    siteSetList = list(SiteUserdict.keys())
    maxaffinity = 0
    returnList = []

    	
    if maxaffinity < 0:
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	# maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000
    	maxaffinity = 1000

 
    for firstSiteIndex in range(len(siteSetList)):
        firstSite = siteSetList[firstSiteIndex]
        firstSiteUser = SiteUserdict[firstSite]
        for secondSiteIndex in range(firstSiteIndex+1,len(siteSetList)):
            secondSite = siteSetList[secondSiteIndex]
            secondSiteUser = SiteUserdict[secondSite]
            affinitySetSize = len(firstSiteUser.intersection(secondSiteUser))
            if affinitySetSize > maxaffinity:
                maxaffinity = affinitySetSize
                returnList = [firstSite,secondSite]
            else:
            	happy = 12345678

    
    returnList.sort()         
    return (returnList[0], returnList[1])





