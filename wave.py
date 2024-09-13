import numpy as np
import matplotlib.pyplot as plt

# 读取TXT文件中的第一行波形数据
def read_single_waveform(file_path):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if i == 4:  # 只读取第一行
                waveform = np.fromstring(line, sep=' ')
                return waveform
    return None

# 绘制波形图
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
    input_file = r'G:\Ar2.txt'  # 你的TXT文件路径
    waveform = read_single_waveform(input_file)
    plot_waveform(waveform)

# 运行主函数
if __name__ == '__main__':
    main()