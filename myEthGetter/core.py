from requests import get

resp = get("https://eth.nanopool.org/api/v1/load_account/0x9c7fb1d6ccbbd1e2ccb567e2313221a544aedcb2")
print(resp.json()["data"]["userParams"]["balance"])
