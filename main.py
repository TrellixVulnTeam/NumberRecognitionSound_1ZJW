import os
import wave
import pylab
import numpy as np
from matplotlib import mlab
import matplotlib.pyplot as plt
from scipy.spatial import distance

def find_similarity(userInput, sample):
    distArr = []
    if len(userInput) >= len(sample):
        for i in range(0, len(userInput) - len(sample) + 1):
            dist = 0
            for j in range(0, len(sample)):
                dist += distance.euclidean(userInput[i + j], sample[j])
            distArr.append(dist/len(sample))
        print(min(distArr))
        return min(distArr)
    else:
        print(100)
        return 100

def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    spectrogram, freq, time = mlab.specgram(sound_info, Fs=frame_rate, scale_by_freq=True, sides='default')
    spectrogram = normalize(spectrogram)
    Y = np.log10(np.flipud(spectrogram))
    Z = np.transpose(Y)

    print(Z)
    print('\n\n')
    return Z

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate

if __name__ == '__main__':

    # main ========================================================================================================================
    wav_file = '/number/zero.wav'
    print(str(0) + ' making spectrogram arr')
    zero = graph_spectrogram(wav_file)

    wav_file = '/number/one.wav'
    print(str(1) + ' making spectrogram arr')
    one = graph_spectrogram(wav_file)

    wav_file = '/number/two.wav'
    print(str(2) + ' making spectrogram arr')
    two = graph_spectrogram(wav_file)

    wav_file = '/number/three.wav'
    print(str(3) + ' making spectrogram arr')
    three = graph_spectrogram(wav_file)

    wav_file = '/number/four.wav'
    print(str(4) + ' making spectrogram arr')
    four = graph_spectrogram(wav_file)

    wav_file = '/number/five.wav'
    print(str(5) + ' making spectrogram arr')
    five = graph_spectrogram(wav_file)

    wav_file = '/number/six.wav'
    print(str(6) + ' making spectrogram arr')
    six = graph_spectrogram(wav_file)

    wav_file = '/number/seven.wav'
    print(str(7) + ' making spectrogram arr')
    seven = graph_spectrogram(wav_file)

    wav_file = '/number/eight.wav'
    print(str(8) + ' making spectrogram arr')
    eight = graph_spectrogram(wav_file)

    wav_file = '/number/nine.wav'
    print(str(9) + ' making spectrogram arr')
    nine = graph_spectrogram(wav_file)

    userInput = input()
    print('user input making spectrogram arr')
    example = graph_spectrogram(userInput)

    one = find_similarity(example, one)
    two = find_similarity(example, two)
    three = find_similarity(example, three)
    four = find_similarity(example, four)
    five = find_similarity(example, five)
    six = find_similarity(example, six)
    seven = find_similarity(example, seven)
    eight = find_similarity(example, eight)
    nine = find_similarity(example, nine)
    zero = find_similarity(example, zero)

    print('\n minimal gap distance arr')
    distance = [zero, one, two, three, four, five, six, seven, eight, nine]

    print(distance)

    print(distance.index(min(distance)))



