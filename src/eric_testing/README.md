# Multi-tool Package

A simplified package that provides JSON-RPC tools for inspect_ai.

## Installation

The package can be installed with pip:

```bash
# Install the package directly from the source directory
pip install .

# Or from the project root directory
pip install -e src/multi_tool/
```

### Playwright Setup

Playwright browsers and system dependencies are automatically installed during package installation.

The installation process runs the following commands:
- `playwright install` - installs required browsers
- `playwright install-deps` - installs system dependencies

No manual setup is required.

## Usage

Once installed, you can use the command-line tool to invoke JSON-RPC methods:

```bash
# Use the command-line tool
multi-tool '{"jsonrpc": "2.0", "method": "editor", "id": 1, "params": {"command": "view", "path": "/tmp"}}'

# Or using Python module syntax
python -m multi_tool '{"jsonrpc": "2.0", "method": "editor", "id": 1, "params": {"command": "view", "path": "/tmp"}}'
```

## Features

1. Simple CLI tool (`multi-tool`) for executing specified tools with given parameters
2. Support for in-process JSON-RPC tools
3. Validation of parameters using Pydantic models

## Package Structure

The package has a minimal structure:

- `multi_tool/`: Main package
  - `_in_process_tools/`: Directory containing tool implementations
    - `_editor/`: Editor tool implementation
  - `_util/`: Utility functions for the tools
  - `__main__.py`: Entry point for module execution
  - `multi_tool.py`: Main CLI implementation

## Adding New Tools

To add a new tool:

1. Create a new directory under `_in_process_tools/` with an underscore prefix (e.g., `_new_tool/`)
2. Create files in the tool directory:
   - `__init__.py`: Empty file for the package
   - `tool_types.py`: Pydantic models for the tool parameters
   - `<tool>.py`: Implementation of the tool functionality
   - `json_rpc_methods.py`: JSON-RPC method definitions

The tool will be automatically detected and loaded when the package is installed.