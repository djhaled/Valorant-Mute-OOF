# Valorant Mute on Focus Loss

Small **Windows quality-of-life script**: mutes Valorant (`VALORANT-Win64-Shipping.exe`) and Riot Client audio when the game window is not focused, and restores audio when you tab back in.

## What it does

- Polls foreground window title
- Mutes/unmutes game and client audio via Windows audio APIs (`pycaw`)

## Why it exists

Background audio from Valorant while multitasking was distracting. Automating mute on alt-tab removes manual volume changes.

## Quick start

```bash
pip install pycaw pywin32
python MuteVal.py
```

Or edit and run `RunValMute.bat` (update Python path inside if needed).

## Requirements

- Windows
- Python 3 with `pycaw` and `pywin32`
- Valorant installed (process names must match running binaries)

## Project status

Personal utility. See commit history.

## License

See repository license file.
