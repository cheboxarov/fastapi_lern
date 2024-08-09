from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel
import uvicorn

app = FastAPI()

class UserCreate(BaseModel):
    email: EmailStr

items = [
    'asdasd',
    'gfsdgdfg',
    'gffgfg'
]


@app.get('/')
def hello_index():
    return {'result': 'hello world'}


@app.get('/hello')
def hello(name: str = 'World'):
    name.strip().title()
    return {
        'message': f'Hello {name}'
    }


@app.get('/items')
def get_items():
    return {'result': items}

@app.post('/users')
def create_user(user: UserCreate):
    return {
        'message': 'success',
        'email': user.email
    }

@app.post('/calc/add')
def add(a: int = Body(), b: int = Body()):
    return {'result': a+b}


@app.get('/items/latest')
def get_latest_item():
    return {'result': items[-1]}


@app.get('/items/{item_id}')
def get_item_by_id(item_id: int):
    print(item_id)
    return {'result': items[item_id]}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
