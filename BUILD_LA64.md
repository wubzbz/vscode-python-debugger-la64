# Building Python Debugger Extension on LoongArch64 Platform

## Overview

This document describes how to build the VSCode Python Debugger extension VSIX package on LoongArch64 architecture.

## Prerequisites

### System Requirements

- LoongArch64 architecture operating system
- VSCodium (LoongArch64 version)
- Python 3.9+ and pip
- [Node.js and npm](https://www.loongnix.cn/zh/api/nodejs/) (LoongArch64 version)
- Git

### Software Installation

#### 1. Install Node.js and npm

See [this page](https://docs.loongnix.cn/nodejs/Doc/list/02.Node.js%E5%AE%89%E8%A3%85%E8%AF%B4%E6%98%8E.html).

#### 2. Install Python 3.9+

```bash
# Ensure Python 3.9 or later is installed
python3 --version
```

#### 3. Install VSCodium

Download [here](https://vscodium.com/).

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
pipx run nox --session install_bundled_libs
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
pipx run nox --session lint
```

### 6. Compilation and Testing

#### Run Full Test Suite

```bash
npm run test
```

> [!NOTE]
> On LoongArch64 architecture, the test framework automatically uses the locally installed VSCodium instead of downloading the x86 version of VSCode, which is different from the official extension.

### 7. Update Build Number (Optional)

Update the build number if you like:

```bash
pipx run nox --session update_build_number -- <build_ID>
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
