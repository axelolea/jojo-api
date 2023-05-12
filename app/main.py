from fastapi import FastAPI

# Routers
from app.characters.router import router as characters_router
from app.stands.router import router as stands_router
from app.parts.router import router as parts_router
from app.images.router import router as images_router

# App
app = FastAPI()

# Include router
app.include_router(characters_router, prefix='/characters', tags=['Characters'])
app.include_router(stands_router, prefix='/stands', tags=['Stands'])
app.include_router(parts_router, prefix='/parts', tags=['Parts'])
app.include_router(images_router, prefix='/images', tags=['Images'])


@app.get('/')
async def index():
    return {
        'msg': 'Jojo Api'
    }
