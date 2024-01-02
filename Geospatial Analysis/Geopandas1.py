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


# visualize the districts (Figure_1)
ax = districts.plot(column='NOM',figsize=(10,6),edgecolor='black',legend=True)
plt.show()

# more detailed graph using contextily (Figure_2)
ax = districts.plot(column='NOM', figsize=(12,6), alpha = 0.5, legend=True)
districts['centroid'].plot(ax=ax, color='green')
sagrada.plot(ax=ax, color='black',marker='+')
contextily.add_basemap(ax, crs=districts.crs.to_string())
plt.title('Detailed Map of Barcelona')
plt.axis('off')
plt.show()


# add data on where bike lanes are located
bike_url = 'https://opendata-ajuntament.barcelona.cat/resources/bcn/CarrilsBici/CARRIL_BICI.geojson'
bike_lane = gpd.read_file(bike_url)
bike_lane = bike_lane.loc[:,['ID','geometry']]
bike_lane.to_crs(epsg=2062, inplace=True)

lanes_districts = gpd.sjoin(districts, bike_lane, how='inner', predicate='intersects')

# visualize bike lanes ontop of district map (Figure_3)
ax = lanes_districts.plot(column='NOM', figsize=(12,6), alpha = 0.5, legend=True)
contextily.add_basemap(ax, crs=lanes_districts.crs.to_string())
bike_lane.plot(ax=ax, color='black')
plt.title('Detailed Map of Barcelona with bike lanes')
plt.axis('off')
plt.show()