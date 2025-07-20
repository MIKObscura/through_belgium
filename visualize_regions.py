import matplotlib.pyplot as plt
import json

stations = json.loads(open("stations.json").read())

per_region = {
    "Wallonie": 6,
    "Vlaanderen": 4,
    "Bruxelles-Capitale": 0
}
for s in stations:
    per_region[s["region"]] += 1

plt.bar(per_region.keys(), per_region.values())
plt.title("Amount of stations per region")
plt.savefig("region.png")
plt.clf()

region_per_sqm = {
    "Wallonie": per_region["Wallonie"] / 169.01,
    "Vlaanderen": per_region["Vlaanderen"] / 136.26,
    "Bruxelles-Capitale": per_region["Bruxelles-Capitale"] / 1.6242
}
plt.bar(region_per_sqm.keys(), region_per_sqm.values())
plt.title("Amount of stations per 100 km² for each region")
plt.savefig("region_sqm.png")
plt.clf()

region_per_capita = {
    "Wallonie": per_region["Wallonie"] / 36.92283,
    "Vlaanderen": per_region["Vlaanderen"] / 68.21770,
    "Bruxelles-Capitale": per_region["Bruxelles-Capitale"] / 12.49597
}
plt.bar(region_per_capita.keys(), region_per_capita.values())
plt.title("Amount of station per 100k inhabitants per region")
plt.savefig("region_capita.png")
plt.clf()