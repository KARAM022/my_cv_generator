from app.utils.image import prepare_avatar
from app.main import CVGenerator

if __name__ == "__main__":
    prepare_avatar()
    CVGenerator().save()