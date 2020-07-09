import pandas as pd
import simplekml

kml=simplekml.Kml()

df = pd.read_excel("Coordinates.xlsx", index_col = 0)




for i in range(len(df)):
    print(".", end="")
    kml.newpoint(name = df.index[i], coords = [(df['Location_Lon_[deg]'][i], df['Location_Lat_[deg]'][i])])

kml.save("Coordinates.kml")
