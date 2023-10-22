import tkinter as tk
import requests
from tkinter import messagebox
def send_request():
    url = 'http://localhost:8081/addLog'  # 修改为您的URL接口
    # 从编辑框获取数据
    param1_value = entry_params[0].get()
    param2_value = entry_params[1].get()
    param3_value = entry_params[2].get()
    param4_value = entry_params[3].get()
    param5_value = entry_params[4].get()
    param6_value = entry_params[5].get()
    param7_value = entry_params[6].get()
    param8_value = entry_params[7].get()
    param9_value = entry_params[8].get()
    param10_value = entry_params[9].get()
    param11_value = entry_params[10].get()
    param12_value = entry_params[11].get()
    param13_value = entry_params[12].get()

    # 构建请求参数
    data = {
        'toRadio': param1_value,
        'frequency': param2_value,
        'mode': param3_value,
        'myRst': param4_value,
        'toRst': param5_value,
        'myPower': param6_value,
        'toPower': param7_value,
        'qth': param8_value,
        'rig': param9_value,
        'ant': param10_value,
        'myRadio': param11_value,
        'time': param12_value,
        'id': param13_value
    }



    try:
        # 发送 HTTP 请求
        response = requests.post(url, data=data)

        # 检查响应状态码
        if response.status_code == 200:
            # 请求成功
            print('请求成功！')
            print('响应内容：', response.text)
            messagebox.showinfo('请求结果', '请求成功！\n\n响应内容：' + response.text)
        else:
            # 请求失败
            print('请求失败！')
            print('错误代码：', response.status_code)
            messagebox.showerror('请求结果', '请求失败！\n\n错误代码：' + str(response.status_code))
    except requests.RequestException as e:
        # 请求异常
        print('请求发生异常：', str(e))
        messagebox.showerror('请求结果', '请求发生异常：' + str(e))

# 创建主窗口
window = tk.Tk()
window.title('HamLog添加记录')

# 参数标签和编辑框的文本
parameter_labels = [
    '对方呼号:', '频道(MHz):', '模式:', '己方信号:', '对方信号:',
    '己方功率(W):', '对方功率(W):', '地理位置:', '设备:', '天线:',
    '己方呼号:', '时间:', 'id:'
]

# 创建参数标签和编辑框，并放置在网格中
entry_params = []
for i, label_text in enumerate(parameter_labels):
    row = i % 13
    column = i // 13

    label = tk.Label(window, text=label_text)
    label.grid(row=row, column=column*2, padx=5, pady=5, sticky='e')

    entry = tk.Entry(window,width=50)
    entry.grid(row=row, column=column*2+1, padx=5, pady=5, sticky='w')

    entry_params.append(entry)

# 创建按钮
button_send = tk.Button(window, text='添加记录', command=send_request)
button_send.grid(row=13, column=0, columnspan=2, padx=5, pady=10)

# 运行主循环
window.mainloop()