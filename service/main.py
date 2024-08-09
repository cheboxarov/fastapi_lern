from fastapi import FastAPI, Body
import uvicorn
from users.views import router as users_router
from items.views import router as items_router


app = FastAPI()
app.include_router(items_router, tags=['Items'])
app.include_router(users_router, tags=['Users'])

@app.get('/')
def hello_index():
    return {'result': 'hello world'}


@app.get('/hello')
def hello(name: str = 'World'):
    name.strip().title()
    return {
        'message': f'Hello {name}'
    }


@app.post('/calc/add')
def add(a: int = Body(), b: int = Body()):
    return {'result': a+b}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='0.0.0.0', port=8000)
