# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:37:11 2021

@author: RENJINI
"""

import os
import pandas as pd
import numpy as np
import csv

os.chdir('E:\Spyder codes')

#%%
##############################################################################################

data = pd.read_csv('Land_verification_chatbot.csv')
data

data.drop(['User_Type'],axis = 1,inplace = True)
data.dropna(axis = 1,inplace = True)
data

rows = data.iloc[:,:]

propid = []
propid.append(data['Property_Id'])
    
propid

#%%
##################################################################################################
  def EndUser():
     
      sample1 = data.copy(deep=True)
      sample1.drop(['p_owner_id','P_owner_name'],inplace = True,axis=1)
      flag = 0
      
      print("# # # # # # END USER # # # # # #")
      val = int(input("Enter the Property Id: "))
      print(sample1.loc[sample1['Property_Id'] == val])
      for column in sample1['Property_Id']:
          if column == val :
              flag = 1
              break
          else:
              flag = 2
      if flag == 2:
          print("No Record exists!!!")
      
 #%% 
################################################################################################### 
  
  def Advocate():
    
    sample = data.copy(deep=True)
    flag = 0
    
    print("# # # # # # ADVOCATE # # # # # #")
    val = int(input("Enter the Property Id: "))
    print(sample.loc[sample['Property_Id'] == val])
    
    
    for column in sample['Property_Id']:
          if column == val:
              flag = 1
              break
          else :
              flag = 2
              
    if flag == 2:
        print("No Record Exist!!!")
        
        
    
    
    
#%%   
#############################################################################################
  def Admin():  
    sample = data.copy(deep=True)
    record = {}
    flag = 0
    
    print("# # # # # # ADMIN # # # # # #")       
    print(" 1.View Record\n 2. Insert Record \n 3.Delete Record")
    choice = int(input('Enter your Choice: '))
    if choice == 1:
        val = int(input("Enter the Property Id: "))
        print(sample.loc[sample['Property_Id'] == val])
        for column in sample['Property_Id']:
            if column == val :
                flag = 1
                break
            else:
                flag = 2
        if flag == 2:
               print("No Record exists!!!")
    elif choice == 2:           
        val1 = input("Enter the property_Id: ")
        val2 = input("Enter the Current Owner name: ")
        val3 = input("Current Owner Id: ")
        val4 = input("Enter Previous Owner name: ")
        val5 = input("Enter Previous owner Id: ")
        val6 = input("Enter Size of land: ")
        val7 = input("Enter the location: ")
        val8 = input("Enter the Registration Date: ")
        record['Property_Id'] = val1
        record['C_owner_name'] = val2
        record['C_owner_Id'] = val3
        record['P_owner_name'] = val4
        record['p_owner_Id'] = val5
        record['Size'] = val6
        record['Location'] = val7
        record['Registration_date'] = val8
        sample = sample.append(record,ignore_index=True)
        #sample.tail(5)
    elif choice == 3:
        newval = int(input("Enter the Property Id to be removed: "))
        propid = []
        propid.append(data['Property_Id'])
        l = len(propid)
        for i in range(0,l):
            if newval == propid[0][i]:
                print("Property removed from record!!")
                sample.drop(i,axis=0,inplace=True)
                break
       
    
    
#%%
####################################################################################################

    print("Hello....")
    print(" Users are : \n 1.Admin \n 2.End user\n 3.Advocates")
    option = int(input("Choose the type of User: "))
    if option == 1:
        Admin()
    elif option == 2:
        EndUser()
    elif option == 3:
        Advocate()
    else :
        print("...Sorry ! Not allowed to enter...")
        