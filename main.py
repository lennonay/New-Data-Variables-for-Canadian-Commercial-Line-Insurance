from Listings import listings
import pandas as pd
from multiprocessing import Pool
from getinfo import getinfo
import time
from Combine import combine


if __name__ == '__main__':
    start_time = time.time()

    dflocation = pd.read_csv("input//location.csv")
    loclist = dflocation.values.tolist()

    dfcuisine = pd.read_csv("input//cuisine.csv")
    cuilist = dfcuisine.values.tolist()

    loc = 0 #modify
    cui = 0 #modify

    len_location = len(dflocation.Location) #102 locations
    len_cuisine = len(dfcuisine.id) #59 cuisines

    #for l in range(loc,loc+1): #len_location
     #   for c in range(cui,cui+1):

    for l in range(loc,len_location): 
        for c in range(cui,len_cuisine):

            df = listings(loclist[l],cuilist[c]) #calling listing fucntion

            output_path = "output//listings//"+str(loclist[l][1])+"//"+str(loclist[l][0])+'_'+str(loclist[l][1])+'_'+str(cuilist[c][0])+'_listings.csv'
            df.to_csv(output_path)

            if len(df) >=1:
                df3 = df
                df3 = df3.values.tolist()

                with Pool(10) as pool:  #number of instances to be opened at once
                    data = pool.map(getinfo, df3)

                df_final = pd.concat(data, ignore_index=True)

                output_path = "output//info//" + loclist[l][1] + "//raw//" + loclist[l][0] + "_" + loclist[l][1] + "_" + cuilist[c][0] + '_restaurant_info.csv'
                df_final.to_csv(output_path)


    combine()

    finish_time = time.time() - start_time
    print(finish_time)