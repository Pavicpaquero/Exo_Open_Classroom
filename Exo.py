import pandas as pd
import numpy as np
import re 

data = pd.read_csv('operations.csv')



#on addition les soldes avant et après pour calculer le montant
print(data.isnull().sum())
mon=data.loc[data['montant'].isnull(),:]
for index in mon.index:
    data.loc[index,'montant']=data.loc[index,'solde_avt_ope'] - data.loc[index+1 ,'solde_avt_ope']


#on regarde si la modifictaion fonctionne .   
mon=data.loc[data['montant'].isnull(),:]
print(mon)



#on regarde les chaine dupliqué 
other=data.loc[data[['date_operation','libelle','montant','solde_avt_ope','categ']].duplicated(keep=False),:]
print(other)



#on supprime la duplication puis on l'affiche
test=other.drop_duplicates()
print(test)



#on affiche toute les lignes de la ou peut se trouver l'erreurs 
cate=data.loc[data['libelle'] =='PRELEVEMENT XX TELEPHONE XX XX']
print(cate)




#on choppe la ligne avec le NaN et on remplace la categ
hoy=data.loc[data['categ'].isnull(), 'categ'] ='FACTURE TELEPHONE'



#on observe une erreur au niveau de date_operation
print(data.dtypes)



#On change le type et on affiche
data['date_operation'] = pd.to_datetime(data['date_operation'],)
print(data.dtypes)



#Autre probleme
print (data.describe())
desc=data.loc[data['categ'] =='AUTRE']
print(desc)

py=data.loc[data['montant'] ==-15000,'montant']=-14.39
print(py)