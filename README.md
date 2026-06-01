# 🌟 DevForge-CLI

> 🛠️ Swiss Army Knife for Developers | Zero Dependencies, Offline, Privacy-First
>
> 🔗 [English](./README.md) | [简体中文](./README_zh-CN.md) | [繁體中文](./README_zh-TW.md)

---

## 🎉 Introduction

**DevForge-CLI** is a Swiss Army Knife-style command-line tool suite designed for developers, providing **30+ essential development tools**, completely **zero-dependency**, **fully offline**, and **privacy-first**.

### ✨ Key Features

- 🔐 **Zero Dependencies** - Uses only Python standard library, no external packages needed
- 🌐 **Fully Offline** - All processing happens locally, data never leaves your machine
- 🎯 **Cross-Platform** - Windows / macOS / Linux supported
- 🎨 **Beautiful UI** - Colorful terminal output, friendly interaction
- 🔗 **Pipeline Friendly** - Supports stdin/stdout for scripting integration

### 💡 Design Philosophy

Inspired by [DevToys](https://devtoys.app/) desktop application, but focused on **terminal/CLI scenarios**, allowing developers to quickly use common tools in any environment without opening a browser or installing heavy GUI applications.

---

## 📦 Core Features

### 📦 Encoding Tools
| Command | Function | Example |
|---------|----------|---------|
| `devforge base64 encode <text>` | Base64 encode | `devforge base64 encode "Hello"` |
| `devforge base64 decode <text>` | Base64 decode | `devforge base64 decode "SGVsbG8="` |
| `devforge url encode <text>` | URL encode | Safely encode URL special chars |
| `devforge html encode <text>` | HTML entity encode | Convert HTML escape chars |

### 🔐 Hash Tools
| Command | Function | Example |
|---------|----------|---------|
| `devforge hash md5 <text>` | MD5 hash | Calculate string MD5 |
| `devforge hash sha256 <text>` | SHA256 hash | Calculate string SHA256 |
| `devforge hash sha512 <text>` | SHA512 hash | Calculate string SHA512 |

### 🆔 UUID Tools
| Command | Function | Example |
|---------|----------|---------|
| `devforge uuid v1` | UUID v1 | Time-based generation |
| `devforge uuid v4` | UUID v4 | Random generation (common) |
| `devforge uuid v5` | UUID v5 | Namespace-based generation |

### 🔑 Password Tools
| Command | Function | Example |
|---------|----------|---------|
| `devforge password 16` | Generate password | Generate 16-char secure password |
| `devforge password strength <pwd>` | Password strength check | Evaluate password security |

### ⏰ Time Tools
| Command | Function | Example |
|---------|----------|---------|
| `devforge time` | Current time | Show Unix timestamp and readable time |
| `devforge cron "*/5 * * * *"` | Cron parse | Parse Cron expression meaning |

### 📝 Regex Tools
| Command | Function | Example |
|---------|----------|---------|
| `devforge regex "\d+" <text>` | Regex test | Test regex in real-time |

### 🎨 Color Tools
| Command | Function | Example |
|---------|----------|---------|
| `devforge color #ff5722` | Color preview | HEX/RGB/HSL conversion + preview |

### 🎲 Other Tools
- **JWT Decode** - `devforge jwt decode <token>`
- **Text Stats** - `devforge text stats <text>`
- **Morse Code** - `devforge morse encode/decode <text>`
- **JSON Format** - `devforge json format <json>`

---

## 🚀 Quick Start

### Requirements
- Python 3.8+
- No external dependencies required!

### Installation

#### Method 1: Direct Run (Recommended)
```bash
# Download script
wget https://raw.githubusercontent.com/gitstq/DevForge-CLI/main/devforge.py

# Add execute permission
chmod +x devforge.py

# Run directly
python3 devforge.py -l
```

#### Method 2: Install as Global Command
```bash
# Clone repository
git clone https://github.com/gitstq/DevForge-CLI.git
cd DevForge-CLI

# Install
pip install -e .

# Use globally
devforge -l
```

#### Method 3: Add to PATH
```bash
# Create symlink
sudo ln -s /path/to/devforge.py /usr/local/bin/devforge

# Use directly
devforge -l
```

### Common Command Examples

```bash
# List all tools
devforge -l

# Base64 encode
devforge base64 encode "Hello World"

# SHA256 hash
devforge hash sha256 "password123"

# Generate random password
devforge password 20

# Current time
devforge time

# Regex test
devforge regex "\d+" "test123abc"

# Color preview
devforge color #ff5722
```

---

## 📖 Detailed Usage Guide

### Pipeline Input Support

```bash
# Read from file
cat file.json | devforge json format

# Pipe from other command
echo "SGVsbG8=" | devforge base64 decode

# Batch processing
for f in *.txt; do echo "$f"; done | devforge base64 encode
```

### Advanced Usage

```bash
# Generate strong password and copy to clipboard
devforge password 32 | xclip -selection clipboard

# Batch verify hash
echo "098f6bcd4621d373cade4e832627b4f6" | openssl md5 -r

# Create random API key
devforge random string 32
```

---

## 💡 Design Philosophy & Roadmap

### Design Principles

1. **Minimalism** - Each tool does one thing well
2. **Zero Dependencies** - Only Python standard library, low barrier to use
3. **Local First** - All processing happens locally, protecting user privacy
4. **Terminal Friendly** - Optimized for CLI scenarios, beautiful and readable output

### Technology Stack

- **Language**: Python 3.8+ (Standard Library)
- **Architecture**: Single file + subcommand pattern
- **UI**: ANSI colored output

### Future Roadmap

- [ ] Add more encoding formats (Base32, Base58, URL-safe Base64)
- [ ] Batch file hash calculation
- [ ] Configuration file support
- [ ] Interactive TUI interface
- [ ] Plugin extension mechanism
- [ ] More regex expression templates
- [ ] HTTP request simulation tools

---

## 📦 Packaging & Deployment

### Cross-Platform Packaging

```bash
# Linux/macOS
chmod +x devforge.py
./devforge.py -l

# Windows
python devforge.py -l
```

### Docker Deployment

```dockerfile
FROM python:3.11-slim
COPY devforge.py /usr/local/bin/devforge
RUN chmod +x /usr/local/bin/devforge
ENTRYPOINT ["/usr/local/bin/devforge"]
```

Usage:
```bash
docker build -t devforge .
docker run --rm devforge -l
```

---

## 🤝 Contributing

Contributions are welcome! Please submit Issues and Pull Requests.

### Development Workflow

1. Fork this repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'feat: add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Submit Pull Request

### Code Standards

- Follow PEP 8
- Add docstrings for new functions
- Keep functions simple and single-purpose

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- Inspiration: [DevToys](https://devtoys.app/) - Excellent developer tools desktop app
- All open source contributors

---

<div align="center">

**If this project helps you, please give us a ⭐️**

Made with ❤️ by [DevForge Team](https://github.com/gitstq)

</div>
