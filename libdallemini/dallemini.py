import requests
import logging
'''from ..utils.client_id_gen import ci_renew
from ..utils.misc import *
import os
'''
logging.basicConfig(filename="events.log", level=logging.DEBUG,format="%(asctime)s %(message)s")

class ImageGenerator:
    def __init__(self):
        print('[+] Dall-e Mini Engine started....')
    
    def upload_imgur(self, b64_image, client_id):
        headers = {
            'authorization': f'Client-Id {client_id}'
        }
        params = {
            'image': b64_image
        }
        UPLOAD_API_URL = 'https://api.imgur.com/3/image'
        response = requests.post(UPLOAD_API_URL, headers=headers, data=params)
        try:
            return response.json()['data']['id']
            '''except IndexError:
            raw_client_ids = os.environ.get('IMGUR_CLIENT_IDS_RAW')
            new_client_id, idx = ci_renew(keyword, raw_client_ids)
            reinit
            os.environ["IMGUR_CLIENT_ID="] = new_client_id
            self.upload_imgur(b64_image, client_id)'''
        except Exception as e:
            logging.error(f"[-] Looks like something unusual happened with Imgur API. Please check the logs:\n{e}")
            return None
        
    def get_image(self, keyword: str, client_id):
        GENERATE_API_URL  ='https://backend.craiyon.com/generate'
        headers = { 
            'accept': 'application/json',   
            'content-type': 'application/json'
        }
        data= f'{{"prompt":"{keyword}"}}'
        response = requests.post(url=GENERATE_API_URL, headers=headers, data=data,  stream=True)
        try:
            images = []
            for j,i in enumerate(response.json()['images']):
                logging.debug(f'[{j}] Uploading image...')
                uploaded_link = self.upload_imgur(i, client_id)
                if uploaded_link==None:
                    return i
                images.append(uploaded_link)
            return images
        except Exception as e:
            logging.error(f"[-] Something unexpected has happened with Craiyon API. Please check the logs:\n{e}")
            return -1
