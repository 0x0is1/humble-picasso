def parse_id(string: str):
    string = string.replace('[`](https://www.example.com/?id=-', '').replace(')', '')
    string = string.split('-')
    curr_idx = int(string[-1])
    string.pop(-1)
    return string, curr_idx

