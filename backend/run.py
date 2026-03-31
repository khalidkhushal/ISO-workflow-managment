from app import create_app
from utils.database import db

app = create_app()

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, port=5001)