# Обучение фреймворку FastAPI

## Инициализация проекта
Чтобы создать приложение FastAPI, нужно инициализировать FastAPI() и запустить данный объект через uvicorn
```python
app = FastAPI() # Создание приложения FastAPI
```
``
uvicorn app_name:app``

## Открытие роута


Чтобы открыть роут, нужно указать над вьюшкой декоратор приложения FastAPI, укажите требуемый метод (get), в аргументы передайте сам роут.
```python
@app.get('/')
def hello_index():
    return {'result': 'hello world'}
```

## Передача query параметров
Чтобы принимать query params в свою view, укажите в аргументах к вью эти параметры.
```python
@app.get('/hello')
def hello(name: str = 'World'):
    name.strip().title()
    return {
        'message': f'Hello {name}'
    }
```

## Обработка POST запосов
Чтобы обработать пост запрос, откройте роут на метод post, укажите параметры View, и сделайте им значение по умолчанию Body(), так эти аргументы будут браться из тела запроса.
```python
@app.post('/calc/add')
def add(a: int = Body(), b: int = Body()):
    return {'result': a+b}
```

## Обработка динамических путей
Чтобы обработать динамический путь, в роуте нужно указать значение, которое будет изменяться
в фигурных скобках.
```python
@app.get('/items/{item_id}')
def get_item_by_id(item_id: int):
    print(item_id)
    return {'result': items[item_id]}
```

## Обработка POST запроса через модель
Для удобной обработки post запросов используется модель тела запроса.
```python
class UserCreate(BaseModel):
    email: EmailStr
```
Далее в view, указываем что в теле должен прийти body эквивалентный данной модели
```python
@app.post('/users')
def create_user(user: UserCreate):
    return {
        'message': 'success',
        'email': user.email
    }
```
