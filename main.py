from fastapi import FastAPI

app = FastAPI()


@app.get("/root")
def read_root():
    return {
        "Hello": "World",
        "name": "Jorge",
        "age": 35,
        "casado": True,
    }
