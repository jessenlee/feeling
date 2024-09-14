import numpy as np
import matplotlib.pyplot as plt

# 读取TXT文件中的波形数据
def read_waveforms(file_path):
    waveforms = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i % 2 == 1 & i<40000:  # 只处理偶数行
                waveform = np.fromstring(line, sep=' ')
                waveform = waveform[1:8000]  # 只取前10000个数据点
                waveforms.append(waveform)
    return waveforms

# 扣除基线
def subtract_baseline(waveform, num_baseline_points=50):
    baseline = np.mean(waveform[:num_baseline_points])
    return waveform - baseline

# 对单个波形进行数值积分
def integrate_waveform(waveform, threshold=-15):
    baseline = np.mean(waveform[:50])
    return np.sum(waveform[waveform < baseline-5])

# 绘制能谱图
def plot_spectrum(integrals):

    plt.hist(integrals, bins=2048, color='blue', alpha=0.7,range=(0,1000))
    plt.title('Energy Spectrum')
    plt.xlabel('Energy Deposition')
    plt.ylabel('Counts')
    
    plt.grid(True)
    plt.show()

#wave
def plot_waveform(waveform):
    if waveform is not None:
        plt.figure(figsize=(10, 4))
        plt.plot(waveform)
        plt.title('Waveform')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.xlim(1000,10000)
        plt.grid(True)
        plt.show()
    else:
        print("No waveform data to plot.")
# 主函数
def main():
    input_file = r'G:\alpha能谱Ar.txt'  # 你的TXT文件路径
    waveforms = read_waveforms(input_file)
    processed_waveforms = []
    i=0
    for waveform in waveforms:
        processed_waveform = subtract_baseline(waveform)
        processed_waveforms.append(processed_waveform)
    integrals = [abs(integrate_waveform(waveform)) for waveform in processed_waveforms]
    plot_spectrum(integrals)


# 运行主函数
if __name__ == '__main__':
    main()