import tkinter as tk
import random
from tkinter import messagebox


class RandomNumberGenerator:
    def __init__(self, master, min_value, max_value):
        self.master = master
        self.min_value = min_value
        self.max_value = max_value
        self.random_numbers = []
        master.minsize(600,400)
        master.title("随机选取一名同学")
        master.attributes("-fullscreen", True)

        self.label = tk.Label(master, text="",font=("黑体",100))
        self.label.pack()
        self.generate_button = tk.Button(master, text="随机选取一名同学", command=self.generate_random_number)
        self.display_button = tk.Button(master, text="显示所有已选同学", command=self.display_random_numbers)
        self.close = tk.Button(master, text=' x ', command=quit, background="#aa2200", foreground="#ffffff",anchor=tk.NW)
        self.close.place(relx=0,rely=0.95)
        self.display_button.pack(side=tk.BOTTOM)
        self.generate_button.pack(side=tk.BOTTOM)


    def generate_random_number(self):
        if len(self.random_numbers)==self.max_value-self.min_value+1:
            messagebox.showinfo("无法随机挑选","选完每一个同学了，请重新启动软件刷新（左下角关闭应用)")
            return
        random_number = -1
        while((random_number in self.random_numbers) or random_number==-1):
            random_number = random.randint(self.min_value, self.max_value)
        self.random_numbers.append(random_number)  # 将新随机数添加到列表中
        self.label.config(text=(str(random_number)+"号"))

    def display_random_numbers(self):
        self.random_numbers.sort()
        if self.random_numbers:
            messagebox.showinfo("已选同学学号", "\n".join(map(str, self.random_numbers)))
        else:
            messagebox.showinfo("无", "还没有生成随机学号。")


if __name__ == "__main__":
    root = tk.Tk()
    RandomNumberGenerator(root, 1, 48)
    root.mainloop()