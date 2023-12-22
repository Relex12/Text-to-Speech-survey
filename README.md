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
