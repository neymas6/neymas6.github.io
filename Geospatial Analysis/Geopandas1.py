import geopandas as gpd
from shapely.geometry import Point
from matplotlib import pyplot as plt
import contextily

# Information for each of Barcelona's districts
url = 'https://raw.githubusercontent.com/jcanalesluna/bcn-geodata/master/districtes/districtes.geojson'

districts = gpd.read_file(url)
print(districts.head(10))

# create GeoJSON file
# districts.to_file('districts.geojson', driver='GeoJSON')

print(districts.crs)

# district GeoDataFrame is associated with geographic coordinates EPSG: 4326

# change EPSG to 2062 (convert to projected coordinates)
districts.to_crs(epsg=2062, inplace=True)
print(districts.crs)

# convert area of each district to km^2
districts['area'] = districts.area / 1000000 

# add column for centroid of each district
districts['centroid'] = districts.centroid

districts['boundary'] = districts.boundary


# find distance from each district's centroid to the Sagrada Family church in the Eixample district in Barcelona

sagrada = Point(2.1743680500855005, 41.403656946781304)
sagrada = gpd.GeoSeries(sagrada, crs=4326)
sagrada = sagrada.to_crs(epsg=2062)
districts['sagrada'] = [float(sagrada.distance(centroid).iloc[0]) / 1000 for centroid in districts.centroid]


# visualize the districts
ax = districts.plot(column='NOM',figsize=(10,6),edgecolor='black',legend=True)
plt.show()