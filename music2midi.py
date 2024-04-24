import os
# os.system("pip install gradio==4.24.0")
import gradio as gr
from scipy.io.wavfile import write
import sys
from basic_pitch import ICASSP_2022_MODEL_PATH
import shutil

from basic_pitch.inference import predict_and_save, Model

basic_pitch_model = Model(ICASSP_2022_MODEL_PATH)
INPUT_MIDI_PATH = './out/htdemucs/test/'
OUT_MIDI_PATH = './out/htdemucs/midi/'


def inference(audio):
    os.makedirs(OUT_MIDI_PATH, exist_ok=True)
    write('test.wav', audio[0], audio[1])
    os.system("demucs -n htdemucs -d cpu test.wav -o out -j 4")

    shutil.rmtree(OUT_MIDI_PATH)
    os.makedirs(OUT_MIDI_PATH, exist_ok=True)
    song_list = os.listdir(INPUT_MIDI_PATH)
    input_list = [os.path.join(INPUT_MIDI_PATH, s) for s in song_list if '.DS_Store' not in s]
    predict_and_save(
    input_list, 
    OUT_MIDI_PATH, 
    model_or_model_path=basic_pitch_model,
    save_midi= True, sonify_midi= False, save_model_outputs=False, save_notes=False
)
    return "./out/htdemucs/test/vocals.wav","./out/htdemucs/test/bass.wav",\
    "./out/htdemucs/test/drums.wav","./out/htdemucs/test/other.wav",\
    "./out/htdemucs/midi/vocals_basic_pitch.mid", \
    "./out/htdemucs/midi/bass_basic_pitch.mid", \
    "./out/htdemucs/midi/drums_basic_pitch.mid", \
    "./out/htdemucs/midi/other_basic_pitch.mid"
  
title = "Demucs"
description = "Gradio demo for Demucs: Music Source Separation in the Waveform Domain. To use it, simply upload your audio, or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/1911.13254' target='_blank'>Music Source Separation in the Waveform Domain</a> | <a href='https://github.com/facebookresearch/demucs' target='_blank'>Github Repo</a></p>"

examples=[['music_condition.mov']]
gr.Interface(
    inference, 
    gr.components.Audio(type="numpy", label="Input"), 
    [gr.components.Audio(type="filepath", label="Vocals"),gr.components.Audio(type="filepath", label="Bass"),gr.components.Audio(type="filepath", label="Drums"),gr.components.Audio(type="filepath",label="Other"), \
    gr.components.File(type="filepath", label="Vocals midi"),gr.components.File(type="filepath", label="Bass midi"),gr.components.File(type="filepath", label="Drums midi"),gr.components.File(type="filepath",label="Other midi")],
    title=title,
    description=description,
    article=article,
    examples=examples,
    # enable_queue=True
    ).launch(debug=True)
