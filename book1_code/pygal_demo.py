import json
import pygal
import math

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建5个列表，分别存储日期、收盘价等数据
dates = []
months = []
weeks = []
weekdays = []
close = []  
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(eval(btc_dict['close']))


# x轴标签顺时针旋转20°，不用显示所有的x轴标签
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False) 
#line_chart = pygal.Bar()
line_chart.title = '收盘价对数变换（元）'
line_chart.x_labels = dates
N = 20 # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变换折线图.svg')
