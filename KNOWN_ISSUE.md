# Known Issues and Possible Resolution

## 1. Proposed API Error

- **Status**: Identified - This is a feature restriction, not a bug

### Symptom

In the OUTPUT panel (or bottom-right notification message), you may see error messages like:

``` log
[error] [Window] Extension 'wubzbz.debugpy' CANNOT USE these API proposals 'portsAttributes, debugVisualization, contribViewsWelcome'. You MUST start in extension development mode or use the --enable-proposed-api command line flag
```

Or more specifically:
``` log
[error] sendDebugpySuccessActivationTelemetry() failed. [Error: Extension 'wubzbz.debugpy' CANNOT use API proposal: portsAttributes.
Its package.json#enabledApiProposals-property declares:  but NOT portsAttributes.
The missing proposal MUST be added and you must start in extension development mode or use the following command line switch: --enable-proposed-api wubzbz.debugpy
```

### Resolution Methods

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

#### 1. Temporary Workaround

Launch VSCodium with the following command:
```bash
codium --enable-proposed-api wubzbz.debugpy
```

If this error disappears, then this solution is proved to match with the problem you encountered. Next, you can try steps shown below.

#### 2. Permanent Solution 1: Edit product.json

> [!IMPORTANT] 
> Before making any changes, create a backup of your `product.json` file.

1. Locate the [`product.json`](https://github.com/VSCodium/vscodium/blob/master/product.json) file in your VSCodium installation directory (typically in `resources/app/product.json`). You probably need a root authentication to edit and save this file.
2. Find (or add) the `extensionEnabledApiProposals` section, which should contains these items and something else(proposed APIs used by other extensions are defined here, too). Or just use `Ctrl`+`F` to search `debugpy`, in most cases you can navigate to here directly. However, if there's no search result, you may consider adding this entry by yourself.

```json
// product.json
{
    ...(other sections)
    "extensionEnabledApiProposals": [
        ...(other extensions)
        "ms-python.vscode-pylance": [
        "terminalShellEnv",
        "portsAttributes"
        ],
        "ms-python.debugpy": [
        "contribViewsWelcome",
        "debugVisualization",
        "portsAttributes"
        ],
        // we need to add an entry here
        ...(other extensions)
    ],
    ...(other sections)
}
```

3. Add proposed APIs entry for `wubzbz.debugpy`. You can place it below `ms-python.debugpy`'s entry, or somewhere else in the `extensionEnabledApiProposals` section. But directly modify `ms-python.debugpy` to 
`wubzbz.debugpy` is not recommended.

```json
        "wubzbz.debugpy": [
        "contribViewsWelcome",
        "debugVisualization",
        "portsAttributes"
        ],
```

4. Restart VSCodium.

#### 3. Permanent Solution 2: Edit argv.json

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

In official distribution builds, these APIs are typically **disabled** by default for stability reasons. However, as you have seen in the `extensionEnabledApiProposals` section of `product.json` file, the official VS Code and VS Codium product include pre-approved exceptions in [`product.json`](https://github.com/VSCodium/vscodium/blob/master/product.json) configuration for certain Microsoft and GitHub extensions (like `ms-python.debugpy`), allowing them to use specific Proposed APIs even in release builds.

Since this project is a port to loongarch64 architecture with a different extension identifier (`wubzbz.debugpy` instead of the official `ms-python.debugpy`), it doesn't benefit from these pre-approved exceptions in VSCodium. Users need to manually enable the Proposed APIs for this extension using one of the methods above.

This is a security and stability feature of VSCodium/VS Code, ensuring that experimental APIs are only used when explicitly permitted by the user.

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

### Resolution Methods

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

#### Complete Uninstallation and Clean Installation

1. **Uninstall conflicting extensions**:
   - Open VSCodium
   - Go to Extensions view (`Ctrl+Shift+X`)
   - Search for and uninstall any of the following extensions if present:
     - `ms-python.debugpy` (official Microsoft version)
     - Any other extension with "debugpy" in its name

2. **Clear extension cache** (**only if** issues persist):
   - Close VSCodium completely
   - Navigate to VSCodium's extension directory:
     - **Linux**: `~/.vscodium/extensions`
   - Delete any remaining debugpy-related folders

3. **Install wubzbz.debugpy**:
   - Install the loongarch64-compatible debugpy extension
   - Restart VSCodium

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

This is a fundamental limitation of the VSCode extension system - only one extension can own a particular command or setting identifier at a time.


<!-- Template
## 1. 

- **Status**: 

### Symptom

### Resolution Methods

> [!NOTE] 
> Seek for [support](./SUPPORT.md) if you encountered difficulties during the following operation.

### Root Cause
-->