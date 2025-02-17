# 排序可视化工具

这是一个使用Python和Tkinter库开发的排序算法可视化工具。它可以帮助用户通过图形界面直观地看到不同排序算法（如冒泡排序、快速排序、归并排序、选择排序、插入排序和希尔排序）的工作过程。

## 认为项目不错就给一个start吧

## 功能

- **冒泡排序**：通过重复遍历待排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
- **快速排序**：通过一个基准值将数列分为两部分，其中一部分的所有数据都比另一部分的所有数据要小，然后再递归地排序这两部分。
- **归并排序**：将两个或两个以上的有序数列合并成一个有序数列。
- **选择排序**：从未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
- **插入排序**：构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
- **希尔排序**：也称为缩小增量排序，是插入排序的一种更高效的改进版本。

## 使用方法

1. 运行`main.py`文件启动应用。
2. 点击界面中的按钮选择排序算法。
3. 观察排序过程的可视化展示。
4. 使用滑动条调整排序速度。

## 技术栈

- **Python**：编程语言。
- **Tkinter**：Python的标准GUI库。
- **Random**：生成随机数。
- **Time**：控制排序动画的速度。

## 依赖

确保你的Python环境中安装了Tkinter库。大多数Python安装都会自带Tkinter，如果没有，可以通过以下命令安装：

```bash
pip install tk
