import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal
from thinkdsp import decorate

signal = TriangleSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
decorate(xlabel='Time (s)')
plt.subplot(121)
segment.plot()

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.subplot(122)
segment.plot()
plt.show()
