# Production Environment Test Checklist for Python Debugger

## 🎯 Basic Functionality Tests

### **Core Debugger Operations**
- [x] Run Python script without debug mode
- [] Extension installation and updates work normally
- [] Display package information correctly
- [] Debugger extension can be properly disabled/enabled
- [] All bundled libraries are properly installed
- [] l10n texts display properly
- [] Launch debug session successfully
- [] Debug output displayed in terminal

### **Breakpoint Management**
- [] Breakpoints are triggered correctly
- [] Variable values displayed during debugging
- [] Logpoints output messages without stopping
- [] Conditional breakpoints function properly
- [] Inline breakpoints function properly(Shift+F9)
- [] Breakpoint section visible in RUN AND DEBUG view
- [] Exception breakpoints work as expected

### **Debug Toolbar UI**
- [] Step Over (F10) works correctly
- [] Step Into (F11) works correctly
- [] Step Out (Shift+F11) works correctly
- [] Continue (F5) resumes execution properly
- [] Restart (Ctrl+Shift+F5) reloads debug session
- [] Stop (Shift+F5) terminates debug session

## 🔧 Advanced Debugging Features

### **Debugging Controls**
#### Launch Methods
- [] Debug Python file from editor button
- [] Debug Python file using launch.json configuration
- [] Launch debugger from RUN AND DEBUG view - Python Debugger
- [] Launch debugger from RUN AND DEBUG view - Custom configuration
- [] Add new debug configuration
- [ ] ~~Generate launch.json from RUN AND DEBUG view~~ waiting for upstream...

#### Debug Interface Elements
- [] Debug sidebar changes color when active (orange/blue)
- [] Debug information displayed in sidebar
- [] Switch between different debug profiles
- [] REPL functionality works in debug console
- [] Debug console supports expression evaluation

### **Data Inspection**
- [] Local variables display correctly
- [] Object properties can be expanded and inspected
- [] Watch expressions update and display properly
- [] Array/list contents displayed correctly
- [] Global variables accessible during debugging
- [] Variable values update during stepping
- [] Inline Hex Decoder works

### **Call Stack Management**
- [] Call stack displays correct function hierarchy
- [] Can navigate between stack frames
- [] Stack frame variables update when switching frames
- [] Call stack preserved during step operations
    - bit of slow when switching

### **Command Palette Integration**
- [] `debugpy.command.clearCacheAndReload` works
- [] `debugpy.command.debugInTerminal` functions
- [] `debugpy.command.debugUsingLaunchConfig` works
- [] `debugpy.command.reportIssue` accessible
    - (linked to right repo but cannot navigate to issue report page in browser)
    - Cannot set properties of undefined (setting 'enabled')
- [] `debugpy.command.viewOutput` displays output

### **Configuration & Settings**
#### Settings Validation
- [] `debugpy.debugJustMyCode` setting functions correctly
- [] `debugpy.showPythonInlineValues` displays inline values
- [] Debugger settings persist between sessions

#### launch.json Configuration
```json
{
    "name": "Python: Current File",
    "type": "python", 
    "request": "launch",
    "program": "${file}",
    "args": ["--verbose"],
    "console": "integratedTerminal",
    "env": {"DEBUG": "true"},
    "cwd": "${workspaceFolder}/test_dir"
}
```
- [] Command line arguments passed correctly to program
- [] Working directory setting functions properly
- [] Environment variables set in launch.json take effect
- [] Attach to process by listening to port works correctly
- [] Multiple debug configurations can be created and used
- [] Three kinds of terminal display output

### **Output & Error Handling**
- [ ] No unexpected errors in OUTPUT panel
- [] DAP server path correctly configured
- [] Proposed API usage properly handled
- [] Warning messages appropriately displayed

## 🐍 Python-Specific Features

### **Python Environment Management**
- [] Correctly detects system Python interpreter
- [] Supports virtual environments (venv, conda, ...)
- [] Can switch between different Python versions
- [] Python path configuration works correctly
- [] Interpreter selection persists between sessions

### **Exception Handling**
- [] Debugger pauses on uncaught exceptions
- [] Exception information displayed correctly
- [] Exception details include stack trace
- [] Can continue execution after handling exception

### **Debugpy Integration**
- [] Debugpy module functions correctly
- [] `--wait-for-client` parameter works
- [] Remote debugging connections established properly
- [] Debugpy commands available and functional
- [] Debugger can properly disconnect

## 📁 Real-World Scenarios

### **Multi-file Project Debugging**
- [] Cross-file breakpoints work correctly
- [] Module imports debug properly
- [] Relative imports resolve correctly
- [] Breakpoints in imported modules function
- [] Step into functionality works across files

### **Concurrent Programming**
- [] Debugging multi-threaded applications works
- [] Thread switching in debugger functions
- [] Breakpoints in threads are hit correctly
- [] Thread information displayed in debug view

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
- [] No native module compatibility issues
    - [] Verified reliable node_modules: only `keytar` with `.node` files - Compatible
- [ ] Normal performance characteristics maintained
- [ ] Normal memory usage patterns observed
- [ ] All debugger features function identically to x86/ARM
- [ ] No architecture-specific crashes or errors


### **Cross-Platform Consistency**
- [ ] Platform-specific paths handled correctly
- [ ] File encoding and line endings handled properly

## 🔍 Additional Test Scenarios

### **Performance & Stability**
- [] Debugger startup time acceptable
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
*Checklist Version: 2.3  
Last Updated: 2025/11/19  
Test Environment: VSCodium with Python Extension on LoongArch64*