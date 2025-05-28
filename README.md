# Devcontainers-Based Project Template

This `README.md` was created using my package [README_genie](https://github.com/browshanravan/README_genie).

A generic, Docker-based development container template that bootstraps a Python workspace—either as a standard package or a Streamlit app—ready to be used in GitHub Codespaces or any local environment supporting Dev Containers.

## About This Project

This repository provides a reusable template for:

- Defining a development container (`.devcontainer/`) with Python 3.10 support.
- Quickly scaffolding a Python package (with `src/` layout).
- Quickly scaffolding a Streamlit application (with configuration and helper scripts).

By leveraging GitHub Codespaces or the VS Code Dev Containers extension, you get a consistent, isolated environment with all necessary tools installed.

## Project Structure

```
.
├── LICENSE
├── README.md                       ← This file
├── create_package_framework.sh     ← Scaffold a Python package
├── create_streamlit_framework.sh   ← Scaffold a Streamlit app
└── .devcontainer/
    ├── Dockerfile                  ← Base image & setup
    └── devcontainer.json           ← Dev Container configuration
```

- **LICENSE**: MIT-licensed, granting full permission to use and modify.
- **create_package_framework.sh**: Generates a standard Python package structure:
  - `main.py`, `requirements.txt`
  - `<project_name>/__init__.py`, `src/utils.py`, and corresponding `__init__.py` files.
- **create_streamlit_framework.sh**: Sets up a basic Streamlit app:
  - Creates `.streamlit/config.toml` with theme and server settings.
  - Generates `app.sh` to install dependencies and launch the app.
  - Appends `streamlit` to `requirements.txt`.
- **.devcontainer/**: Contains container build instructions and feature settings for Python 3.10.

## Features

- **Isolated Dev Environment**  
  Docker-based container with Python 3.10, install tools, and easy extension via Dev Containers features.
- **Package Scaffolding**  
  Quickly generate a `src/`-style Python package with minimal boilerplate.
- **Streamlit Scaffolding**  
  Instantly create a Streamlit app skeleton with sensible defaults: theme, server auto-reload, upload limits.
- **GitHub Codespaces Ready**  
  Open this repo in Codespaces for a one-click development experience.

## Getting Started

### Prerequisites

- Docker (for local Dev Container builds)
- Visual Studio Code with [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)  
  _or_ GitHub Codespaces enabled on your account  
- Bash shell (to run the scaffold scripts)

### Launching the Dev Container

1. Clone this repository:  
   ```bash
   git clone https://github.com/browshanravan/devcontainers_template.git
   cd devcontainers_template
   ```
2. Open in VS Code:  
   - Command Palette → **Remote-Containers: Open Folder in Container**  
   - Or click **Open in Codespace** on GitHub

The container builds automatically using `.devcontainer/Dockerfile` and `devcontainer.json`, installing Python 3.10 and tools.

## Usage

### 1. Scaffold a Python Package

Run the package framework script:

```bash
sh create_package_framework.sh
```

This will create:

- `main.py`
- `requirements.txt`
- A directory named after your project (`<project_name>/`) with:
  - `__init__.py`
  - `src/utils.py`
  - `src/__init__.py` importing `utils`

Start implementing your package by editing `src/utils.py` and adding dependencies to `requirements.txt`.

### 2. Scaffold a Streamlit App

Run the Streamlit framework script:

```bash
sh create_streamlit_framework.sh
```

This will:

- Create `.streamlit/config.toml` with custom theme and server settings.
- Generate `app.sh` to install dependencies and launch your app.
- Append `streamlit` to `requirements.txt`.

To run your new Streamlit app:

```bash
bash app.sh
```

By default it runs on port `8501` with hot-reload enabled.

## Customizing the Dev Container

- **Python Version**: Modify 
  ```json
  "features": {
    "ghcr.io/devcontainers/features/python:1": { "version": "3.10" }
  }
  ```
  in `.devcontainer/devcontainer.json`.
- **Additional Tools**: Add entries under `"features"` or extend the `Dockerfile` with custom `RUN` commands.
- **Port Forwarding**: Use `"forwardPorts": [ ]` in `devcontainer.json` to expose extra ports.

## License

This project is licensed under the [MIT License](LICENSE).  
© 2025 Behzad Rowshanravan.