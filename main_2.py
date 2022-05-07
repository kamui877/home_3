import requests


class YaUploader:
    host = "https://cloud-api.yandex.net:443"

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        link = f'{self.host}/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': True}
        resp = requests.get(link, headers=headers, params=params)
        requests.put(resp.json()['href'], files={'file': file_path})


if __name__ == '__main__':
    path_to_file = '/test.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


