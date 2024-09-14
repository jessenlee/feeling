import numpy as np
import matplotlib.pyplot as plt

# 读取TXT文件中的第一行波形数据
def read_single_waveform(file_path):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i == 5:  # 只读取第一行
                waveform = np.fromstring(line, sep=' ')
                return waveform
    return None

def subtract_baseline(waveform, num_baseline_points=50):
    baseline = np.mean(waveform[:num_baseline_points])
    print(baseline)
    return waveform - baseline
# 绘制波形图
def plot_waveform(waveform):
    if waveform is not None:
        plt.figure(figsize=(10, 4))
        plt.plot(waveform)
        plt.title('Waveform')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')
        plt.xlim(0,10000)
        plt.grid(True)
        plt.show()
    else:
        print("No waveform data to plot.")

# 主函数
def main():
    input_file = r'G:\alpha能谱Ar.txt'  # 你的TXT文件路径
    waveform = read_single_waveform(input_file)
    subtract_baseline(waveform,50)
    plot_waveform(waveform)

# 运行主函数
if __name__ == '__main__':
    main()