# JSON is commonly used with data APIs. Here's how we can parse JSON into a python dictionary
# if u call this file json.py we get a conflict because that's the name of the module
# That's why we call it py_json.py

# Let's import a json module
import json

# creating a Json(double Quotes is JSON Format)
CameraFXSettingsJSON = '{"Motion Blur":"Maximum","Vignette":"Rounded","Ambient Oclussion Distance":2.0}'
 
#  Parse to dictionary
cameraFX = json.loads(CameraFXSettingsJSON)
print(cameraFX) 
print(cameraFX['Motion Blur'])

# Creating a dictionary
cameraLens = {'Shutter':5.2,'model':'CANON X789'}

cameraLensJSON = json.dumps(cameraLens)
# Serialize object to formatted JSON

print (cameraLensJSON)
