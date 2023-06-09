from app.main import app
from app.core.config import get_settings
import uvicorn

settings = get_settings()

if __name__ == '__main__':
    uvicorn.run(
        app,
        reload=True,
        port=settings.port
    )
