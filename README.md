## QuickRun
C C++ Python 等语言快速编译运行的小工具，使用 Python Tkinter，代码很少也很简单，短短几十行。作者 Copcin，初一在读，本软件长期维护。

### 使用

如果没有 Python 3 运行环境的朋友可以直接下载我打包过的版本 QuickRun.exe。文件比较大，因为包含了 Python 3 解释器和依赖项。运行它，把文件拖入文件框，再点击运行即可快速编译运行程序。

有 Python 3 运行环境的朋友先安装依赖 windnd：

```bash
pip install windnd
```

然后下载源码，解压缩后运行 QuickRun.py 即可。把文件拖入文件框，再点击运行即可快速编译运行程序。

如果是 C / C++ 程序，编译后的 exe 文件会生成在 Results 目录下。

### 须知

目前 QuickRun 仅支持 Windows 平台，macOS 平台和 Linux 平台的支持后续会加入。

快速运行 Python 3 文件需要先安装 Python 3 解释器并将其添加至 Path；

快速运行 C / C++ 文件需要先安装 GCC / G++，这里推荐使用 TDM-GCC，MinGW-32 或 MinGW-W64 也是可以的。

本软件遵循 GNU GPLv3 协议，详情见 LICENSE。

（不要问我为什么代码这么少还加一个比代码多十几倍的 LICENSE，生活总是要来点仪式感）
