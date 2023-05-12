from django.core.management.base import BaseCommand
import pandas as pd
from aerodevs.models import Product

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument('file', type=str, help='Adding data')

	def handle(self, *args, **kwargs):
		my_file = kwargs['file']
		df = pd.read_excel(my_file)
		df = df.iloc[:21]
		df = df[['Part Name', 'Material Composition', 'Age (years)', 
		'Manufacturer', #'Landfill Waste Saved (kg)', 'Energy Consumption Saved (kWh)', 
		#'Remanufacturing Potential (%)'
		]]
		mapping = {'Part Name': 'part_name', 'Material Composition': 'material', 'Age (years)': 'age', 'Manufacturer':'manufacturer' #'Landfill Waste Saved (kg)':'Landfill_Waste_Saved','Energy Consumption Saved (kWh)':'Energy_Saved','Remanufacturing Potential (%)':'Remanufacturing_Potential'
		}
		df = df.rename(columns=mapping)

		#objs = [Product(**row.to_dict()) for _,row in df.iterrows()]
		#Product.objects.bulk_create(objs)
		#data_index = df.columns.get_loc('part_name')
		for row in df.values:
			Product_qs = Product.objects.create(part_name=row[0],
				material=row[1], age=row[2], manufacturer=row[3],
				#Landfill_Waste_Saved=row[4], Energy_Saved=row[5],
				#Remanufacturing_Potential=row[6]
				)
			
		
		#for _, row in df.iterrows():
		#    obj = Product(
		 #       part_name=row['part_name'],
		  #      material=row['material'],
		   #     age=row['age'],
		    #    manufacturer=row['manufacturer']
		    #)
		    #obj.save()	