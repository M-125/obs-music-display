import sys
from obswebsocket import obsws,requests

currentscene=""
previousscene=""



sys.path.append('../')


host = "localhost"
port = 4455
password = open("obspass").readline().removesuffix("\n")

ws = obsws(host, port, password)


def switchscene(name:str):
     ws.connect()
     ws.call(requests.SetCurrentProgramScene(sceneName=name))
     global currentscene
     global previousscene
     previousscene=currentscene
     currentscene=name
     ws.disconnect()
def undoswitchscene():
    switchscene(previousscene)
def settext(textname,content):
     ws.connect()
     ws.call(requests.SetInputSettings(inputName=textname,inputSettings={"text":content}))
     ws.disconnect()



