India_State_Capital_Date={'Karnataka':{'Capital':'Bangalore','Date':'1 Nov 1956'}
                          ,'Arunachalpradesh':{'Capital':'Itanagar','Date':'20 Feb 1987'}
                          ,'Bihar':{'Capital':'Patna','Date':'26 Jan 1950'}
                          ,'Chhattisgarh':{'Capital':'Raipur','Date':'1 Nov 2000'}
                          ,'Haryana':{'Capital':'Chandighar','Date':'1 Nov 1966'}
                          ,'Jharkand':{'Capital':'Ranchi','Date':'15 Nov 2000'}
                          ,'AndraPradesh':{'Capital':'Amaravati','Date':'1 Nov 1956'}
                          ,'TamilNadu':{'Capital':'Chennai','Date':'26 jan 1950'}
                          ,'Assam':{'Capital':'Dispur','Date':'26 Jan 1950'}
                          ,'Goa':{'Capital':'Panaji','Date':'30 May 1987'}
                          ,'Kerala':{'Capital':'Thiruvananthapuram','Date':'1 Nov 1956'}
                          ,'Maharashtra':{'Capital':'Mumbai','Date':'1 May 1960'}
                          ,'Gujarath':{'Capital':'Gandhinagar','Date':'1 May 1960'}
                          ,'Madhyapradesh':{'Capital':'Bhopal','Date':'1 Nov 1956'}
                          ,'Nagaland':{'Capital':'Kohima','Date':'1 Dec 1963'}
                          ,'Punjab':{'Capital':'Chandhighar','Date':'1 Nov 1956'}
                          ,'Telangana':{'Capital':'Hydrabad','Date':'2 June 2014'}
                          ,'Westbengal':{'Capital':'Kolkata','Date':'1 Nov 1956'}
                          ,'Odisha':{'Capital':'Bhubaneswar','Date':'26 Jan 1950'}
                          ,'Himachalpradesh':{'Capital':'Shimla','Date':'25 Jan 1971'}
                          ,'Manipur':{'Capital':'Imphal','Date':'21 Jan 1972'}
                          ,'Meghalaya':{'Capital':'Shillong','Date':'21 Jan 1972'}
                          ,'Rajasthan':{'Capital':'Jaipur','Date':'1 Nov 1956'}
                          ,'Mizoram':{'Capital':'Aizawl','Date':'20 Feb 1987'}
                          ,'Sikkim':{'Capital':'Gangtok','Date':'16 May 1975'}
                          ,'Tripura':{'Capital':'Agartala','Date':'21 Jan 1972'}
                          ,'Uttarpradesh':{'Capital':'Lucknow','Date':'26 Jan 1950'}
                          ,'Uttarkand':{'Capital':'Dehradun (Winter)Gairsain (Summer)','Date':'9 Nov 2000'}}
print(len(India_State_Capital_Date))
del India_State_Capital_Date['Arunachalpradesh']
print(India_State_Capital_Date['Karnataka'])
for Data in India_State_Capital_Date.items():
    print(Data)
    #print(Data)