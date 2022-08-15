import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io





def make_plot_brand(brand):

	train = pd.read_csv("train.csv")
	train.drop(columns="New_Price",inplace=True)
	train.dropna(axis=0, inplace=True)

	brand_col = train.Name.str.extract(pat=r'(\w+) (\w+)', expand=False)[0]
	train["Brand"] = brand_col
	brands_less_than_10 = train.Brand.value_counts()[train.Brand.value_counts().values < 10].index.to_list()
	train.Brand = train.Brand.apply(lambda x: 'other' if x in brands_less_than_10 else x)


	plt.figure(figsize=(8, 4))
	plt.title(str(brand))
	plt.ylabel('Price')
	sns.scatterplot(x = train["Year"].loc[train["Brand"] == str(brand)], y = train["Price"].loc[train["Brand"] == str(brand)], data=train)
	bytes_image = io.BytesIO()
	plt.savefig(bytes_image, format='png')
	bytes_image.seek(0)
    
	return bytes_image

def make_plot_fuel_type(fuel_type):

	train = pd.read_csv("train.csv")
	train.drop(columns="New_Price",inplace=True)
	train.dropna(axis=0, inplace=True)

	plt.figure(figsize=(8, 4))
	plt.title(str(fuel_type))
	plt.ylabel('Price')
	sns.scatterplot(x = train["Year"].loc[train["Fuel_Type"] == str(fuel_type)], y = train["Price"].loc[train["Fuel_Type"] == str(fuel_type)], data=train)
	bytes_image = io.BytesIO()
	plt.savefig(bytes_image, format='png')
	bytes_image.seek(0)
    
	return bytes_image



def make_plot_year(year):

	train = pd.read_csv("train.csv")
	train.drop(columns="New_Price",inplace=True)
	train.dropna(axis=0, inplace=True)

	plt.figure(figsize=(8, 4))	
	plt.title(str(year))
	#train.loc[train["Year"] == year].boxplot(column=['Price'])
	fig1, ax1 = plt.subplots()
	ax1.set_title(str(year))
	ax1.boxplot(train["Price"].loc[train["Year"] == year])
	bytes_image = io.BytesIO()
	plt.savefig(bytes_image, format='png')
	bytes_image.seek(0)  
    
	return bytes_image


def make_plot_transmission(transmission):

	train = pd.read_csv("train.csv")
	train.drop(columns="New_Price",inplace=True)
	train.dropna(axis=0, inplace=True)

	brand_col = train.Name.str.extract(pat=r'(\w+) (\w+)', expand=False)[0]
	train["Brand"] = brand_col
	brands_less_than_10 = train.Brand.value_counts()[train.Brand.value_counts().values < 10].index.to_list()
	train.Brand = train.Brand.apply(lambda x: 'other' if x in brands_less_than_10 else x)


	plt.figure(figsize=(8, 4))
	plt.title(str(brand))
	plt.ylabel('Price')
	sns.scatterplot(x = train["Year"].loc[train["Brand"] == str(brand)], y = train["Price"].loc[train["Brand"] == str(brand)], data=train)
	bytes_image = io.BytesIO()
	plt.savefig(bytes_image, format='png')
	bytes_image.seek(0)
    
	return bytes_image


def make_plot_engine(engine):

	train = pd.read_csv("train.csv")
	train.drop(columns="New_Price",inplace=True)
	train.dropna(axis=0, inplace=True)

	brand_col = train.Name.str.extract(pat=r'(\w+) (\w+)', expand=False)[0]
	train["Brand"] = brand_col
	brands_less_than_10 = train.Brand.value_counts()[train.Brand.value_counts().values < 10].index.to_list()
	train.Brand = train.Brand.apply(lambda x: 'other' if x in brands_less_than_10 else x)


	plt.figure(figsize=(8, 4))
	plt.title(str(brand))
	plt.ylabel('Price')
	sns.scatterplot(x = train["Year"].loc[train["Brand"] == str(brand)], y = train["Price"].loc[train["Brand"] == str(brand)], data=train)
	bytes_image = io.BytesIO()
	plt.savefig(bytes_image, format='png')
	bytes_image.seek(0)
    
	return bytes_image