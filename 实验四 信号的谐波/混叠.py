import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal,decorate,SquareSignal,SawtoothSignal,CosSignal

signal = CosSignal(4500)
duration = signal.period*5
segment = signal.make_wave(duration, framerate=10000)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
decorate(xlabel='Time (s)')
plt.subplot(121)
segment.plot()

signal = CosSignal(5500)
duration = signal.period*5
segment = signal.make_wave(duration, framerate=10000)

decorate(xlabel='Frequency (Hz)')
plt.subplot(122)
segment.plot()
plt.show()

