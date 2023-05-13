from django.core.management.base import BaseCommand
import pandas as pd
from aerodevs.models import Product

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument('file', type=str, help='Adding data')

	def handle(self, *args, **kwargs):
		my_file = kwargs['file']
		df = pd.read_excel(my_file)
		df = df
		df['Percentage_recycled'] = (df['Recycling Rate (%)']*df['Remanufacturing Potential']*df['Renewable Material Content (%)'])/(len(df.index)*10000)

		df = df[['Part Name', 'Material Composition', 'Age (years)', 
		'Manufacturer',
		'New Parts Carbon Footprint (kg CO2e)', 
		'Recycled Parts Carbon Footprint (kg CO2e)',
		'Energy Consumption - New Parts (kWh)',
		'Renewable Material Content (%)',
		'Carbon Footprint Saved (kg CO2e)',
		'Energy Consumption Saved (kWh)',
		'Remanufacturing Potential (%)',
		'Percentage_recycled'
		]]

		mapping = {'Part Name': 'part_name', 
		'Material Composition': 'material', 
		'Age (years)': 'age', 
		'Manufacturer':'manufacturer',
		'New Parts Carbon Footprint (kg CO2e)':'New_Parts_Carbon_Footprint',
		'Recycled Parts Carbon Footprint (kg CO2e)': 'Recycled_Parts_Carbon_Footprint',
		'Energy Consumption - New Parts (kWh)': 'Energy_Consumption_New_Parts',
		'Renewable Material Content (%)':'Renewable_Material_Content',
		'Carbon Footprint Saved (kg CO2e)':'Carbon_Footprint_Saved',
		'Energy Consumption Saved (kWh)': 'Energy_Consumption_Saved',
		'Remanufacturing Potential (%)': 'Remanufacturing_Potential',
		'Percentage_recycled':'Percentage_recycled'
		}
		df = df.rename(columns=mapping)

		#objs = [Product(**row.to_dict()) for _,row in df.iterrows()]
		#Product.objects.bulk_create(objs)
		#data_index = df.columns.get_loc('part_name')
		for row in df.values:
			Product_qs = Product.objects.create(part_name=row[0],
				material=row[1], age=row[2], manufacturer=row[3],
				New_Parts_Carbon_Footprint =row[4],
				Recycled_Parts_Carbon_Footprint =row[5],
				Energy_Consumption_New_Parts =row[6],
    			Renewable_Material_Content =row[7],
    			Carbon_Footprint_Saved =row[8],
    			Energy_Consumption_Saved =row[9],
    			Remanufacturing_Potential =row[10],
    			Percentage_recycled=row[11]
				)
			
		
		#for _, row in df.iterrows():
		#    obj = Product(
		 #       part_name=row['part_name'],
		  #      material=row['material'],
		   #     age=row['age'],
		    #    manufacturer=row['manufacturer']
		    #)
		    #obj.save()	