import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal
from thinkdsp import decorate
from thinkdsp import SquareSignal

signal = SquareSignal(1100)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
decorate(xlabel='Time (s)')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.subplot(121)
segment.plot()
wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()

decorate(xlabel='Frequency (Hz)')
plt.subplot(122)
spectrum.plot()
plt.show()
