# Production Environment Test Checklist for Python Debugger

## 🎯 Basic Functionality Tests

### **Core Debugger Operations**
- [x] Run Python script without debug mode
- [x] Display package information correctly
- [x] Debugger extension can be properly disabled/enabled
- [x] All bundled libraries are properly installed
- [x] Launch debug session successfully
- [x] Debug output displayed in terminal
- [x] Debugger can properly disconnect

### **Breakpoint Management**
- [x] Breakpoints are triggered correctly
- [x] Variable values displayed during debugging
- [x] Inline breakpoints function properly(Shift+F9)
- [x] Function breakpoints work as expected
- [x] Logpoints output messages without stopping
- [x] Breakpoint section visible in RUN AND DEBUG view
- [x] Breakpoints in valid code areas work correctly
- [x] Conditional breakpoints function properly
- [x] Exception breakpoints work as expected

## 🔧 Advanced Debugging Features

### **Debugging Controls & UI**
#### Debug Toolbar
- [x] Step Over (F10) works correctly
- [x] Step Into (F11) works correctly
- [x] Step Out (Shift+F11) works correctly
- [x] Continue (F5) resumes execution properly
- [x] Restart (Ctrl+Shift+F5) reloads debug session
- [x] Stop (Shift+F5) terminates debug session

#### Launch Methods
- [x] Debug Python file from editor button
- [x] Debug Python file using launch.json configuration
- [x] Launch debugger from RUN AND DEBUG view - Python Debugger
- [x] Launch debugger from RUN AND DEBUG view - Custom configuration
- [ ] Add new debug configuration
- [ ] ~~Generate launch.json from RUN AND DEBUG view~~ waiting...

#### Debug Interface Elements
- [x] Debug sidebar changes color when active (orange/blue)
- [x] Debug information displayed in sidebar
- [ ] Switch between different debug profiles
- [x] Print log text in debug console
- [x] REPL functionality works in debug console
- [x] Debug console supports expression evaluation

### **Data Inspection**
- [x] Local variables display correctly
- [x] Object properties can be expanded and inspected
- [x] Watch expressions update and display properly
- [x] Array/list contents displayed correctly
- [x] Global variables accessible during debugging
- [x] Variable values update during stepping
- [x] Inline Hex Decoder works

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
- [x] Call stack displays correct function hierarchy
- [x] Can navigate between stack frames
- [x] Stack frame variables update when switching frames
- [x] Call stack preserved during step operations

### **Command Palette Integration**
- [x] `debugpy.command.clearCacheAndReload` works
- [ ] `debugpy.command.debugInTerminal` functions
- [ ] `debugpy.command.debugUsingLaunchConfig` works
- [ ] `debugpy.command.reportIssue` accessible
- [x] `debugpy.command.viewOutput` displays output

### **Configuration & Settings**
#### Settings Validation
- [x] `debugpy.debugJustMyCode` setting functions correctly
- [x] `debugpy.showPythonInlineValues` displays inline values
- [x] Debugger settings persist between sessions

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
- [x] JSON comments supported in launch.json
- [ ] Attach to process by PID works correctly
- [ ] Multiple debug configurations can be created and used

### **Output & Error Handling**
- [x] No unexpected errors in OUTPUT panel
- [x] DAP server path correctly configured
- [x] Proposed API usage properly handled
- [x] Warning messages appropriately displayed
- [x] l10n bundle displayed translation

## 🐍 Python-Specific Features

### **Python Environment Management**
- [ ] Correctly detects system Python interpreter
- [x] Supports virtual environments (venv, conda, pipenv)
- [x] Can switch between different Python versions
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
- [x] Debugger pauses on uncaught exceptions
- [x] Exception information displayed correctly
- [x] Exception details include stack trace
- [x] Can continue execution after handling exception

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
- [ ] Platform-specific paths handled correctly
- [ ] File encoding and line endings handled properly

## 🔍 Additional Test Scenarios

### **Performance & Stability**
- [x] Debugger startup time acceptable
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
*Checklist Version: 2.2  
Last Updated: 2025/11/5  
Test Environment: VSCodium with Python Extension on LoongArch64*