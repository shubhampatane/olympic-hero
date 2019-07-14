# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data =pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace='True')
print(data.head(10))
#Code starts here



# --------------
#Code starts here





data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', 'Winter')
data.loc[data.Total_Summer == data.Total_Winter, 'Better_Event'] = 'Both' 
btr = data['Better_Event'].value_counts()

if(btr[0]>btr[1] and btr[0]>btr[2]):
    better_event = 'Summer'
elif(btr[1]>btr[0] and btr[1]>btr[2]):
    better_event = 'Winter'
else:
    better_event = 'Both'
print(better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries.drop([146], axis=0)
def top_ten(tc,cn):
    td = tc.nlargest(10,cn)
    country_list = list(td['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
common = [x for x in top_10_summer if x in top_10_winter and x in top_10]
print(common)




# --------------
#Code starts here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1)
data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace='True')

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries.drop([146], axis=0)
def top_ten(tc,cn):
    td = tc.nlargest(10,cn)
    country_list = list(td['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
common = [x for x in top_10_summer if x in top_10_winter and x in top_10]

summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind ='bar',x='Country_Name',y='Total_Summer',ax=ax_1)
ax_1.set_title('Applicant Income')
winter_df.plot(kind ='bar',x='Country_Name',y='Total_Winter',ax=ax_2)
ax_2.set_title('Applicant Income')
top_df.plot(kind ='bar',x='Country_Name',y='Total_Medals',ax=ax_3)
ax_3.set_title('Applicant Income')
plt.show()



# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
ser = summer_df.loc[summer_df['Golden_Ratio'].idxmax()]
summer_country_gold = ser[0]

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
ser = winter_df.loc[winter_df['Golden_Ratio'].idxmax()]
winter_country_gold = ser[0]

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
ser = top_df.loc[top_df['Golden_Ratio'].idxmax()]
top_country_gold = ser[0]


# --------------
#Code starts here



data_1 = data[:146]
data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']
most_points = data_1['Total_Points'].max()
ser = data_1.loc[data_1['Total_Points'].idxmax()]
best_country = ser[0]


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


