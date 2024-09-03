from app import Application
from di_builder import di

app = di.resolve(Application)
app.run()
