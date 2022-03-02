# Surf's Up Module 9 Challenge
Module 9: Surf's Up with Advanced Data Storage and Retrieval

## The Purpose of This Analysis
1. Explain the structures, interactions, and various types of data in this dataset
2. Explain the differences in SQLite and PostgreSQL 
3. Leverage SQLAlchemy to connect to and query a SQLite database
4. Provide statisticas as part of the data analysis
5. Design and create a Flask application using the data

## Overview:
We are looking to open a surf and shake shop in the state of Hawaii on Oahu. We have some of our own capital but are also looking for investors. As such we have reached out to W. Avy who is a top surfer interested in our business plan but he wants an analysis of a weather dataset he has in order to determine the feasibility of such a plan. He's asking because he's literally been rained out on prior investments. The main plan is to be open year round but we could see if this plan might be modified to close during some of the wetter months if necessary.

## Conclusions:
### Temperature and Precipitation Stats for the Month of June

![Pic_1](https://github.com/dannybarto/Surfs_Up/raw/main/Resources/June_Temp.png)
![Pic_2](https://github.com/dannybarto/Surfs_Up/raw/main/Resources/June_Prcp.png)


### Temperature and Precipitation Stats for the Month of December

![Pic_3](https://github.com/dannybarto/Surfs_Up/raw/main/Resources/December_Temp.png)
![Pic_4](https://github.com/dannybarto/Surfs_Up/raw/main/Resources/December_Prcp.png)

The mean temperature is about 75 degrees versus the 71 degree mean we observe in December. As far as the preciptiation goes we observe a mean of nearly .14 inches in June against the approximately .22 inches in December.

### Additional Queries for Histogram and Scatter Plots to Visulize the Data

![Pic_5](https://github.com/dannybarto/Surfs_Up/raw/main/Resources/June_Temps_Histogram.png)
![Pic_6](https://github.com/dannybarto/Surfs_Up/raw/main/Resources/June_Temp_Prcp_Scatter.png)
![Pic_7](https://github.com/dannybarto/Surfs_Up/raw/main/Resources/Dec_Temps_Histogram.png)
![Pic_8](https://github.com/dannybarto/Surfs_Up/raw/main/Resources/Dec_Temp_Prcp_Scatter.png)

We made use of histograms to visually display how the frequency centers around the two means.  Each of the graphs use the same parameters to ensure comparability.  We can see that the June data is skewed to the left while December has a more symmetrical or uniform skew.


 We created an additional query filtered by June and December  The temperature and precipitation data was then graphed as a scatterplot with a trendline.  For June the slope is -.0367 and is a little bit steeper than December's slope at  -.0186. This indicates that temperature increases the precipitation decreases. This isn'a a particularly material difference.  Overall the precipitation tends to stay under 3 inches in either month.



## Summary:
W. Avy was primarily concerned with how the rain might affect business  Comparing the June and December weather patterns, the temperatures and precipitation means are reasonably close.  While December is slightly wetter and slightly cooler there really doesn't seem to be any reason for concern.  In my opinion the data clearly shows that the Ice Cream and Surf shop can be open year round without issue.
