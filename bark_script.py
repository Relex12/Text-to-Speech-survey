# TODO: move in python code of readme and delete this file

##############
# Short text #
##############

# from bark import preload_models, generate_audio, SAMPLE_RATE
# from scipy.io.wavfile import write as write_wav

# # download and load all models
# preload_models()

# # generate audio from text
# f = open("lorem-ispum.txt", "r")
# audio_array = generate_audio(f.read())

# # save audio to disk
# write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)


#############
# Long text #
#############

# import os

# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# from IPython.display import Audio
# import nltk  # we'll use this to split into sentences
# import numpy as np
# from scipy.io.wavfile import write as write_wav

# from bark.generation import (
#     generate_text_semantic,
#     preload_models,
# )
# from bark.api import semantic_to_waveform
# from bark import generate_audio, SAMPLE_RATE

# f = open("lorem-ispum.txt", "r")
# script = f.read().replace("\n", " ").strip()

# nltk.download('punkt')

# sentences = nltk.sent_tokenize(script)

####################
# Simple long text #
####################

# SPEAKER = "v2/en_speaker_6"
# silence = np.zeros(int(0.25 * SAMPLE_RATE))  # quarter second of silence

# pieces = []
# for sentence in sentences:
#     audio_array = generate_audio(sentence, history_prompt=SPEAKER)
#     pieces += [audio_array, silence.copy()]

# write_wav("bark_generation.wav", SAMPLE_RATE, np.concatenate(pieces))

# Audio(np.concatenate(pieces), rate=SAMPLE_RATE)

######################
# Advanced long text #
######################

# GEN_TEMP = 0.6
# SPEAKER = "v2/en_speaker_6"
# silence = np.zeros(int(0.25 * SAMPLE_RATE))  # quarter second of silence

# pieces = []
# for sentence in sentences:
#     semantic_tokens = generate_text_semantic(
#         sentence,
#         history_prompt=SPEAKER,
#         temp=GEN_TEMP,
#         min_eos_p=0.05,  # this controls how likely the generation is to end
#     )

#     audio_array = semantic_to_waveform(semantic_tokens, history_prompt=SPEAKER,)
#     pieces += [audio_array, silence.copy()]

# Audio(np.concatenate(pieces), rate=SAMPLE_RATE)