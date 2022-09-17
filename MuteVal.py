from win32gui import GetWindowText, GetForegroundWindow
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time


ValProcess = 'VALORANT-Win64-Shipping.exe'
Bagaio = 'RiotClientServices.exe'
Status = 0
StatusVOIP = 0

def SetAudio(volume2Use):
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		volume = session._ctl.QueryInterface(ISimpleAudioVolume)
		if session.Process and session.Process.name() == ValProcess or session.Process and session.Process.name() == Bagaio: 
			volume.SetMasterVolume(volume2Use, None)

def SetAudioVOIP(Volumeiro):
	sessionsVOIP = AudioUtilities.GetAllSessions()
	for sessionVP in sessionsVOIP:
		volumeVOIP = sessionVP._ctl.QueryInterface(ISimpleAudioVolume)
		if sessionVP.Process and sessionVP.Process.name() == Bagaio: 
			volumeVOIP.SetMasterVolume(Volumeiro, None)


def MuteValorant():
	global Status
	if Status == 0:
		SetAudio(0.0)
		Status = 1


def UnMuteValorant():
	global Status
	if Status == 1:
		SetAudio(0.85)
		Status = 0

while True:
	time.sleep(0.1);
	Game = (GetWindowText(GetForegroundWindow()))
	if Game == "VALORANT  ":
		UnMuteValorant();
	else:
		MuteValorant();



