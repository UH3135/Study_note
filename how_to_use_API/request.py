import requests

BASE_URL = "https://openapi.gg.go.kr/Genrestrtcate?Type=json"

def rejust_data(json_data: list):
    data_list = json_data["Genrestrtcate"][1]['row']
    for data in data_list:
        if data["BSN_STATE_NM"] == "영업":
            print(data["BIZPLC_NM"])    


def get_restarnts_data(city: str):
    i = 1
    arguments = f"&SIGUN_NM={city}&pIndex={i}"
    response = requests.get(BASE_URL+arguments)
    print()
    if response.status_code != 200:
        return []
    
    data = response.json()
    rejust_data(data)


if __name__ == "__main__":
    get_restarnts_data("남양주시")