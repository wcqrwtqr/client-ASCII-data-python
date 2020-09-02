#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:14:44 2017

@author: mohammedalbatati
"""

import pandas as pd
import matplotlib.pyplot as plt
#from bokeh.plotting import figure, output_file,show

#df2 = pd.read_csv('2 inch oil.csv',header=None,skiprows = 12,index_col = False,names=['Date','Time','empty','Oil line Temp','2" Measured Rate','2" Liquid Rate Ave','2" Liquid Cum','BS&W Cut','Oil SG','Oil SG Temp','API @60F','CMF','ST Temp','CTL','2" STOil Rate','2" STOil Cum','Water Rate','Water Cum'])
#df3 = pd.read_csv('3 inch oil.csv',header=None,skiprows = 12, index_col = False,names=['Date','Time','empty','Meter Temp','3" Measured Rate','3" Liquid Rate','3" Liquid Cum','BS&W Cut','Oil SG','Oil SG Temp','API @60F','CMF','ST Temp','CTL','3" STOil Rate','3" STOil Cum','Water Rate','Water Cum'])
#dfG = pd.read_csv('Gas.csv',header=None,skiprows = 12, index_col = False,names=['Date','Time','empty','Static Press','Gas line Temp','Differential Press','Plate Size','Gas G','Fn','Fc(Flange) / Fb(Pipe)','Fsl(Flange) / Fr(Pipe)','Fpv','Ftf','Ftb','Y','Fgr','Fpb','C','Gas Rate (Inst) Ave','Gas Rate (average) Ave','Gas Cum'])
#dfW = pd.read_csv('WHP.csv',header=None,skiprows = 12, index_col = False,names=['Date','Time','empty','WHP','WHT','DSCP','CSGP','Oil line Temp','3" Measured Rate','3" Liquid Cum','3" STOil Rate','3" STOil Cum','2" Measured Rate','2" Liquid Cum','Measured Rate CPF','Water Cum'])


dfM = pd.read_csv('Merged2.csv',header=None,skiprows = 1, index_col = False,names=['Date','Time','Combo_Date','WHP','WHT','DSCP','CSGP','Oil line Temp','Static Press','Gas line Temp','Differential Press','Gas Rate (Inst) Ave','Gas Rate (average) Ave','Gas Cum','3" STOil Rate','3" STOil Cum','2" STOil Rate','2" STOil Cum'])

#Dropping===================================
#df2['D_T'] = pd.to_datetime(df2['Date'] +' '+ df2['Time'])
#
##print(df2.columns)
#df2 = df2.drop(['empty', 'Oil line Temp', '2" Measured Rate',
#       '2" Liquid Rate Ave', '2" Liquid Cum', 'BS&W Cut', 'Oil SG',
#       'Oil SG Temp', 'API @60F', 'CMF', 'ST Temp', 'CTL',
#        'Water Rate', 'Water Cum'],axis=1)
#
##print(df3.columns)
#df3 = df3.drop(['empty', 'Meter Temp', '3" Measured Rate',
#       '3" Liquid Rate', '3" Liquid Cum', 'BS&W Cut', 'Oil SG', 'Oil SG Temp',
#       'API @60F', 'CMF', 'ST Temp', 'CTL',
#       'Water Rate', 'Water Cum'],axis=1)
#
##print(dfG.columns)
#dfG = dfG.drop(['empty', 'Plate Size', 'Gas G', 'Fn',
#       'Fc(Flange) / Fb(Pipe)', 'Fsl(Flange) / Fr(Pipe)', 'Fpv', 'Ftf', 'Ftb',
#       'Y', 'Fgr', 'Fpb', 'C', 'Gas Rate (Inst) Ave'],axis=1)
#
#
##print(dfW.columns)
#dfW = dfW.drop(['empty', 'WHP', 'WHT', 'DSCP', 'CSGP',
#       '3" Measured Rate', '3" Liquid Cum', '3" STOil Rate', '3" STOil Cum',
#       '2" Measured Rate', '2" Liquid Cum', 'Measured Rate CPF', 'Water Cum'],axis=1)

#=====================================

#df = pd.merge(df2,df3,on='Time')
#df1= pd.merge(df,dfG,on='Time')
#dfF = pd.merge(df1,dfW,on='Time')

#df3 = df3.drop(['NN_x','NN_y','Storage_T_P_02_x','Gas Rate (average)_y','Gas Cum_y','SEP Press_y','Differential Press_y','Gas T_y','Date_y','Storage_T_P_02_y'],axis=1)

#dfM['D_T'] = pd.to_datetime(dfM['Date'] +' '+ dfM['Time'])
dfM['Combo_Date'] = pd.to_datetime(dfM['Combo_Date'])

#print(df3.columns)
#print(df3['Gas Rate (average)_x'])
#df3['myGOR'] = df3['Gas Rate (average)_x']*1000000/df3['STOil Rate'] 
#print(df3['Differential Press_x'].head(20),df3['Differential Press_y'].head(20) )
#print(df3['myGOR'][0:44].mean())



plt.figure()
plt.plot(dfM['Combo_Date'],dfM['2" STOil Rate'],'b-')
plt.plot(dfM['Combo_Date'],dfM['3" STOil Rate'],'g-')
plt.plot(dfM['Combo_Date'],dfM['WHP'],'r-')
#plt.plot(x,MPFM_data.loc[n:m,'Temperature'],'r-')
#plt.xticks(rotation='vertical')
plt.xticks(rotation=45)
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.05)
plt.subplots_adjust(bottom=0.15)
plt.legend()
plt.show

#plt.figure()
#plt.plot(dfM['Combo_Date'],dfM['Gas Rate (average) Ave'],'b-')
#plt.plot(dfM['Combo_Date'],dfM['3" STOil Rate'],'g-')
#plt.plot(dfM['Combo_Date'],dfM['WHP'],'r-')
#plt.xticks(rotation=45)
#plt.legend()
#plt.show

#plt.figure()
#plt.plot(x,MPFM_data.loc[n:m,'Std.GasFlowrate'],'y-')
#plt.plot(x,MPFM_data.loc[n:m,'Std.Watercut'],'b-')
#plt.xticks(rotation=45)
#plt.legend()
#plt.show

#p = figure(plot_width=900, plot_height=500, x_axis_type='datetime')
#p.title='2" Flow rate'
#p.line(dfM['D_T'],dfM['2" STOil Rate'],line_width=2,color='red')
##p.line(dfM['Combo_Date'],dfM['3" STOil Rate'],line_width=2, color='blue')
#output_file('TT-29 Row Date_plotting.html')
#show(p)
#
#p3 = figure(plot_width=900, plot_height=500, x_axis_type='datetime')
#p3.title='3" Flow rate'
#p3.line(df3['D_T'],df3['3" STOil Rate'],line_width=2)

##p.line(df3['Date_Time1'],df3['WHT'],line_width=2, line_color='red', y_range_name="foo")
#output_file('TT-29 Row Date_plotting.html')
#show(p)
#show(p3)

#print(df.head(5))

# test the git updater
