import pandas as pd   
df = pd.read_excel('produits.xlsx')

#afficher les dimmenssions du dataframe
print(df.shape)

#INFORMATIONS
print(df.info())

#10 premieres lignes 
print(df.head(10))

#afficher la liste des variables
print(df.columns)

#extraire les colonnes 
colonnes = ["Nom","Categorie","Origine" , "Prix"]

#afficher les conditions 
print(df.loc[df["Categorie"] == "Boissons" , colonnes] )

#boissons et prix > 100
print(df.loc[(df["Categorie"] == "Boissons") & (df["Prix"] > 100) , colonnes] )

#catégorie = boissons et origine=CEE et prix > 100
print(df.loc[(df["Categorie"] == "Boissons") & (df["Origine"] == "CEE") & (df["Prix"] > 100) , colonnes] )


#catégorie = boissons ou catégorie = condiments
print(df.loc[(df["Categorie"] == "Boissons") | (df["Categorie"] == "Condiments") , colonnes] )
#(catégorie = boissons et origine = CEE) OU (catégorie = condiment)
print(df.loc[((df["Categorie"] == "Boissons") & (df["Origine"] == "CEE")) | (df["Categorie"] == "Condiments") , colonnes] )
#catégorie = viande ET origine = CEE) OU (catégorie = condiment ET origine = extérieur)
print(df.loc[((df["Categorie"] == "Viande") & (df["Origine"] == "CEE")) | ((df["Categorie"] == "Condiments") & (df["Origine"] == "extérieur")) , colonnes] )
#prix > 70 et prix <=100
print(df.loc[(df["Prix"] > 70) & (df["Prix"] <= 100) , colonnes] )
#Lister les aliments dont le prix est compris entre 100 et 200, et qui sont des « viandes »
print(df.loc[(df["Prix"] > 100) & (df["Prix"] <= 200) & (df["Categorie"] == "Viande") , colonnes] )


#lister les 5 produits les moins cher 
print(df.loc[df.nsmallest(15, 'Prix').index , colonnes] )