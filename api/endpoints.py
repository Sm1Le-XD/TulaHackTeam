from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import httpx
import db.db as db



async def get_ps_pages(tg_id):
    url = "https://mc.dev.rand.agency/api/v1/get-access-token"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": token
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code != 200:
                return 'error'
        return response.json()


async def put_ps_page(tg_id, key, new_data):
    url = f"https://mc.dev.rand.agency/api/page/{page_id}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": token
    }
    async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            if response.status_code == 200:
                response = response.json()
                response[key] = new_data
                res2 = await client.put(url, headers=headers, json=response)
            else:
                return 'error'
