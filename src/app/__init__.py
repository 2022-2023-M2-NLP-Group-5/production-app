import os
from flask import Flask
from .views import app

app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'minty'   
