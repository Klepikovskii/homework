import json
import requests
from pprint import pprint

# def super_heroes():
#     url = "https://akabab.github.io/superhero-api/api/all.json"
#     response = requests.get(url)
#     list_one = response.json()

#     for heroes in list_one:
#         name = heroes['name']
#         if name == 'Hulk':
#             Hulk_intelligence = heroes['powerstats']['intelligence']
#         elif name == 'Captain America':
#             Captain_America_intelligence = heroes['powerstats']['intelligence']
#         elif name == 'Thanos':
#             Thanos_intelligence = heroes['powerstats']['intelligence']
#     if  Hulk_intelligence > Captain_America_intelligence and Hulk_intelligence > Thanos_intelligence:
#         print(f'Hulk самый сильный')
#     elif Captain_America_intelligence > Thanos_intelligence and Captain_America_intelligence > Hulk_intelligence:
#         print(f'Captain_America самый сильный')
#     else: print(f'Thanos самый сильный') 
     


        


# if __name__ == '__main__':
#     super_heroes()



# Задача №2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url =  'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            "path": file_path
        }
        headers = {
            "Authorization": token
        }
        response = requests.get(url, headers=headers, params=params)
        print(response.json())
        url_for_upload = response.json().get('href', '')
        with open('IMG_4946.JPG', 'rb') as file:
            response_upload = requests.put(url_for_upload, files={"file": file})
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'Homework/IMG_4946.JPG'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)