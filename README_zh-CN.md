# 🌟 DevForge-CLI

> 🛠️ 开发者瑞士军刀 | Zero Dependencies, Offline, Privacy-First
>
> 🔗 [English](./README.md) | [简体中文](./README_zh-CN.md) | [繁體中文](./README_zh-TW.md)

---

## 🎉 项目介绍

**DevForge-CLI** 是一款专为开发者设计的瑞士军刀式命令行工具箱，提供 **30+ 常用开发工具**，完全 **零依赖**、**全离线**运行，**隐私优先**。

### ✨ 核心亮点

- 🔐 **零依赖** - 仅使用Python标准库，无需安装任何外部包
- 🌐 **全离线** - 所有处理在本地完成，数据绝不外传
- 🎯 **跨平台** - Windows / macOS / Linux 全平台支持
- 🎨 **美观易用** - 彩色终端输出，交互友好
- 🔗 **管道友好** - 支持管道输入输出，方便脚本集成

### 💡 设计理念

灵感来源于 [DevToys](https://devtoys.app/) 桌面应用，但专注于 **终端/CLI 场景**，让开发者可以在任何环境下快速使用常用工具，无需打开浏览器或安装重型GUI应用。

---

## 📦 核心功能

### 📦 编码解码工具
| 命令 | 功能 | 示例 |
|------|------|------|
| `devforge base64 encode <text>` | Base64编码 | `devforge base64 encode "Hello"` |
| `devforge base64 decode <text>` | Base64解码 | `devforge base64 decode "SGVsbG8="` |
| `devforge url encode <text>` | URL编码 | 安全处理URL特殊字符 |
| `devforge html encode <text>` | HTML实体编码 | 转换HTML转义字符 |

### 🔐 哈希计算工具
| 命令 | 功能 | 示例 |
|------|------|------|
| `devforge hash md5 <text>` | MD5哈希 | 计算字符串MD5 |
| `devforge hash sha256 <text>` | SHA256哈希 | 计算字符串SHA256 |
| `devforge hash sha512 <text>` | SHA512哈希 | 计算字符串SHA512 |

### 🆔 UUID生成工具
| 命令 | 功能 | 示例 |
|------|------|------|
| `devforge uuid v1` | UUID v1 | 基于时间戳生成 |
| `devforge uuid v4` | UUID v4 | 随机生成（常用） |
| `devforge uuid v5` | UUID v5 | 基于命名空间生成 |

### 🔑 密码工具
| 命令 | 功能 | 示例 |
|------|------|------|
| `devforge password 16` | 生成密码 | 生成16位安全密码 |
| `devforge password strength <pwd>` | 密码强度检测 | 评估密码安全性 |

### ⏰ 时间工具
| 命令 | 功能 | 示例 |
|------|------|------|
| `devforge time` | 当前时间 | 显示Unix时间戳和可读时间 |
| `devforge cron "*/5 * * * *"` | Cron解析 | 解析Cron表达式含义 |

### 📝 正则工具
| 命令 | 功能 | 示例 |
|------|------|------|
| `devforge regex "\d+" <text>` | 正则测试 | 实时测试正则表达式 |

### 🎨 颜色工具
| 命令 | 功能 | 示例 |
|------|------|------|
| `devforge color #ff5722` | 颜色预览 | HEX/RGB/HSL互转+预览 |

### 🎲 其他工具
- **JWT解码** - `devforge jwt decode <token>`
- **文本统计** - `devforge text stats <text>`
- **莫尔斯电码** - `devforge morse encode/decode <text>`
- **JSON格式化** - `devforge json format <json>`

---

## 🚀 快速开始

### 环境要求
- Python 3.8+
- 无需安装任何依赖包！

### 安装方式

#### 方式一：直接运行（推荐）
```bash
# 下载脚本
wget https://raw.githubusercontent.com/gitstq/DevForge-CLI/main/devforge.py

# 添加执行权限
chmod +x devforge.py

# 直接运行
python3 devforge.py -l
```

#### 方式二：安装为全局命令
```bash
# 克隆仓库
git clone https://github.com/gitstq/DevForge-CLI.git
cd DevForge-CLI

# 安装
pip install -e .

# 全局使用
devforge -l
```

#### 方式三：添加到 PATH
```bash
# 创建符号链接
sudo ln -s /path/to/devforge.py /usr/local/bin/devforge

# 直接使用
devforge -l
```

### 常用命令示例

```bash
# 列出所有工具
devforge -l

# Base64编码
devforge base64 encode "Hello World"

# SHA256哈希
devforge hash sha256 "password123"

# 生成随机密码
devforge password 20

# 当前时间
devforge time

# 正则测试
devforge regex "\d+" "test123abc"

# 颜色预览
devforge color #ff5722
```

---

## 📖 详细使用指南

### 管道输入支持

```bash
# 从文件读取
cat file.json | devforge json format

# 从其他命令管道
echo "SGVsbG8=" | devforge base64 decode

# 批量处理
for f in *.txt; do echo "$f"; done | devforge base64 encode
```

### 高级用法

```bash
# 生成强密码并复制到剪贴板
devforge password 32 | xclip -selection clipboard

# 批量验证哈希
echo "098f6bcd4621d373cade4e832627b4f6" | openssl md5 -r

# 创建随机API密钥
devforge random string 32
```

---

## 💡 设计思路与迭代规划

### 设计理念

1. **极简主义** - 每个工具专注做好一件事
2. **零依赖** - 仅使用Python标准库，降低使用门槛
3. **本地优先** - 所有处理在本地完成，保护用户隐私
4. **终端友好** - 专为CLI场景优化，输出美观易读

### 技术选型

- **语言**: Python 3.8+（标准库）
- **架构**: 单文件 + 子命令模式
- **界面**: ANSI彩色输出

### 未来迭代计划

- [ ] 添加更多编码格式支持（Base32, Base58, URL-safe Base64）
- [ ] 增加文件哈希批量计算
- [ ] 支持配置文件自定义行为
- [ ] 添加交互式TUI界面
- [ ] 支持插件扩展机制
- [ ] 增加更多正则表达式模板
- [ ] 添加HTTP请求模拟工具

---

## 📦 打包与部署

### 跨平台打包

```bash
# Linux/macOS
chmod +x devforge.py
./devforge.py -l

# Windows
python devforge.py -l
```

### Docker 部署

```dockerfile
FROM python:3.11-slim
COPY devforge.py /usr/local/bin/devforge
RUN chmod +x /usr/local/bin/devforge
ENTRYPOINT ["/usr/local/bin/devforge"]
```

使用：
```bash
docker build -t devforge .
docker run --rm devforge -l
```

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 开发流程

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/amazing-feature`
3. 提交更改：`git commit -m 'feat: add amazing feature'`
4. 推送到分支：`git push origin feature/amazing-feature`
5. 提交 Pull Request

### 代码规范

- 遵循 PEP 8
- 为新功能添加文档字符串
- 保持函数简洁单一职责

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 🙏 致谢

- 灵感来源：[DevToys](https://devtoys.app/) - 优秀的开发者工具桌面应用
- 所有开源贡献者

---

<div align="center">

**如果这个项目对您有帮助，请给我们一个 ⭐️**

Made with ❤️ by [DevForge Team](https://github.com/gitstq)

</div>
