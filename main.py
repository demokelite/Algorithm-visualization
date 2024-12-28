import tkinter as tk
import random
import time


class SortVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("排序可视化")
        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack()

        self.array = []
        self.generate_array()
        self.draw_array()

        self.sort_bubble_button = tk.Button(master, text="冒泡排序", command=self.bubble_sort)
        self.sort_bubble_button.pack()

        self.sort_quick_button = tk.Button(master, text="快速排序", command=self.quick_sort)
        self.sort_quick_button.pack()

        self.sort_merge_button = tk.Button(master, text="归并排序", command=self.merge_sort)
        self.sort_merge_button.pack()

        self.sort_selection_button = tk.Button(master, text="选择排序", command=self.selection_sort)
        self.sort_selection_button.pack()

        self.sort_insertion_button = tk.Button(master, text="插入排序", command=self.insertion_sort)
        self.sort_insertion_button.pack()

        self.sort_shell_button = tk.Button(master, text="希尔排序", command=self.shell_sort)
        self.sort_shell_button.pack()

        self.reset_button = tk.Button(master, text="重新排序", command=self.generate_array)
        self.reset_button.pack()

        # 添加滑动条来调整速度
        self.speed_label = tk.Label(master, text="排序速度:")
        self.speed_label.pack()
        self.speed_scale = tk.Scale(master, from_=1, to=100, orient=tk.HORIZONTAL, label="速度",
                                    command=self.update_speed)
        self.speed_scale.set(10)  # 默认速度
        self.speed_scale.pack()

        self.delay = 10  # 默认延迟

    def generate_array(self):
        """生成一个新的随机数组"""
        self.array = [random.randint(10, 300) for _ in range(30)]
        self.draw_array()

    def draw_array(self):
        """绘制当前数组的条形图"""
        self.canvas.delete("all")
        bar_width = 600 / len(self.array)
        for i, height in enumerate(self.array):
            self.canvas.create_rectangle(i * bar_width, 400 - height, (i + 1) * bar_width, 400, fill="blue")

    def bubble_sort(self):
        """冒泡排序算法"""
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.draw_array()
                    self.master.update()
                    time.sleep(self.delay / 1000.0)  # 控制排序速度

    def quick_sort(self):
        """快速排序算法"""
        self._quick_sort(0, len(self.array) - 1)

    def _quick_sort(self, low, high):
        """快速排序的递归实现"""
        if low < high:
            pi = self.partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

    def partition(self, low, high):
        """快速排序的分区操作"""
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.draw_array()
                self.master.update()
                time.sleep(self.delay / 1000.0)  # 控制排序速度
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        self.draw_array()
        self.master.update()
        time.sleep(self.delay / 1000.0)  # 控制排序速度
        return i + 1

    def merge_sort(self):
        """归并排序算法"""
        self._merge_sort(0, len(self.array) - 1)

    def _merge_sort(self, left, right):
        """归并排序的递归实现"""
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(left, mid)
            self._merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        """归并操作"""
        left_array = self.array[left:mid + 1]
        right_array = self.array[mid + 1:right + 1]

        i = j = 0
        k = left

        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                self.array[k] = left_array[i]
                i += 1
            else:
                self.array[k] = right_array[j]
                j += 1
            self.draw_array()
            self.master.update()
            time.sleep(self.delay / 1000.0)  # 控制排序速度
            k += 1

        while i < len(left_array):
            self.array[k] = left_array[i]
            i += 1
            k += 1
            self.draw_array()
            self.master.update()
            time.sleep(self.delay / 1000.0)  # 控制排序速度

        while j < len(right_array):
            self.array[k] = right_array[j]
            j += 1
            k += 1
            self.draw_array()
            self.master.update()
            time.sleep(self.delay / 1000.0)  # 控制排序速度

    def selection_sort(self):
        """选择排序算法"""
        n = len(self.array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.draw_array()
            self.master.update()
            time.sleep(self.delay / 1000.0)  # 控制排序速度

    def insertion_sort(self):
        """插入排序算法"""
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.draw_array()
            self.master.update()
            time.sleep(self.delay / 1000.0)  # 控制排序速度

    def shell_sort(self):
        """希尔排序算法"""
        n = len(self.array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j - gap] > temp:
                    self.array[j] = self.array[j - gap]
                    j -= gap
                self.array[j] = temp
                self.draw_array()
                self.master.update()
                time.sleep(self.delay / 1000.0)  # 控制排序速度
            gap //= 2

    def update_speed(self, value):
        """更新排序速度"""
        self.delay = int(value)


if __name__ == "__main__":
    root = tk.Tk()
    app = SortVisualizer(root)
    root.mainloop()