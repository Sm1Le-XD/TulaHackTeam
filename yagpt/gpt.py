#  работа с ягпт

import requests
import json
import os
import time
from pprint import pprint

from config import IAM_TOKEN, APY_KEY

with open('yagpt/json/main.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
f.close()
data['modelUri'] = "gpt://" + IAM_TOKEN + "/yandexgpt-lite"
with open('yagpt/json/main.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
f.close()


headers = {
    'Authorization': f'Api-Key {APY_KEY}',
}

def epi(text, fio):
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    with open('yagpt/json/main.json', 'r', encoding='utf-8') as f:
        main = json.load(f)
    f.close()
    with open('yagpt/json/epi.json', 'r', encoding='utf-8') as f:
        epi = json.load(f)
    f.close()
    main['messages'] = epi
    main['messages'][-1]['text'] = text
    with open('yagpt/body.json', 'w', encoding='utf-8') as f:
        json.dump(main, f, ensure_ascii=False, indent=4)
    f.close()
    with open('yagpt/body.json', 'r', encoding='utf-8') as f:
        data = json.dumps(json.load(f))
    # pprint(data)
    resp = requests.post(url, headers=headers, data=data)
    pprint(resp)
    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                {resp.status_code}, {resp.text}
            )
        )
    res = resp.json()['result']['alternatives'][-1]['message']['text']
    with open('yagpt/json/ref.json', 'r', encoding='utf-8') as f:
        ref = json.load(f)
    f.close()
    main['messages'] = ref
    main['messages'][-1]['text'] = res + fio
    time.sleep(1)
    with open('yagpt/body.json', 'w', encoding='utf-8') as f:
        json.dump(main, f, ensure_ascii=False, indent=4)
    f.close()
    with open('yagpt/body.json', 'r', encoding='utf-8') as f:
        data = json.dumps(json.load(f))
    pprint("gfgf")
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                {resp.status_code}, {resp.text}
            )
        )
    return resp.json()['result']['alternatives'][-1]['message']['text']


def bio(text, name):
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    with open('yagpt/json/main.json', 'r', encoding='utf-8') as f:
        main = json.load(f)
    f.close()
    with open('yagpt/json/bio.json', 'r', encoding='utf-8') as f:
        epi = json.load(f)
    f.close()
    main['messages'] = epi
    main['messages'][-1]['text'] = text
    with open('yagpt/body.json', 'w', encoding='utf-8') as f:
        json.dump(main, f, ensure_ascii=False, indent=4)
    f.close()
    with open('yagpt/body.json', 'r', encoding='utf-8') as f:
        data = json.dumps(json.load(f))
    # pprint(data)
    resp = requests.post(url, headers=headers, data=data)
    pprint(resp)
    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                {resp.status_code}, {resp.text}
            )
        )
    res = resp.json()['result']['alternatives'][-1]['message']['text']
    with open('yagpt/json/ref.json', 'r', encoding='utf-8') as f:
        ref = json.load(f)
    f.close()
    main['messages'] = ref
    main['messages'][-1]['text'] = res + name
    time.sleep(1)
    with open('yagpt/body.json', 'w', encoding='utf-8') as f:
        json.dump(main, f, ensure_ascii=False, indent=4)
    f.close()
    with open('yagpt/body.json', 'r', encoding='utf-8') as f:
        data = json.dumps(json.load(f))
    pprint("gfgf")
    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                {resp.status_code}, {resp.text}
            )
        )
    return resp.json()['result']['alternatives'][-1]['message']['text']

