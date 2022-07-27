# 作者：Copcin
# 具体使用方法见 README.md

from tkinter import *
import windnd
import os

def dragged_files(files):
    fileEntry.insert(END, ('\n'.join((item.decode('gbk') for item in files))))
    fileEntry.insert(END, "\n")

def run_files():
    # 获取文件绝对路径列表
    files = fileEntry.get("1.0", END).split("\n")
    # 去掉多余的空格
    while True:
        if files.count("") != 0:
            files.remove("")
        else:
            break

    # 将文件快速运行代码写入 entrance.bat
    entrance = open("entrance.bat","w")
    entrance.write("@echo off"+"\n")
    for file in files:
        if file.endswith("py"):
            entrance.write("python \""+file+"\"\n")
        elif file.endswith("c"):
            entrance.write("gcc \""+file+"\" -o \"Results\\"+get_file_name(file)+".exe\"\n")
            entrance.write("Results\\"+get_file_name(file)+".exe\n")
        elif file.endswith("cpp") or file.endswith("cplusplus"):
            entrance.write("g++ \""+file+"\" -o \"Results\\"+get_file_name(file)+".exe\"\n")
            entrance.write("\"Results\\"+get_file_name(file)+".exe\"\n")
    entrance.write("PAUSE")
    entrance.close()

    # 运行文件
    os.system("entrance.bat")

def get_file_name(file):
    f = file
    # 反转字符串
    f = f[::-1]
    f = f[:f.index("\\")]
    f = f[::-1]
    f = f[:f.index(".")]
    return f

if not os.path.isdir("Results"):
    os.mkdir("Results")

tk = Tk()
tk.geometry("300x170")
tk.title("QuickRun")
tk.resizable(0,0)

fileEntry = Text(tk, width=40, height=10)
fileEntry.pack()

commit = Button(tk, text="运行", command=run_files)
commit.pack()
 
if __name__ == '__main__':
    windnd.hook_dropfiles(fileEntry, func=dragged_files)
    tk.mainloop()
