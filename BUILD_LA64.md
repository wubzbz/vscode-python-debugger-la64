# Building Python Debugger Extension on LoongArch64 Platform

## Overview

This document describes how to build the VSCode Python Debugger extension VSIX package on LoongArch64 architecture.

## Prerequisites

### System Requirements

- LoongArch64 architecture operating system
- **VSCodium 1.92.0+** (LoongArch64 version)
- **Python 3.9+** and **pip**
- [**Node.js 22 LTS** and **npm 10**](https://www.loongnix.cn/zh/api/nodejs/) (LoongArch64 version)
- Git

### Software Installation

#### 1. Install Node.js 22 and npm 10

See loongnix's [instruction](https://docs.loongnix.cn/nodejs/Doc/list/02.Node.js%E5%AE%89%E8%A3%85%E8%AF%B4%E6%98%8E.html) on Node.js installation.

```bash
node --version
v22.21.1

npm --version
10.x.x
```

Starting with v2025.18.0, this fork has upgraded to **npm 10** (bundled with Node.js 22 LTS) as the package manager. An important related change is: 

- The [`package-lock.json`](https://github.com/wubzbz/vscode-python-debugger-la64/blob/main/package-lock.json) file in this project is now generated in **Lockfile v3** format, 
- while the upstream source may still be using the older Lockfile v2 format.

Our Strategy: To ensure optimal compatibility and performance, this fork will maintain an independent dependency lockfile based on Lockfile v3. After merging upstream code changes, we typically **regenerate this file** based on the updated `package.json` and loongnix npm registry.

**What This Means for You:**

- Cloning/Installation: Use the `package-lock.json` from this repository directly; running `npm ci` will give you a consistent environment.

- Merging Upstream Changes: If dependencies in `package.json` are updated, you may need to run `npm install` on this branch to regenerate a new lockfile.

- Dependency Differences: Due to architectural or toolchain differences, some dependency versions may slightly differ from upstream. Such variations are controlled and validated:

| Package name | Upstream version | Current version |
| --- | --- | --- |
| fsevents | 2.3.2 | N/A[^1] |

[^1]: Optional module for Darwin.

This change is made to adapt to modern toolchains and improve the development experience. If you have any questions, please discuss them in the relevant Issues.


#### 2. Install Python 3.9+

Ensure Python 3.9 or later is installed on your machine.

```bash
python3 --version
```

#### 3. Install VSCodium and Recommended Extensions

Download [the latest version](https://vscodium.com/) of VS Codium.

Install and enable [`dbaeumer.vscode-eslint`](https://open-vsx.org/extension/dbaeumer/vscode-eslint), [`amodio.tsl-problem-matcher`](https://open-vsx.org/extension/amodio/tsl-problem-matcher), and [`loong-vsx.ruff`](https://open-vsx.org/extension/loong-vsx/ruff) before starting your development.

> `loong-vsx.ruff` is ruff extension's loong64 port. This extension, instead of the original `charliermarsh.ruff`, is adopted based on the same reason why this fork exists.

## Build Steps

### 1. Get Source Code

```bash
git clone https://github.com/wubzbz/vscode-python-debugger-la64.git
cd vscode-python-debugger
```

### 2. Set Up Python Environment

```bash
# Update pip and install necessary tools
python3 -m pip install -U pip pipx wheel

# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install nox
pip install nox
```

### 3. Install Node.js Dependencies

```bash
npm ci --prefer-offline
```

### 4. Install Bundled Python Libraries

```bash
nox --session install_bundled_libs
```

### 5. Code Quality Checks

#### TypeScript Code Linting

```bash
# Lint TypeScript code
npm run lint

# Check TypeScript code formatting
npm run format-check
```

#### Python Code Linting

```bash
# Check Python code linting and formatting
nox --session lint
```

### 6. Compilation and Testing

#### Run Full Test Suite

```bash
npm run test
```

> [!NOTE]
> On LoongArch64 architecture, the test framework automatically uses the locally installed VSCodium instead of downloading the x86 version of VSCode, which is different from the official extension.

Open VS Codium RUN AND DEBUG panel, choose `Bash Unit Tests`, a tuned test configuration for loong64, to run unit tests. 

Similarly, choose `Base Run Extension` if you want to check if the extension works well in test environment. `Unit Tests` and `Run Extension` is the upstream version which may not work on LoongArch.

### 7. Update Build Number (Optional)

Update the build number if you like:

```bash
nox --session update_build_number -- <build_ID>
```

### 8. Build VSIX Package

```bash
npm run vsce-package
```

After completion, the VSIX file will be generated in the project root directory.

## Testing and Verification

After building, manual testing is recommended:

1. Install the generated VSIX file to VSCodium:

```bash
codium --install-extension <generated-vsix-file>
```

2. Test core debugging functionality on your machine:

   - Breakpoint setting and hitting
   - Variable inspection
   - Step-by-step debugging
   - Console output

## How to contribute to this project?

See [this page](./contributing.md).
