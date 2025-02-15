import requests
res=requests.get("https://api.open-meteo.com/v1/forecast?latitude=39.56939&longitude=2.65024&hourly=temperature_2m")
datos=res.json()
temp=datos["hourly"]["temperature_2m"]
l=len(temp)
print(f'La temperatura media es {sum(temp)/l}.')