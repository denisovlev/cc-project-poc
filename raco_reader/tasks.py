from raco_reader.celery import app

@app.task
def print_stuff():
    print("background task")
