project:
  name: "Password Cracker"
  short_name: "password-cracker"
  emoji: "🔐"
  repo_url: "https://github.com/ZeefaShaikh/Password-Cracker"
  description: >
    Password Cracker is an educational Python tool to demonstrate password
    security and generation. It can generate strong random passwords and
    includes simple cracking examples (brute-force / dictionary) for learning
    how weak passwords are vulnerable. Intended for learning and testing only.

badges:
  license: "https://img.shields.io/badge/license-MIT-blue.svg"

metadata:
  authors:
    - name: "Zeefa Shaikh"
      github: "ZeefaShaikh"
  license:
    spdx: "MIT"
    url: "https://opensource.org/licenses/MIT"
  last_updated: "2025-09-24"

prerequisites:
  - "Python 3.8+ installed"
  - "Optional: virtualenv for isolated environment"

installation:
  recommended_workflow:
    - step: "Clone repository"
      command: "git clone https://github.com/ZeefaShaikh/Password-Cracker.git"
    - step: "Change to project directory"
      command: "cd Password-Cracker"
    - step: "Create virtual environment (recommended)"
      command: "python -m venv .venv && source .venv/bin/activate  # mac/linux\npython -m venv .venv && .\\.venv\\Scripts\\activate  # windows"
    - step: "Install optional dependencies (if any)"
      command: "pip install -r requirements.txt  # create requirements.txt only if needed"

usage:
  basic:
    description: "Run the main script to generate passwords or try demo cracking routines."
    commands:
      - "python password_cracker.py            # interactive mode / generate password"
  options_and_examples:
    - name: "Generate password with length 16"
      command: "python password_cracker.py --generate --length 16"
    - name: "Run demo brute-force (educational, small scope)"
      command: "python password_cracker.py --demo brute-force --target weakpass"
  notes: >
    Always use this tool ethically for learning and testing on your own accounts/data.
    Brute-force examples are limited for demonstration and are not optimized for real attacks.

features:
  - "Strong password generation: letters, digits, symbols, configurable length"
  - "Simple demonstrations of cracking approaches (dictionary & brute-force) for education"
  - "Lightweight, single-file script for easy reading and modification"

files:
  important:
    - "password_cracker.py       # main script"
    - "README.md                 # human-readable project documentation"
    - "LICENSE                   # MIT license"
  optional:
    - "wordlists/                # optional dictionary files (not included by default)"
    - "examples/                 # sample inputs or demonstration runs"

screenshots:
  - path: "Screenshots/home.png"
    caption: "Password generator output example"
  - path: "Screenshots/demo_crack.png"
    caption: "Demo brute-force progress (educational)"

contributing:
  summary: >
    Contributions welcome. Fork the repo, create a feature branch, and open a PR.
    Keep changes small and documented. Add tests/examples where appropriate.
  steps:
    - "Fork the repository"
    - "git checkout -b feature/your-feature"
    - "Make changes and commit with clear message"
    - "git push origin feature/your-feature"
    - "Open a Pull Request describing your change"

security_and_responsibility:
  - "This repository is for educational use only."
  - "Do not use cracking tools on systems you do not own or have explicit permission to test."
  - "Report any security issues to the repo owner via GitHub issues."

future_plan:
  - "Add CLI flags and argument parsing for all demo modes"
  - "Add unit tests for core functions (generation & helpers)"
  - "Add optional GUI (Tkinter or simple web UI) for easier use"
  - "Provide example wordlists in a separate release if desired"

license:
  type: "MIT"
  text_short: "Permissive open-source license allowing reuse with attribution."
  url: "https://opensource.org/licenses/MIT"

contact:
  - type: "github"
    handle: "ZeefaShaikh"
    url: "https://github.com/ZeefaShaikh"
