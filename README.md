# Custom Protocol Handler
[English](./README.md) | [简体中文](docs/README_ZH.md)

CustomProtocolHandler" is a tool used to handle custom protocols, aiming to implement the processing of custom protocol links. It allows for the execution of specific programs when a link is clicked, enabling the opening of applications and performing other operations.

For example, it can be used to handle backlinks in note-taking software（such as obsidian, onenote）, allowing for navigation back to the original context, such as videos, PowerPoint presentations, and PDF files.

Of course, there can be other uses as well. Feedback is welcome.

Note:

- The automatic generation of links can be done using Quicker or other methods.
- The existing tools in this repository are suitable for the Windows platform. For Linux and macOS platforms, the .py files may not need to be modified, but the registry part should be replaced with other methods.

## Usage

### Direct Usage

1. Download and extract the compressed package from the "Release" section.
2. Right-click and run the `设置注册表.bat` file as an administrator. (This batch file is used to modify the registry and contains the content of [自定义协议.reg](./自定义协议.reg)).
3. Configure the `config.conf` file by setting the paths of your respective software to your own software paths.

### Customization

#### Packaging as an Executable File

If you want to package the Python file as an executable file, you can use a tool like PyInstaller, for example:

`pyinstaller "customProtocolHandler.py" -w`

#### Without Packaging

Modify the execution command in the registry to [python path] [custom protocol handler.py path] %1.

自定义协议.reg
If you want to register the registry using the "自定义协议.reg" file, please note:

- Escape the strings properly.
- The file encoding should be UTF16-LE."

## Feedback, questions, ideas, problems

Feel free to contact me if:

- You have any issues or questions regarding usage.
- You have suggestions or feedback.
- You want to discuss interesting ideas or new features.

Communication channels can be:

- GitHub issues.
- Email.
- Bilibili comments or private messages.
- My personal contact information (WeChat, QQ).

## Say Thank You

If you find the modifications I made helpful to you, feel free to leave comments and messages.

You can also sponsor me a cup of coffee:

- WeChat sponsorship code.
<img src="images/赞助码.jpg" width="200px">
- ko-fi
  <a href='https://ko-fi.com/G2G3SY16R' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
