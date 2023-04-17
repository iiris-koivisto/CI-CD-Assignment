import webbrowser


km = 12.25
mi = 7.38

mi_to_km = mi * 1.61
km_to_mi = km / 1.61

print(mi, "miles is", round(mi_to_km, 2), "kilometers")
print(km, "kilometers is", round(km_to_mi, 2), "miles")

webbrowser.open("https://github.com/marketplace/actions/broken-link-check")