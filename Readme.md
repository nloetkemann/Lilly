# Lilly
- oder Leila (steht für Leila Intelligent Language Assistent)
- oder Diva (steht für Diva Intelligent Voice Assistent)
Name ist also noch nicht sicher

## Installation
For the Server, the terminal programm ffmpeg should be installed

Here is a manual: [Click Here](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
For the Voice Assistent you need to install ``portaudio``
### Requirements
You need several Tokens to run the Server.
You need a
- [WolframAlpha](http://products.wolframalpha.com/) Token
- [Openwather](https://openweathermap.org/) Token
- [Wit](https://wit.ai/) Token
- [Bot Token](https://core.telegram.org/bots) von Telegram 

Wit analyzes your input and it uses a neural network to validate your text.

You can install all required libs with ```make install```
## Start
You need to run the Server first.
### Server
in the Server directory, run the ``main.py``.
### Telegrammclienten
in the TelegrammClient directory, run the ``main.py``.
### Sprachassistenten
in the VoiceClient directory, run the ``main.py``.
### Start with docker-compose
you need an docker-compose.override.yaml file
```
version: '2'

services:
  server:
    environment:
      WIT_TOKEN: 'to_be_set'
      WEATHER_TOKEN: 'to_be_set'
      WOLFRAM_TOKEN: 'to_be_set'

  client:
    environment:
      BOT_TOKEN: 'to_be_set'

```

Alles nur für den privaten Gebrauch.