# Outils de synthèse vocale

## EDGE-TTS

```bash
pip install edge-tts
edge-tts --list-voices
edge-tts --list-voices | grep fr
edge-tts --voice fr-FR-HenriNeural --file lorem-ispum.txt --write-media lorem.mp3
```

## GTTS

```bash
pip install gTTS
gtts-cli --lang fr --file lorem-ispum.txt --output lorem.mp3
```

* Coupe tous les 100 caractères

## SVOXPICO

```bash
sudo apt install libttspico-utils
cat lorem-ispum.txt | pico2wave --lang fr-FR --wave lorem.wav
```

## ESPEAK + MBROLA

```bash
sudo apt install espeak-ng-espeak mbrola
cat lorem-ispum.txt | espeak -v fr -w lorem.wav   # use default espeak french voice
espeak --version                                  # get espeak data location
espeak --voices=fr                                # list french voices
sudo apt install mbrola-fr1 mbrola-fr2 mbrola-fr3 # download Mbrola voices
sudo apt install mbrola-fr4 mbrola-fr5 mbrola-fr6 mbrola-fr7
for i in `echo "1 2 3 4 5 6 7"` ; do $(cat lorem-ispum.txt | espeak -v french-mbrola-$i -w lorem.$i.wav) ; done
```

## FESTIVAL

```bash
sudo apt install festival
cat lorem-ispum.txt | text2wave -o lorem.wav
```

## SOX

* Converti les WAV en MP3

```bash
sudo apt install sox libsox-fmt-mp3
sox --type wav --channels 1 lorem.wav --type mp3 lorem.mp3
```

# TODO

* Tableau comparatif
* Liste de critères

## TORTOISE TTS

* https://github.com/neonbjb/tortoise-tts

```bash
pip install tortoise-tts
tortoise_tts.py --help
```

## BARK

* TODO: fichiers longs et CLI

```bash
pip install git+https://github.com/suno-ai/bark.git
python3 -m bark --text "Hello, my name is Suno." --output_filename "example.wav"
```

```python
from bark import preload_models generate_audio SAMPLE_RATE
from scipy.io.wavfile import write as write_wav
preload_models()                                             # download and load all models
f = open("lorem-ipsum.txt", "r")                             # generate audio from text
audio_array = generate_audio(f.read())
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)   # save audio to disk
```

* Le nom de fichier ne doit pas être `bark.py`
* Supporte les langues étrangères et les instructions comme [laughs] [sighs] [music] [gasps]

## TERMUX-TTS-SPEAK

Sur Termux:

```bash
pkg install termux-tts-speak
termux-tts-speak "Faites demi-tour dès que possible !"
```

* Enregistrement du son interne avec pyaudio

```bash
pkg install python3 wget
python -m pip install -U pip
wget https://its-pointless.github.io/setup-pointless-repo.sh
bash setup-pointless-repo.sh
rm setup-pointless-repo.sh
pkg install portaudio portaudio-dev
python -m pip install pyaudio
```

* A voir comment enregistrer le son interne avec pyaudio

# Autres divers

## Liens utiles

* Wiki Ubuntu fr : https://doc.ubuntu-fr.org/synthese_vocale
* From Reddit : https://tuxicoman.jesuislibre.net/2015/05/synthese-vocale-sous-linux.html
* Phonemizer : https://github.com/bootphon/phonemizer
* Docker-tts : https://github.com/ozzyjohnson/docker-tts
* YouTube : V2F - IA JDG

## Scrapping Wikidot et Wikimedia

* [Wikimedia API](https://www.mediawiki.org/wiki/API:Main_page), notamment *Get_the_contents_of_a_page*
  * exemple : https://creepypasta.fandom.com/fr/api.php?action=parse&format=json&formatversion=2&page=Smile_Dog&prop=wikitext
* [Github de SCP Wiki](https://github.com/scpwiki) qui prend la suite de Wikidot pour SCP et Backrooms
