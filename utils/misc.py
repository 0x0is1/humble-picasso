import json
import time

def reinit_token(token_idx: int):
    with open('../tokensInfo.json', 'r+') as f:
        data = json.loads(f.read())
        try:
            data['data'][token_idx] = {}
        except IndexError:
            data['data'].append([])
        data['data'][token_idx] = {
            'init_time': round(time.time()),
            'hourly_usage_count': 0
        }
        f.seek(0)
        json.dump(data, f)


def modify_token_data(token_idx: int, usage_count: int):
    with open('../tokensInfo.json', 'r+') as f:
        data = json.loads(f.read())
        if data['data'][token_idx]['hourly_usage_count'] <= 41:
            data['data'][token_idx]['hourly_usage_count'] = usage_count + 9
            f.seek(0)
            json.dump(data, f)
            return 1
        return -1
