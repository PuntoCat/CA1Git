from app import create_app  # from the app package __init__

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
    flask_app.run()
