import requests

response = requests.get("https://mempool.space/api/v1/fees/recommended")
fees = response.json()
print(f"Fast (10 min): {fees['fastestFee']} sat/vB")
print(f"Medium (30 min): {fees['halfHourFee']} sat/vB")
print(f"Low (1 hour): {fees['hourFee']} sat/vB")
