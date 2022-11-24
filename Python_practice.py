counties_tuple = ("Arapahoe","Denver","Jefferson")

print(len(counties_tuple))

counties_dict={}

counties_dict["Araphoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438

print(counties_dict)

print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
counties_dict.get("Denver")

counties_dict['Araphoe']

voting_data=[]

voting_data.append({"county":"Araphoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered voters":463353})
voting_data.append({"county":"Jefferson","registered voters":432438})

print(voting_data)

counties = ["Arapahoe","Denver","Jefferson"]

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties_dict:
    print(counties_dict[county])

for county, voters in counties_dict.items():
    print(county, voters)

for county_dict in voting_data:
    print(county_dict)