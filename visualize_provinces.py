import matplotlib.pyplot as plt
import json

stations = json.loads(open("stations.json").read())

per_province = {
    "Hainaut": 4,
    "Namur": 2,
    "Brabant Wallon": 0,
    "Liège": 0,
    "Luxembourg": 0,
    "Limburg": 0,
    "Vlaams Brabant": 0,
    "Antwerpen": 0,
    "Oost Vlaanderen": 4,
    "West Vlaanderen": 0
}
for s in stations:
    if s["region"] == "Bruxelles-Capitale":
        continue
    per_province[s["province"]] += 1
print(per_province)

plt.bar(per_province.keys(), per_province.values())
plt.tight_layout()
plt.title("Amount of stations per province")
plt.xticks(rotation=60, fontsize=8)
fig = plt.gcf()
fig.set_size_inches((10, 11))
plt.savefig("province.png", dpi=100)
plt.clf()

province_sqm = {
    "Hainaut": per_province["Hainaut"] / 38.13,
    "Namur": per_province["Namur"] / 36.75,
    "Brabant Wallon": per_province["Brabant Wallon"] / 	10.97,
    "Liège": per_province["Liège"] / 38.57,
    "Luxembourg": per_province["Luxembourg"] / 44.59,
    "Limburg": per_province["Limburg"] / 24.27,
    "Vlaams Brabant": per_province["Vlaams Brabant"] / 21.18,
    "Antwerpen": per_province["Antwerpen"] / 28.76,
    "Oost Vlaanderen": per_province["Oost Vlaanderen"] / 30.07,
    "West Vlaanderen": per_province["West Vlaanderen"] / 31.97
}
print(province_sqm)

plt.bar(province_sqm.keys(), province_sqm.values())
plt.tight_layout()
plt.title("Amount of stations per 100 km² per province")
plt.xticks(rotation=60, fontsize=6)
fig = plt.gcf()
fig.set_size_inches((10, 20))
plt.savefig("province_sqm.png", dpi=100)
plt.clf()

province_capita = {
    "Hainaut": per_province["Hainaut"] / 13.60074,
    "Namur": per_province["Namur"] / 5.03895,
    "Brabant Wallon": per_province["Brabant Wallon"] / 4.14130,
    "Liège": per_province["Liège"] / 11.19038,
    "Luxembourg": per_province["Luxembourg"] / 2.95146,
    "Limburg": per_province["Limburg"] / 9.00098,
    "Vlaams Brabant": per_province["Vlaams Brabant"] / 11.96773,
    "Antwerpen": per_province["Antwerpen"] / 19.26522,
    "West Vlaanderen": per_province["West Vlaanderen"] / 12.26375,
    "Oost Vlaanderen": per_province["Oost Vlaanderen"] / 15.72002
}
print(province_capita)

plt.bar(province_capita.keys(), province_capita.values())
plt.tight_layout()
plt.title("Amount of stations per 100k inhabitants per province")
plt.xticks(rotation=60, fontsize=5)
fig = plt.gcf()
fig.set_size_inches((10, 30))
plt.savefig("province_capita.png", dpi=100)
plt.clf()