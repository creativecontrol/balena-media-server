## Fasting Girls - an OMXPlayer Network Media System with Remote Control

This implementation uses:
- Raspbian Buster Lite on Raspberry Pi 3 B+
https://www.raspberrypi.org/downloads/raspbian/

- OMXPlayer
https://github.com/popcornmix/omxplayer

- OMXPlayer Wrapper
https://github.com/willprice/python-omxplayer-wrapper

- python-osc
https://pypi.org/project/python-osc/

Is is intended to be used with OSC remote control via QLab but could be used
by any OSC capable client. An test file for QLab is included.

**The following OMXPlayer features have been implemented**

- Load: */load <filename> <pause=False>*
- Play: */play*
- Pause: */pause*
- Stop: */stop*
- Mute: */mute*
- Unmute: */unmute*
- Alpha: */alpha <0..255>*
- Action: */action <key>*  https://python-omxplayer-wrapper.readthedocs.io/en/latest/omxplayer/#module-omxplayer.keys
- Rate: */rate <float>*
- Seek: */seek <relative position : seconds>*
- Position: */position <position from start : seconds>*
- Video position: */video_pos <top left> <top right> <bottom right> <bottom left>*
- Video Crop: */video_crop <top left> <top right> <bottom right> <bottom left>*
- Aspect: */aspect <"letterbox" | "fill" | "stretch">*
