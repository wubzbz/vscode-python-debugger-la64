# Production Environment Test Checklist

## 🎯 Basic Tests

### **basic of basic**

- [x] run python without debug
- [x] package info
- [x] disable the extension
- [x] bundled libs installed

- [x] launch a debug
- [x] show output in terminal
- [ ] 调试器能正常断开连接


### **breakpoint related**

- [] triggered breakpoint
- [] value shown while debugging
- [] inline breakpoint
- [] function breakpoint
- [] data breakpoint
- [] logpoint
- [] breakpoint section in RUN AND DEBUG view
- [x] breakpoint in passed area


## 🔧 Advanced tests

### **UI**

#### debug toolbar

- [ ] Step Over (F10)
- [ ] Step Into (F11)
- [ ] Step Out (Shift+F11)
- [ ] Continue (F5)
- [] Restart(Ctrl+Shift+F5)
- [] Stop(Shift+F5)

#### launch from editor button

- [] debug python file
- [] debug python file using launch.json

#### launch from RUN AND DEBUG view

- [] play: python debugger
- [] play: custom debug
- [] add config


#### debug console

- [x] print log text
- [x] REPL

#### debug sidebar

- [x] turning orange(blue)
- [x] show info
- [] switch debug profile

### **variable and monitor**

- [ ] 局部变量正确显示
- [ ] 对象属性可展开查看
- [ ] 监视表达式工作正常
- [ ] 数组/列表内容正确显示

### **调用堆栈测试**

```python
# test_callstack.py
def function_a():
    function_b()  # 查看调用堆栈

def function_b():
    function_c()

def function_c():
    x = 1  # 在此设置断点

function_a()
```
- [ ] 调用堆栈正确显示函数调用关系
- [ ] 能在堆栈帧间切换

### **debug console**

- [] debug in terminal
- [] 
- []

### **commands**

- [] debugpy.command.clearCacheAndReload.title
- [] debugpy.command.debugInTerminal.title
- [] debugpy.command.debugUsingLaunchConfig.title
- [] debugpy.command.reportIssue.title
- [] debugpy.command.viewOutput.title

### **settings**

- [] debugpy.debugJustMyCode.description
- [] debugpy.showPythonInlineValues.description

### **OUTPUT**

- [] no error
- [x] DAP server path correct
- [] proposed api

```
[error] [窗口] Extension debugpy CANNOT USE these API proposals 'portsAttributes, debugVisualization, contribViewsWelcome'. You MUST start in extension development mode or use the --enable-proposed-api command line flag
```

- keypoint: `product.json`

- [VSCode Discussions #899](https://github.com/microsoft/vscode-discussions/discussions/899).
- [Issue 20247](https://github.com/microsoft/vscode-python/issues/20247) and [Issue 20498](https://github.com/microsoft/vscode-python/issues/20498)

### **configuration**

#### launch.json

```json
// .vscode/launch.json 的各种配置
{
    "name": "Python: Current File",
    "type": "python",
    "request": "launch",
    "program": "${file}",
    "args": ["--verbose"]
}
```

- [] generate from RUN AND DEBUG view

```
[error] [窗口] command 'command:workbench.action.debug.configure' not found: Error: command 'command:workbench.action.debug.configure' not found
    at gYe._tryExecuteCommand (vscode-file://vscode-app/usr/lib/vscodium/resources/app/out/vs/workbench/workbench.desktop.main.js:1337:5745)
    at gYe.executeCommand (vscode-file://vscode-app/usr/lib/vscodium/resources/app/out/vs/workbench/workbench.desktop.main.js:1337:5643)
    at async MXe.open (vscode-file://vscode-app/usr/lib/vscodium/resources/app/out/vs/workbench/workbench.desktop.main.js:1362:404)
    at async LXe.open (vscode-file://vscode-app/usr/lib/vscodium/resources/app/out/vs/workbench/workbench.desktop.main.js:1362:1969)
```

- [ ] 命令行参数传递正常
- [ ] 工作目录设置正确
- [ ] 环境变量设置生效
- [] comments in json?
- [] attach to process id


## 🐍 Python 特定功能

### **Python env test**

- [ ] 能正确识别系统 Python 解释器
- [ ] 支持虚拟环境 (venv, conda)
- [ ] 能切换不同 Python 版本

### **Exception handling**
```python
# test_exceptions.py
def risky_operation():
    return 1 / 0  # 除零异常

try:
    risky_operation()
except Exception as e:
    print(f"Caught exception: {e}")
```
- [ ] 未捕获异常时调试器暂停
- [ ] 异常信息正确显示
- [ ] 用户异常断点工作

### **test with debugpy**

- []
- [] --wait-for-client


## 📁 实际场景测试

### **多文件项目测试**

```bash
project/
├── main.py
├── utils/
│   └── helpers.py
└── tests/
    └── test_basic.py
```

- [ ] 跨文件断点工作正常
- [ ] 模块导入调试正常
- [ ] 相对路径导入正确解析

### **multi-threading**


### **Django, Flask, and FastAPI**


### **SSH Remote Debug**


## 🏗️ Platform-specific tests

### **LoongArch64 compatibility**

- [ ] 插件在 LoongArch64 上稳定运行
- [x] 无原生模块兼容性问题
    - [x] checked reliables in node_modules: only `keytar` with `.node` -- OK.
- [ ] normal performance
- [ ] normal ram usage
