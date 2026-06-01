# 🌟 DevForge-CLI

> 🛠️ 開發者瑞士刀 | 零依賴、離線運行、隱私優先
>
> 🔗 [English](./README.md) | [简体中文](./README_zh-CN.md) | [繁體中文](./README_zh-TW.md)

---

## 🎉 專案介紹

**DevForge-CLI** 是一款專為開發者設計的瑞士刀式命令列工具箱，提供 **30+ 常用開發工具**，完全 **零依賴**、**全離線** 運行，**隱私優先**。

### ✨ 核心亮點

- 🔐 **零依賴** - 僅使用Python標準庫，無需安裝任何外部套件
- 🌐 **全離線** - 所有處理在本地完成，資料絕不外傳
- 🎯 **跨平台** - Windows / macOS / Linux 全平台支援
- 🎨 **美觀易用** - 彩色終端輸出，互動友好
- 🔗 **管道友善** - 支援管道輸入輸出，方便腳本整合

### 💡 設計理念

靈感來源於 [DevToys](https://devtoys.app/) 桌面應用，但專注於 **終端/CLI 場景**，讓開發者可以在任何環境下快速使用常用工具，無需打開瀏覽器或安裝重型GUI應用。

---

## 📦 核心功能

### 📦 編碼解碼工具
| 命令 | 功能 | 範例 |
|------|------|------|
| `devforge base64 encode <text>` | Base64編碼 | `devforge base64 encode "Hello"` |
| `devforge base64 decode <text>` | Base64解碼 | `devforge base64 decode "SGVsbG8="` |
| `devforge url encode <text>` | URL編碼 | 安全處理URL特殊字符 |
| `devforge html encode <text>` | HTML實體編碼 | 轉換HTML跳脫字符 |

### 🔐 雜湊計算工具
| 命令 | 功能 | 範例 |
|------|------|------|
| `devforge hash md5 <text>` | MD5雜湊 | 計算字串MD5 |
| `devforge hash sha256 <text>` | SHA256雜湊 | 計算字串SHA256 |
| `devforge hash sha512 <text>` | SHA512雜湊 | 計算字串SHA512 |

### 🆔 UUID生成工具
| 命令 | 功能 | 範例 |
|------|------|------|
| `devforge uuid v1` | UUID v1 | 基於時間戳生成 |
| `devforge uuid v4` | UUID v4 | 隨機生成（常用） |
| `devforge uuid v5` | UUID v5 | 基於命名空間生成 |

### 🔑 密碼工具
| 命令 | 功能 | 範例 |
|------|------|------|
| `devforge password 16` | 生成密碼 | 生成16位安全密碼 |
| `devforge password strength <pwd>` | 密碼強度檢測 | 評估密碼安全性 |

### ⏰ 時間工具
| 命令 | 功能 | 範例 |
|------|------|------|
| `devforge time` | 當前時間 | 顯示Unix時間戳和可讀時間 |
| `devforge cron "*/5 * * * *"` | Cron解析 | 解析Cron表達式含義 |

### 📝 正規表達式工具
| 命令 | 功能 | 範例 |
|------|------|------|
| `devforge regex "\d+" <text>` | 正規表達式測試 | 即時測試正規表達式 |

### 🎨 顏色工具
| 命令 | 功能 | 範例 |
|------|------|------|
| `devforge color #ff5722` | 顏色預覽 | HEX/RGB/HSL互轉+預覽 |

### 🎲 其他工具
- **JWT解碼** - `devforge jwt decode <token>`
- **文字統計** - `devforge text stats <text>`
- **摩爾斯電碼** - `devforge morse encode/decode <text>`
- **JSON格式化** - `devforge json format <json>`

---

## 🚀 快速開始

### 環境要求
- Python 3.8+
- 無需安裝任何依賴套件！

### 安裝方式

#### 方式一：直接執行（推薦）
```bash
# 下載腳本
wget https://raw.githubusercontent.com/gitstq/DevForge-CLI/main/devforge.py

# 新增執行權限
chmod +x devforge.py

# 直接執行
python3 devforge.py -l
```

#### 方式二：安裝為全域命令
```bash
# 複製倉庫
git clone https://github.com/gitstq/DevForge-CLI.git
cd DevForge-CLI

# 安裝
pip install -e .

# 全域使用
devforge -l
```

#### 方式三：新增到 PATH
```bash
# 建立符號連結
sudo ln -s /path/to/devforge.py /usr/local/bin/devforge

# 直接使用
devforge -l
```

### 常用命令範例

```bash
# 列出所有工具
devforge -l

# Base64編碼
devforge base64 encode "Hello World"

# SHA256雜湊
devforge hash sha256 "password123"

# 生成隨機密碼
devforge password 20

# 當前時間
devforge time

# 正規表達式測試
devforge regex "\d+" "test123abc"

# 顏色預覽
devforge color #ff5722
```

---

## 📖 詳細使用指南

### 管道輸入支援

```bash
# 從檔案讀取
cat file.json | devforge json format

# 從其他命令管道
echo "SGVsbG8=" | devforge base64 decode

# 批次處理
for f in *.txt; do echo "$f"; done | devforge base64 encode
```

### 進階用法

```bash
# 生成強密碼並複製到剪貼簿
devforge password 32 | xclip -selection clipboard

# 批次驗證雜湊
echo "098f6bcd4621d373cade4e832627b4f6" | openssl md5 -r

# 建立隨機API密鑰
devforge random string 32
```

---

## 💡 設計思路與迭代規劃

### 設計理念

1. **極簡主義** - 每個工具專注做好一件事
2. **零依賴** - 僅使用Python標準庫，降低使用門檻
3. **本地優先** - 所有處理在本地完成，保護用戶隱私
4. **終端友善** - 專為CLI場景優化，輸出美觀易讀

### 技術選型

- **語言**: Python 3.8+（標準庫）
- **架構**: 單檔案 + 子命令模式
- **介面**: ANSI彩色輸出

### 未來迭代計劃

- [ ] 新增更多編碼格式支援（Base32, Base58, URL-safe Base64）
- [ ] 增加檔案雜湊批次計算
- [ ] 支援設定檔自訂行為
- [ ] 新增互動式TUI介面
- [ ] 支援外掛擴展機制
- [ ] 增加更多正規表達式範本
- [ ] 新增HTTP請求模擬工具

---

## 📦 打包與部署

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

## 🤝 貢獻指南

歡迎提交 Issue 和 Pull Request！

### 開發流程

1. Fork 本倉庫
2. 建立功能分支：`git checkout -b feature/amazing-feature`
3. 提交更改：`git commit -m 'feat: add amazing feature'`
4. 推送分支：`git push origin feature/amazing-feature`
5. 提交 Pull Request

### 程式碼規範

- 遵循 PEP 8
- 為新功能新增文檔字串
- 保持函數簡潔單一職責

---

## 📄 開源協議

本專案採用 [MIT License](LICENSE) 開源協議。

---

## 🙏 致謝

- 靈感來源：[DevToys](https://devtoys.app/) - 優秀的開發者工具桌面應用
- 所有開源貢獻者

---

<div align="center">

**如果這個專案對您有幫助，請給我們一個 ⭐️**

Made with ❤️ by [DevForge Team](https://github.com/gitstq)

</div>
