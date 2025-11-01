# Production Environment Test Checklist for Python Debugger

## 🎯 Basic Functionality Tests

### **Core Debugger Operations**
- [x] Run Python script without debug mode
- [x] Display package information correctly
- [x] Debugger extension can be properly disabled/enabled
- [x] All bundled libraries are properly installed
- [x] Launch debug session successfully
- [x] Debug output displayed in terminal
- [ ] Debugger can properly disconnect
- [ ] Debug session can be terminated cleanly

### **Breakpoint Management**
- [ ] Breakpoints are triggered correctly
- [ ] Variable values displayed during debugging
- [ ] Inline breakpoints function properly
- [ ] Function breakpoints work as expected
- [ ] Data breakpoints function correctly
- [ ] Logpoints output messages without stopping
- [ ] Breakpoint section visible in RUN AND DEBUG view
- [x] Breakpoints in valid code areas work correctly
- [ ] Conditional breakpoints function properly
- [ ] Exception breakpoints work as expected

## 🔧 Advanced Debugging Features

### **Debugging Controls & UI**
#### Debug Toolbar
- [ ] Step Over (F10) works correctly
- [ ] Step Into (F11) works correctly
- [ ] Step Out (Shift+F11) works correctly
- [ ] Continue (F5) resumes execution properly
- [ ] Restart (Ctrl+Shift+F5) reloads debug session
- [ ] Stop (Shift+F5) terminates debug session

#### Launch Methods
- [ ] Debug Python file from editor button
- [ ] Debug Python file using launch.json configuration
- [ ] Launch debugger from RUN AND DEBUG view - Python Debugger
- [ ] Launch debugger from RUN AND DEBUG view - Custom configuration
- [ ] Add new debug configuration
- [ ] Generate launch.json from RUN AND DEBUG view

#### Debug Interface Elements
- [x] Debug sidebar changes color when active (orange/blue)
- [x] Debug information displayed in sidebar
- [ ] Switch between different debug profiles
- [x] Print log text in debug console
- [x] REPL functionality works in debug console
- [ ] Debug console supports expression evaluation

### **Data Inspection**
- [ ] Local variables displayed correctly
- [ ] Object properties can be expanded and inspected
- [ ] Watch expressions update and display properly
- [ ] Array/list contents displayed correctly
- [ ] Global variables accessible during debugging
- [ ] Variable values update during stepping

### **Call Stack Management**
```python
# test_callstack.py
def function_a():
    function_b()  # Check call stack here

def function_b():
    function_c()

def function_c():
    x = 1  # Set breakpoint here

function_a()
```
- [ ] Call stack displays correct function hierarchy
- [ ] Can navigate between stack frames
- [ ] Stack frame variables update when switching frames
- [ ] Call stack preserved during step operations

### **Command Palette Integration**
- [ ] `debugpy.command.clearCacheAndReload.title` works
- [ ] `debugpy.command.debugInTerminal.title` functions
- [ ] `debugpy.command.debugUsingLaunchConfig.title` works
- [ ] `debugpy.command.reportIssue.title` accessible
- [ ] `debugpy.command.viewOutput.title` displays output

### **Configuration & Settings**
#### Settings Validation
- [ ] `debugpy.debugJustMyCode` setting functions correctly
- [ ] `debugpy.showPythonInlineValues` displays inline values
- [ ] Debugger settings persist between sessions

#### launch.json Configuration
```json
{
    "name": "Python: Current File",
    "type": "python", 
    "request": "launch",
    "program": "${file}",
    "args": ["--verbose"],
    "console": "integratedTerminal",
    "env": {"DEBUG": "true"}
}
```
- [ ] Command line arguments passed correctly to program
- [ ] Working directory setting functions properly
- [ ] Environment variables set in launch.json take effect
- [ ] JSON comments supported in launch.json
- [ ] Attach to process by PID works correctly
- [ ] Multiple debug configurations can be created and used

### **Output & Error Handling**
- [ ] No unexpected errors in OUTPUT panel
- [x] DAP server path correctly configured
- [x] Proposed API usage properly handled
- [ ] Error messages are clear and actionable
- [ ] Warning messages appropriately displayed

## 🐍 Python-Specific Features

### **Python Environment Management**
- [ ] Correctly detects system Python interpreter
- [ ] Supports virtual environments (venv, conda, pipenv)
- [ ] Can switch between different Python versions
- [ ] Python path configuration works correctly
- [ ] Interpreter selection persists between sessions

### **Exception Handling**
```python
# test_exceptions.py
def risky_operation():
    return 1 / 0  # Zero division error

try:
    risky_operation()
except Exception as e:
    print(f"Caught exception: {e}")
```
- [ ] Debugger pauses on uncaught exceptions
- [ ] Exception information displayed correctly
- [ ] User-defined exception breakpoints work
- [ ] Exception details include stack trace
- [ ] Can continue execution after handling exception

### **Debugpy Integration**
- [ ] Debugpy module functions correctly
- [ ] `--wait-for-client` parameter works
- [ ] Remote debugging connections established properly
- [ ] Debugpy commands available and functional

## 📁 Real-World Scenarios

### **Multi-file Project Debugging**
```
project/
├── main.py
├── utils/
│   └── helpers.py
└── tests/
    └── test_basic.py
```
- [ ] Cross-file breakpoints work correctly
- [ ] Module imports debug properly
- [ ] Relative imports resolve correctly
- [ ] Breakpoints in imported modules function
- [ ] Step into functionality works across files

### **Concurrent Programming**
```python
# test_threading.py
import threading
import time

def worker_function(thread_id):
    print(f"Thread {thread_id} starting")
    time.sleep(1)
    print(f"Thread {thread_id} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker_function, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```
- [ ] Debugging multi-threaded applications works
- [ ] Thread switching in debugger functions
- [ ] Breakpoints in threads are hit correctly
- [ ] Thread information displayed in debug view

### **Web Framework Support**
- [ ] Django application debugging
- [ ] Flask application debugging  
- [ ] FastAPI application debugging
- [ ] Web framework hot reload works with debugger
- [ ] Request breakpoints function in web apps

### **Remote Debugging**
- [ ] SSH remote debugging setup works
- [ ] Remote interpreter detection functions
- [ ] File synchronization during remote debug
- [ ] Remote breakpoints work correctly

## 🏗️ Platform-Specific Tests

### **LoongArch64 Compatibility**
- [ ] Extension runs stably on LoongArch64 architecture
- [x] No native module compatibility issues
    - [x] Verified reliable node_modules: only `keytar` with `.node` files - Compatible
- [ ] Normal performance characteristics maintained
- [ ] Normal memory usage patterns observed
- [ ] All debugger features function identically to x86/ARM
- [ ] No architecture-specific crashes or errors
- [ ] Extension installation and updates work normally

### **Cross-Platform Consistency**
- [ ] All functionality consistent with x86 platforms
- [ ] All functionality consistent with ARM platforms
- [ ] Platform-specific paths handled correctly
- [ ] File encoding and line endings handled properly

## 🔍 Additional Test Scenarios

### **Performance & Stability**
- [ ] Debugger startup time acceptable
- [ ] No memory leaks during extended debug sessions
- [ ] Large project debugging performs adequately
- [ ] Breakpoint management responsive with many breakpoints

### **Edge Cases**
- [ ] Debugging scripts with syntax errors
- [ ] Handling of infinite loops during debugging
- [ ] Debugger recovery after target process crashes
- [ ] Large data structure inspection performance
- [ ] Unicode and special character handling in variables

---
*Checklist Version: 2.0  
Last Updated: 2025/10/31  
Test Environment: VSCodium with Python Extension on LoongArch64*