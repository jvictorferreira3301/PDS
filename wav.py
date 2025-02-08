''''''
# EC01045 - PROCESSAMENTO DIGITAL DE SINAIS (2024 .4 - T01)
# Faculdade de Engenharia da Computação e Telecomunicações - Universidade Federal do Pará
# Professor: Ronaldo de Freitas Zampolo 
# Aluno: Joao Victor Santos Brito Ferreira
# Tarefa 1 - Audio Wav
''''''

from pydub import AudioSegment
from scipy.io import wavfile
import matplotlib.pyplot as plt

def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")

def cut_first_10_seconds(wav_path, output_path):
    sample_rate, data = wavfile.read(wav_path)
    cut_data = data[10 * sample_rate:]  
    wavfile.write(output_path, sample_rate, cut_data)
    return sample_rate, cut_data

def plot_wav_info(sample_rate, data):
    bits_per_sample = data.dtype.itemsize * 8
    print(f"Frequência de amostragem: {sample_rate} Hz")
    print(f"Quantidade de bits por amostra: {bits_per_sample} bits")
    
    plt.figure(figsize=(10, 4))
    plt.plot(data)
    plt.title('Waveform')
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.show()

mp3_path = 'REMO.mp3'
wav_path = 'REMO.wav'
cut_wav_path = 'REMO_CUT.wav'

convert_mp3_to_wav(mp3_path, wav_path)
sample_rate, cut_data = cut_first_10_seconds(wav_path, cut_wav_path)
plot_wav_info(sample_rate, cut_data)