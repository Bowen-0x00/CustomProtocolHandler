# Custom Protocol Handler

[English](../README.md) | [简体中文](./README_ZH.md)

CustomProtocolHandler是一个用于处理自定义协议的工具，旨在实现处理自定义协议链接。
可以做到点击链接时执行特定的程序，可以打开应用以及执行其他操作。

比如可以用于处理笔记软件（如obsidian、onenote）中的回链，以跳转回原上下文。如视频、PPT和PDF。

当然还可以有其他用途，欢迎反馈。

注意：

- 链接自动生成部分可以使用quicker或其他方式。
- 这个仓库中的现成工具适用于windows平台。对于linux和mac平台，py文件可以不用改，而注册表部分需要换成其他方式。
  
## 使用

### 直接使用

1. 下载并解压Release中的压缩包
2. 右键管理员运行其中的`设置注册表.bat`。（这个批处理是用来设置注册表，内容是[自定义协议.reg](../自定义协议.reg)）
3. 配置解压后的`config.conf`，设置其中各自软件的路径为你自己的软件路径

### 自己折腾

#### 自己打包可执行文件

如果你想要用可执行文件的方式可以自己打包python文件为可执行文件，如：

`pyinstaller "customProtocolHandler.py" -w`

#### 不打包

注册表中的执行命令改为`[python 路径] [custom protocol handler.py路径] %1`

#### 自定义协议.reg

如果你想要通过这个文件来注册注册表，注意

- 转义字符
- 文件编码应该为 UTF16-LE
  
## 问题、反馈、创意

欢迎联系我，如果：

- 遇到使用问题
- 建议与反馈
- 交流沟通有趣的想法、新的feature

沟通渠道可以是：

- github issue
- 邮件
- B站留言或私信
- 我的个人联系方式 (微信、qq)

## 赞助

如果你觉得我做的这些修改对你有所帮助，欢迎评论、留言。

你也可以赞助我一杯咖啡：

- 微信赞助码 
  <img src="../images/赞助码.jpg" width="200px">
- ko-fi
  <a href='https://ko-fi.com/G2G3SY16R' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
