# Known Issues and Possible Solution

## 1. Proposed API Error

- **Status**: Identified - This is a feature restriction, not a bug

### Symptom

In the OUTPUT panel (or bottom-right notification message), you may see error messages like:

``` log
[error] [Window] Extension 'wubzbz.debugpy' CANNOT USE these API proposals 
'portsAttributes, debugVisualization, contribViewsWelcome'. You MUST start in 
extension development mode or use the --enable-proposed-api command line flag
```

Or more specifically:

``` log
[error] sendDebugpySuccessActivationTelemetry() failed. [Error: Extension 
'wubzbz.debugpy' CANNOT use API proposal: portsAttributes.
Its package.json#enabledApiProposals-property declares:  but NOT portsAttributes.
The missing proposal MUST be added and you must start in extension development
mode or use the following command line switch: --enable-proposed-api wubzbz.debugpy
```

### Solution

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

#### 1. Temporary Workaround

Launch VSCodium with the following command:
```bash
codium --enable-proposed-api wubzbz.debugpy
```

If this error disappears, then this solution is proved to match with the problem you encountered. Next, you can try steps shown below.

#### 2. Permanent Solution: Edit argv.json

> [!IMPORTANT] 
> Before making any changes, create a backup of your `argv.json` file.

1. In VSCodium, open the Command Palette (`Ctrl+Shift+P`)
2. Run "Preferences: Configure Runtime Arguments"
3. Add the following to the `argv.json` file:

```json
{
    "enable-proposed-api": ["wubzbz.debugpy"]
}
```

4. Save and restart VSCodium

### Root Cause

[**Proposed APIs**](https://code.visualstudio.com/api/advanced-topics/using-proposed-api) are experimental features in VS Code/VSCodium that are still under development and not yet stable for general use. They allow extension developers to test new functionality before official release.

In official distribution builds, these APIs are typically **disabled** by default for stability reasons. However, the official VS Code and VS Codium product include pre-approved exceptions in [`product.json`](https://github.com/VSCodium/vscodium/blob/master/product.json) configuration for certain Microsoft and GitHub extensions (like `ms-python.debugpy`), allowing them to use specific Proposed APIs even in release builds.

Since this project is a port to loongarch64 architecture with a different extension identifier (`wubzbz.debugpy` instead of the official `ms-python.debugpy`), it doesn't benefit from these pre-approved exceptions in VSCodium. Users need to manually enable the Proposed APIs for this extension using one of the methods above.

#### Related links

- [`product.json`](https://github.com/microsoft/vscode/blob/main/product.json) of VS Code and [`product.json`](https://github.com/VSCodium/vscodium/blob/master/product.json) of VS Codium.
    - `extensionEnabledApiProposals` is not defined in [VS Code repository](https://github.com/microsoft/vscode/tree/main)'s `product.json` file, but it actually exists in the official distributions you downloaded. Check `resources/app/product.json` in where you installed a Microsoft VSCode to verify it.
- [VSCode Discussions #899](https://github.com/microsoft/vscode-discussions/discussions/899).
- VSCode python extension [Issue #20247](https://github.com/microsoft/vscode-python/issues/20247) and [Issue #20498](https://github.com/microsoft/vscode-python/issues/20498).


## 2. Activating extension 'wubzbz.debugpy' failed

- **Status**: Identified - Extension conflict issue

### Symptom

When installing `wubzbz.debugpy` without first uninstalling other debugpy extensions, you may see error messages in the bottom-right notification area:

``` log
Activating extension 'wubzbz.debugpy' failed: command 'debugpy.viewOutput' already exists.
[wubzbz.debugpy]: Cannot register "debugpy.showPythonInlineValues". This property has been registered. 
[wubzbz.debugpy]: Cannot register "debugpy.debugJustMyCode". This property has been registered. 
```

### Solution

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

#### Complete Uninstallation and Clean Installation

1. **Uninstall conflicting extensions**:
   - Open VSCodium
   - Go to Extensions view (`Ctrl+Shift+X`)
   - Search for and uninstall any of the following extensions if present:
     - `ms-python.debugpy` (official Microsoft version)
     - Any other extension with "debugpy" in its name

2. **Install Python Debugger for LoongArch (wubzbz.debugpy)**:
   - Install the loongarch64-compatible debugpy extension
   - Restart VSCodium

3. **Clear extension cache** (**only if** issues persist):
   - Close VSCodium completely
   - Navigate to VSCodium's extension directory:
     - **Linux**: `~/.vscodium/extensions`
   - Delete any remaining debugpy-related folders
   - Repeat Step 2

#### Alternative: Disable Conflicting Extensions

If you need to keep other Python extensions for compatibility reasons:

1. Go to Extensions view (`Ctrl+Shift+X`)
2. Find conflicting extensions (like `ms-python.python`)
3. Click the "Disable" button instead of uninstalling
4. Restart VSCodium, install and enable `wubzbz.debugpy`

### Root Cause

This issue occurs because multiple extensions are trying to register the same commands, settings, and contributions with identical identifiers. VSCodium/VSCode doesn't allow duplicate registrations for:

- **Commands** (like `debugpy.viewOutput`)
- **Settings** (like `debugpy.debugJustMyCode`)

The official Microsoft debugpy extension (`ms-python.debugpy`) and our loongarch64 port (`wubzbz.debugpy`) both attempt to register identical functionality, causing conflicts during activation.


## 3. 'npm: command not found' During Debugging Extension

- **Status**: Resolved in [Pull Request #4](https://github.com/wubzbz/vscode-python-debugger-la64/pull/4).

### Symptom

When attempting to debug this extension using the original [`launch.json`](https://github.com/microsoft/vscode-python-debugger/blob/main/.vscode/launch.json) and [`tasks.json`](https://github.com/microsoft/vscode-python-debugger/blob/main/.vscode/tasks.json) configurations, the debugging process fails with the error:

```
*  Executing task: npm run watch 

/usr/bin/bash: line 1: npm: command not found

*  The terminal process "/usr/bin/bash '-c', 'npm run watch'" failed to start (exit code: 127).
```

Or something like this

```
*  Executing task: npm run watch 

npm: command not found

*  Terminal process terminated with exit code: 127.
```

This occurs even though npm commands work correctly in the terminal. The preLaunchTask fails to execute because the npm command cannot be found in the task execution environment.

### Solution

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

The solution involved modifying both `tasks.json` and `launch.json` to ensure proper environment loading:

**In [`tasks.json`](./.vscode/tasks.json):**
- Add `shell` type tasks instead of direct `npm` type tasks
- Use `bash -l -c` command structure to run npm scripts
- Create new task labels: `bash-npm-watch` and `bash-npm-watch-tests`
- Update dependency chains to use the new bash-wrapped tasks

**In [`launch.json`](./.vscode/launch.json):**
- Add new debug configurations: "Bash Run Extension" and "Bash Unit Tests"  
- Update `preLaunchTask` references to point to the new bash-wrapped tasks
- Keep original configurations for reference, but use the new bash-based ones for actual debugging

**Usage:**
- Use "Bash Run Extension" configuration instead of "Run Extension" for debugging the main extension
- Use "Bash Unit Tests" configuration instead of "Unit Tests" for running tests
- The new configurations ensure proper environment setup before executing npm commands

### Root Cause

The issue stems from how nvm manages Node.js environments and how VS Code executes tasks:

**nvm Installation Method:**

nvm is typically installed by adding initialization scripts to `~/.bashrc`. These scripts set up environment variables (PATH, NVM_DIR) and shell functions. And nvm operates as a shell function rather than a standalone binary.

**Original Configuration Failure:**

VS Code tasks execute in a non-login shell by default, but non-login shells do not automatically source `~/.bashrc`. Thus, without `.bashrc` being sourced, nvm initialization doesn't occur, which explains why the npm command remains unavailable in the task execution context.

The solution used `bash -l` (login shell) that forces the loading of user profile scripts including `~/.bashrc`. This ensures the task execution environment matches the interactive terminal environment. The `-c` parameter allows passing the npm command to the login shell.

This approach maintains nvm's environment setup while working within VS Code's task execution model.


## 4. "Create a launch.json" Button Failure in Non-English Environments

- **Status**: Fixed upstream (refer to VSCode Pull Request [#271707](https://github.com/microsoft/vscode/pull/271707)).

<img width="284" height="187" alt="图片" src="https://github.com/user-attachments/assets/650f4745-396f-4bf8-93fe-8203c0fc7784" />

### Symptom

When the display language is set to a non-English language in VSCode/VSCodium:

1.  Navigate to the **Run and Debug** view.
2.  If no `launch.json` file exists in the current workspace, a welcome page with a "Create a launch.json" button is displayed.
3.  Clicking this button fails with an error in the OUTPUT panel:
    ``` log
    [error] [窗口] command 'command:workbench.action.debug.configure' not found:
    Error: command 'command:workbench.action.debug.configure' not found
    ```
    This prevents the creation of the essential `launch.json` file, which is crucial for configuring the debug environment, thus blocking debugging functionality.

### Solution

This issue is resolved in VSCode updates. Regularly update your VSCodium.

### Root Cause

The core issue was a mislocalized string, which has been addressed in the upstream fix.

#### Related links

- [VSCode Issue #271691](https://github.com/microsoft/vscode/issues/271691).
- [VSCode Pull Request #271707](https://github.com/microsoft/vscode/pull/271707).


## 5. "'inlineHexDecoder' is already registered" During Unit Tests

- **Status**: Observing

### Symptom

With Jupyter extensions installed, error log presents during running unit tests:
```
Debugging - pythonInlineProvider
    ✔ ProvideInlineValues function should return all the vars in the python file (56ms)
    rejected promise not handled within 1 second: TypeError: Cannot read properties of undefined (reading 'get')
    rejected promise not handled within 1 second: Error: A debug visualization provider with id 'inlineHexDecoder' is already registered
    ✔ ProvideInlineValues function should return all the vars in the python file with self in class (1052ms)
    ✔ ProvideInlineValues function should return the vars in the python file with readable class variables
    ✔ ProvideInlineValues function should return all the vars in the python file using Assignment Expressions
```

### Solution

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

Disable or uninstall Jupyter serial extensions(Jupyter, Jupyter Cell Tags, Jupyter Keymap, Jupyter Notebook Renderers, and Jupyter Slide Show).

### Root Cause

There may be some conflicts between Python Debugger extension and Jupyter extensions on registration of a debug visualization provider with id 'inlineHexDecoder'. 
We are still observing its influence on Python Debugger extension's function `showPythonInlineValues`.


## 6. "property 'serverReadyAction' AssertionError" During Unit Tests

- **Status**: Fixed in [Pull Request #5](https://github.com/wubzbz/vscode-python-debugger-la64/pull/5).

### Symptom

Error log presents during running unit tests:
```
Debugging - pythonInlineProvider
    ✔ ProvideInlineValues function should return all the vars in the python file (56ms)
    rejected promise not handled within 1 second: AssertionError: expected { name: 'Python launch', …(19) } to have property 'serverReadyAction' of { …(3) }, but got { …(3) }
    ✔ ProvideInlineValues function should return all the vars in the python file with self in class (1052ms)
    ✔ ProvideInlineValues function should return the vars in the python file with readable class variables
    ✔ ProvideInlineValues function should return all the vars in the python file using Assignment Expressions
```

### Solution

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

**For end users**: No action required. Just keep your extensions updated.

**For developers**: Fetch the latest changes from this repository to get the fix.

### Root Cause

The issue was caused by **improper object comparison**: The 'Add serverReadyAction for Django and Flask' [test](./src/test/unittest/configuration/resolvers/launch.unit.test.ts) used shallow property comparison (`expect().to.have.property(property, value)`) which only checks reference equality for objects, not their actual content. This caused false negatives when comparing the `serverReadyAction` configuration objects.

The following changes were implemented to resolve the issue:

1. **Use deep equality comparison for objects**:
   ```javascript
   // Before (problematic):
   expect(debugConfig).to.have.property('serverReadyAction', expectedServerReadyAction);
   
   // After (fixed):
   expect(debugConfig).to.have.property('serverReadyAction');
   expect(debugConfig.serverReadyAction).to.deep.equal(expectedServerReadyAction);
   ```

2. **Add null checks** to prevent undefined property access errors.


## 7. "Unable to find thread to evaluate variable reference"

- **Status**: Unknown

### Symptom

```
[Error] CodeExceptionError: Unable to find thread to evaluate variable reference.
```

### Solution

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

### Root Cause


## 8. Cannot read undefined property 'extensionId'

- **Status**: Unknown

### Symptom

```
[info] [Window] Started local extension host with pid 19729.
[error] [Window] Cannot read properties of undefined (reading 'extensionId'): TypeError: Cannot read properties of undefined (reading 'extensionId')
    at t (vscode-file://vscode-app/usr/lib/vscodium/resources/app/out/vs/workbench/workbench.desktop.main.js:4070:2745)
    at tIt.recommendRemoteExtensionIfNeeded (vscode-file://vscode-app/usr/lib/vscodium/resources/app/out/vs/workbench/workbench.desktop.main.js:4070:3495)
[info] [Window] [perf] Render performance baseline is 51ms
```

### Solution

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

### Root Cause


## 9. Module `punycode` is deprecated

- **Status**: Observing

### Symptom

```
[error] [Window] [Extension Host] (node:23102) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
(Use `exe --trace-deprecation ...` to show where the warning was created)
```

### Solution

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

Just waiting for upstream update.

### Root Cause

`punycode` is one of the dependencies of this extension.

<!-- Template
## 1. 

- **Status**: 

### Symptom

### Solution

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

### Root Cause
-->
