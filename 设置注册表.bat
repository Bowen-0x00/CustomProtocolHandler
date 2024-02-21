@echo off

REM 获取当前路径
set "current_path=%~dp0"

REM 查找当前路径下的 .exe 文件
for %%i in ("%current_path%*.exe") do (
    set "exe_path=%%i"
    goto :found
)

REM 若没有找到 .exe 文件，则给出错误提示并退出
echo No .exe file found in the current directory.
exit /b

:found
REM 添加注册表项和值到HKEY_CURRENT_USER\Software\Classes
reg add HKEY_CLASSES_ROOT\ymjr /ve /t REG_SZ /d "URL:myapp Protocol Handler" /f
reg add HKEY_CLASSES_ROOT\ymjr /v "URL Protocol" /t REG_SZ /d "" /f
reg add HKEY_CLASSES_ROOT\ymjr\shell /f
reg add HKEY_CLASSES_ROOT\ymjr\shell\open /f
reg add HKEY_CLASSES_ROOT\ymjr\shell\open\command /ve /t REG_SZ /d "\"%exe_path%\" %%1" /f

REM 暂停命令行窗口
pause