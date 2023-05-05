#! /usr/bin/env python# -*- coding: utf-8 -*-
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
"""
绘制加速比柱状图
Author：shaomingshan
Input：
    version：需要对比的版本
    speedup：加速比
"""


import matplotlib.pyplot as plt
import numpy as np

# 3072k
knl = 1.24
p100_1x = 1.96
p100_2x = 3.53
v100_1x = 2.58
v100_2x = 3.85
sw_32 = 1.12
sw_64 = 2.24
sw_128 = 4.50

# 1536k
# knl = 1.755
# gold = 6.254
# p100_1x = 6.671
# p100_2x = 9.746
# sw_4 = 0.299


ns_day = [sw_128, sw_64, sw_32, v100_2x, v100_1x, p100_2x, p100_1x, knl]
version = ['32X SW', '16X SW', '8X SW', '2X V100', '1X V100', '2X P100', '1X P100', 'KNL']
# ns_day = [sw_4, p100_2x, p100_1x, gold, knl]
# version = ['4X SW', '2X P100', '1X P100', 'GOLD', 'KNL']

margin_top = 0.6
margin_right = 0.5
width, height = 3.5, 2  # inch
title = u''
xlabel = u'ns/day'
ylabel = u''
bar_width = 0.5
text_size = 8
font_size = 7
legend1 = 'SW'
legend2 = 'V100'
legend3 = 'P100'
legend4 = 'KNL'
grid_color = '#d9d9d9'
# dark
# color4 = '#b3e5cc'  # 绿
# color3 = '#f7e8b1'  # 黄
# color2 = '#9fbfdf'  # 蓝
# color1 = '#d98c8c'  # 红

# light
# color4 = '#d5e8d4'  # 绿
# color3 = '#eeeeee'  # 灰
# color2 = '#dae8fc'  # 蓝
# color1 = '#e1d5e7'  # 紫

# color1 = '#d0beda'  # 紫
# color2 = '#9fbfdf'  # 蓝
# color3 = '#d9d9d9'  # 灰
# color4 = '#b3e5cc'  # 绿

color1 = '#dccfe2'  # 紫
color2 = '#b3d8ff'  # 蓝
color3 = '#d9d9d9'  # 灰
color4 = '#b3e5cc'  # 绿

linewidth = 0.1
edgecolor = "#4d4d4d"


def get_max(data):
    max_num = float('-inf')
    for i in data:
        max_num = i if i > max_num else max_num
    return max_num


def draw(save_path):
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

    fig = plt.figure()
    fig.set_size_inches(width, height)
    # plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)
    plt.subplots_adjust(left=0.18, bottom=0.17)

    # 3072k
    plt.barh([7], ns_day[7], height=bar_width, linewidth=linewidth, edgecolor=edgecolor,
             tick_label=[7], color=color1, alpha=0.9, label=legend4, zorder=0)
    plt.barh([5, 6], ns_day[5:7], height=bar_width, linewidth=linewidth, edgecolor=edgecolor,
             tick_label=[5, 6], color=color2, alpha=0.9, label=legend3, zorder=0)
    plt.barh([3, 4], ns_day[3:5], height=bar_width, linewidth=linewidth, edgecolor=edgecolor,
             tick_label=[3, 4], color=color3, alpha=0.9, label=legend2, zorder=0)
    plt.barh([0, 1, 2], ns_day[0:3], height=bar_width, linewidth=linewidth, edgecolor=edgecolor,
             tick_label=[0, 1, 2], color=color4, alpha=0.9, label=legend1, zorder=0)
    # 1536k
    # plt.barh([4], ns_day[4], height=bar_width,
    #          tick_label=[4], color=color1, alpha=0.9, label=legend4, zorder=0)
    # plt.barh([2, 3], ns_day[2:4], height=bar_width,
    #          tick_label=[2, 3], color=color2, alpha=0.9, label=legend3, zorder=0)
    # plt.barh([1], ns_day[1], height=bar_width,
    #          tick_label=[1], color=color3, alpha=0.9, label=legend2, zorder=0)
    # plt.barh([0], ns_day[0], height=bar_width,
    #          tick_label=[0], color=color4, alpha=0.9, label=legend1, zorder=0)

    # plt.bar(range(len(ns_day)), ns_day, width=bar_width,
    #         tick_label=version, color=color, alpha=0.9, label=legend1, zorder=0)

    # # 补-1到0之间gap
    # gap_bar = [-1, -1, -1, -1, -1]
    # plt.bar(range(len(ns_day)), gap_bar, width=bar_width,
    #         tick_label=version, color=color, alpha=0.9, zorder=0)

    for x, y, v in zip(np.arange(len(ns_day)), ns_day, ns_day):
        plt.text(y+0.25, x, '%.2f' % v, ha='center', va='center', fontsize=text_size)  # 保留两位小数

    # x label
    plt.text((get_max(ns_day) + margin_top) / 2,
             - 3.3 * margin_top,
             xlabel, ha='center', va='center', fontsize=text_size)

    plt.title(title)
    plt.tick_params(labelsize=text_size)

    plt.grid(axis='x', linestyle='--', linewidth=1, c=grid_color, alpha=0.6, zorder=-10)
    plt.legend(loc='upper right', fontsize=font_size,
               ncol=2, columnspacing=0.43, borderpad=0.4, borderaxespad=0.4,
               handletextpad=0.33, handlelength=2)
    plt.ylim(0 - margin_top, len(version) - 1 + margin_top)
    plt.yticks(np.arange(len(version)), version)
    plt.xlim(0, get_max(ns_day) + margin_right)
    # 3072k
    # plt.xticks([0, 1, 2, 3, 4, 5, 6 , 7,])
    # 1536k
    # plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    plt.savefig(save_path)
    plt.show()


if __name__ == '__main__':
    file = 'knl_gpu.pdf'
    draw(file)
