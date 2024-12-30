from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read__root():
    return {'message': 'Hello, World!'}
