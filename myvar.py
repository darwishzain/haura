from win32api import GetSystemMetrics #screen resolution
appName = "Haura System"
tab = ["Home", "Settings", "Misc", "About"]

mainColor = '#f3c300'
subColor = '#515356'


#size respective to screen size
fWidth = str(GetSystemMetrics(0))#get screen resolution(width) -> into string
fHeight = str(GetSystemMetrics(1))#get screen resolution(height) -> into string

hWidth = str(GetSystemMetrics(0)/2)
hHeight = str(GetSystemMetrics(0)/2)
qWidth = str(GetSystemMetrics(0)/4)
qHeight = str(GetSystemMetrics(0)/4)

