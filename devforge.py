#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevForge-CLI - 开发者瑞士军刀 CLI工具箱
A Swiss Army Knife for Developers - Zero Dependencies, Offline, Privacy-First
"""

import sys
import argparse
import json
import base64
import hashlib
import uuid
import re
import time
import random
import string
import html
import urllib.parse
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any, List, Tuple

# ANSI颜色码
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorize(text: str, color: str) -> str:
    """为文本添加颜色"""
    colors = {
        'header': Colors.HEADER,
        'blue': Colors.BLUE,
        'cyan': Colors.CYAN,
        'green': Colors.GREEN,
        'yellow': Colors.YELLOW,
        'red': Colors.RED,
        'bold': Colors.BOLD,
        'underline': Colors.UNDERLINE,
    }
    return f"{colors.get(color, '')}{text}{Colors.ENDC}"

def print_header(text: str):
    """打印标题"""
    print(colorize(f"\n{'='*60}", 'cyan'))
    print(colorize(f"  {text}", 'bold'))
    print(colorize(f"{'='*60}\n", 'cyan'))

def print_success(text: str):
    """打印成功信息"""
    print(colorize(f"✓ {text}", 'green'))

def print_error(text: str):
    """打印错误信息"""
    print(colorize(f"✗ {text}", 'red'))

def print_info(text: str):
    """打印信息"""
    print(colorize(f"ℹ {text}", 'blue'))

# ==================== Base64工具 ====================
def base64_encode(text: str) -> str:
    """Base64编码"""
    return base64.b64encode(text.encode('utf-8')).decode('ascii')

def base64_decode(text: str) -> str:
    """Base64解码"""
    try:
        return base64.b64decode(text.encode('ascii')).decode('utf-8')
    except Exception as e:
        raise ValueError(f"Base64解码失败: {e}")

def base64_file_encode(file_path: str) -> str:
    """文件Base64编码"""
    with open(file_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('ascii')

def base64_file_decode(data: str, output_path: str):
    """Base64解码为文件"""
    with open(output_path, 'wb') as f:
        f.write(base64.b64decode(data.encode('ascii')))

# ==================== URL工具 ====================
def url_encode(text: str, safe: str = '') -> str:
    """URL编码"""
    return urllib.parse.quote(text, safe=safe)

def url_decode(text: str) -> str:
    """URL解码"""
    return urllib.parse.unquote(text)

def url_parse(url: str) -> Dict[str, str]:
    """URL解析"""
    parsed = urllib.parse.urlparse(url)
    return {
        'scheme': parsed.scheme,
        'netloc': parsed.netloc,
        'path': parsed.path,
        'params': parsed.params,
        'query': parsed.query,
        'fragment': parsed.fragment,
        'hostname': parsed.hostname,
        'port': parsed.port,
        'username': parsed.username,
        'password': parsed.password,
    }

# ==================== HTML工具 ====================
def html_encode(text: str) -> str:
    """HTML实体编码"""
    return html.escape(text)

def html_decode(text: str) -> str:
    """HTML实体解码"""
    return html.unescape(text)

# ==================== 哈希工具 ====================
def hash_md5(text: str) -> str:
    """MD5哈希"""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def hash_sha1(text: str) -> str:
    """SHA1哈希"""
    return hashlib.sha1(text.encode('utf-8')).hexdigest()

def hash_sha256(text: str) -> str:
    """SHA256哈希"""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def hash_sha512(text: str) -> str:
    """SHA512哈希"""
    return hashlib.sha512(text.encode('utf-8')).hexdigest()

def hash_file(file_path: str, algorithm: str = 'sha256') -> str:
    """文件哈希"""
    h = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()

# ==================== UUID工具 ====================
def uuid_v1() -> str:
    """UUID v1 (基于时间)"""
    return str(uuid.uuid1())

def uuid_v4() -> str:
    """UUID v4 (随机)"""
    return str(uuid.uuid4())

def uuid_v5(namespace: str, name: str) -> str:
    """UUID v5 (基于命名空间)"""
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{namespace}:{name}"))

# ==================== 密码生成工具 ====================
def generate_password(length: int = 16, 
                      use_upper: bool = True,
                      use_lower: bool = True,
                      use_digits: bool = True,
                      use_special: bool = True) -> str:
    """生成安全密码"""
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += '!@#$%^&*()_+-=[]{}|;:,.<>?'

    if not chars:
        chars = string.ascii_letters + string.digits

    return ''.join(random.choice(chars) for _ in range(length))

def password_strength(password: str) -> Tuple[int, str]:
    """密码强度检测"""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password):
        score += 1

    if score <= 2:
        return score, "弱 - 建议使用更复杂的密码"
    elif score <= 4:
        return score, "中等 - 可以更安全"
    elif score <= 6:
        return score, "强 - 密码强度良好"
    else:
        return score, "非常强 - 密码安全性很高"

# ==================== JWT工具 ====================
def jwt_decode(token: str) -> Dict[str, Any]:
    """JWT解码（不验证签名）"""
    parts = token.split('.')
    if len(parts) != 3:
        raise ValueError("无效的JWT格式")

    header, payload, signature = parts

    # Base64URL解码
    def decode_base64url(data: str) -> str:
        # 添加padding
        padding = 4 - len(data) % 4
        if padding != 4:
            data += '=' * padding
        return base64.b64decode(
            data.replace('-', '+').replace('_', '/')
        ).decode('utf-8')

    header_obj = json.loads(decode_base64url(header))
    payload_obj = json.loads(decode_base64url(payload))

    return {
        'header': header_obj,
        'payload': payload_obj,
        'signature': signature,
    }

# ==================== 时间工具 ====================
def timestamp_to_datetime(timestamp: Optional[float] = None) -> str:
    """时间戳转日期时间"""
    if timestamp is None:
        timestamp = time.time()
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def datetime_to_timestamp(date_str: str, fmt: str = '%Y-%m-%d %H:%M:%S') -> float:
    """日期时间转时间戳"""
    dt = datetime.strptime(date_str, fmt)
    return dt.timestamp()

def current_timestamp() -> float:
    """获取当前时间戳"""
    return time.time()

def now_iso() -> str:
    """获取当前ISO时间"""
    return datetime.now(timezone.utc).isoformat()

def parse_cron(cron_expr: str) -> Dict[str, Any]:
    """解析Cron表达式"""
    parts = cron_expr.split()
    if len(parts) != 5:
        raise ValueError("Cron表达式格式错误，需要5个字段")

    names = ['minute', 'hour', 'day', 'month', 'weekday']
    result = dict(zip(names, parts))

    # 解释每个字段
    explanations = []
    explanations.append(f"分 (Minute): {parts[0]} - {get_cron_description(parts[0], '分钟')}")
    explanations.append(f"时 (Hour): {parts[1]} - {get_cron_description(parts[1], '小时')}")
    explanations.append(f"日 (Day): {parts[2]} - {get_cron_description(parts[2], '日期')}")
    explanations.append(f"月 (Month): {parts[3]} - {get_cron_description(parts[3], '月份')}")
    explanations.append(f"周 (Weekday): {parts[4]} - {get_weekday_description(parts[4])}")

    result['explanations'] = explanations
    return result

def get_cron_description(field: str, unit: str) -> str:
    """获取Cron字段描述"""
    if field == '*':
        return f"每{unit}"
    elif field.startswith('*/'):
        return f"每{field[2:]}{unit}"
    elif ',' in field:
        return f"在{field}这些{unit}"
    elif '-' in field:
        return f"从{field.replace('-', '到')}{unit}"
    else:
        return f"在第{field}{unit}"

def get_weekday_description(field: str) -> str:
    """获取星期描述"""
    weekdays = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
    if field == '*':
        return "每天"
    elif field.isdigit():
        idx = int(field) % 7
        return weekdays[idx]
    else:
        return field

# ==================== 正则工具 ====================
def regex_test(pattern: str, text: str, flags: int = 0) -> Dict[str, Any]:
    """正则表达式测试"""
    try:
        regex = re.compile(pattern, flags)
        matches = regex.finditer(text)
        result = []

        for match in matches:
            result.append({
                'match': match.group(),
                'start': match.start(),
                'end': match.end(),
                'groups': match.groups(),
                'group_dict': match.groupdict(),
            })

        return {
            'valid': True,
            'matches': result,
            'match_count': len(result),
        }
    except re.error as e:
        return {
            'valid': False,
            'error': str(e),
            'matches': [],
            'match_count': 0,
        }

# ==================== 文本工具 ====================
def text_stats(text: str) -> Dict[str, int]:
    """文本统计"""
    lines = text.split('\n')
    return {
        'lines': len(lines),
        'words': len(text.split()),
        'characters': len(text),
        'characters_no_space': len(text.replace(' ', '')),
    }

def case_convert(text: str, style: str) -> str:
    """大小写转换"""
    if style == 'upper':
        return text.upper()
    elif style == 'lower':
        return text.lower()
    elif style == 'title':
        return text.title()
    elif style == 'camel':
        words = re.split(r'[\s_]+', text)
        return words[0].lower() + ''.join(w.capitalize() for w in words[1:])
    elif style == 'snake':
        return re.sub(r'[\s]+', '_', text.lower())
    elif style == 'kebab':
        return re.sub(r'[\s]+', '-', text.lower())
    elif style == 'constant':
        return re.sub(r'[\s]+', '_', text.upper())
    else:
        return text

def text_diff(text1: str, text2: str) -> List[Dict[str, Any]]:
    """文本差异对比（简单实现）"""
    lines1 = text1.split('\n')
    lines2 = text2.split('\n')

    diff = []
    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        line1 = lines1[i] if i < len(lines1) else None
        line2 = lines2[i] if i < len(lines2) else None

        if line1 == line2:
            diff.append({'type': 'same', 'line': i+1, 'content': line1})
        elif line1 is None:
            diff.append({'type': 'add', 'line': i+1, 'content': line2})
        elif line2 is None:
            diff.append({'type': 'delete', 'line': i+1, 'content': line1})
        else:
            diff.append({'type': 'change', 'line': i+1, 'old': line1, 'new': line2})

    return diff

# ==================== 颜色工具 ====================
def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """HEX转RGB"""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    if len(hex_color) != 6:
        raise ValueError("无效的HEX颜色格式")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r: int, g: int, b: int) -> str:
    """RGB转HEX"""
    return f"#{r:02x}{g:02x}{b:02x}"

def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """RGB转HSL"""
    r, g, b = r/255, g/255, b/255
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    l = (max_c + min_c) / 2

    if max_c == min_c:
        h = s = 0
    else:
        d = max_c - min_c
        s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        if max_c == r:
            h = ((g - b) / d + (g < b)) * 60
        elif max_c == g:
            h = ((b - r) / d + 2) * 60
        else:
            h = ((r - g) / d + 4) * 60

    return round(h, 1), round(s * 100, 1), round(l * 100, 1)

def hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
    """HSL转RGB"""
    h, s, l = h / 360, s / 100, l / 100

    if s == 0:
        r = g = b = l
    else:
        def hue_to_rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1
            if t < 1/6: return p + (q - p) * 6 * t
            if t < 1/2: return q
            if t < 2/3: return p + (q - p) * (2/3 - t) * 6
            return p

        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)

    return round(r * 255), round(g * 255), round(b * 255)

def preview_color(hex_color: str) -> str:
    """终端颜色预览"""
    r, g, b = hex_to_rgb(hex_color)
    # 计算前景色（黑色或白色）
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    fg = '\033[30m' if luminance > 0.5 else '\033[97m'
    return f"{fg}\033[48;2;{r};{g};{b}m 预览 {Colors.ENDC}"

# ==================== 随机工具 ====================
def random_string(length: int, charset: str = None) -> str:
    """随机字符串"""
    if charset is None:
        charset = string.ascii_letters + string.digits
    return ''.join(random.choice(charset) for _ in range(length))

def random_numbers(length: int) -> str:
    """随机数字"""
    return ''.join(random.choice(string.digits) for _ in range(length))

def random_hex(length: int) -> str:
    """随机十六进制"""
    return ''.join(random.choice('0123456789abcdef') for _ in range(length))

# ==================== 进制转换工具 ====================
def to_binary(text: str) -> str:
    """文本转二进制"""
    return ' '.join(format(ord(c), '08b') for c in text)

def from_binary(binary: str) -> str:
    """二进制转文本"""
    return ''.join(chr(int(b, 2)) for b in binary.split())

def to_hex_str(text: str) -> str:
    """文本转十六进制"""
    return ' '.join(format(ord(c), '02x') for c in text)

def from_hex_str(hex_str: str) -> str:
    """十六进制转文本"""
    return ''.join(chr(int(h, 16)) for h in hex_str.split())

# ==================== 莫尔斯电码工具 ====================
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

MORSE_REVERSE = {v: k for k, v in MORSE_CODE.items()}

def text_to_morse(text: str) -> str:
    """文本转莫尔斯电码"""
    return ' '.join(MORSE_CODE.get(c.upper(), c) for c in text)

def morse_to_text(morse: str) -> str:
    """莫尔斯电码转文本"""
    return ''.join(MORSE_REVERSE.get(c, c) for c in morse.split())

# ==================== JSON工具 ====================
def json_format(text: str, indent: int = 2) -> str:
    """JSON格式化"""
    obj = json.loads(text)
    return json.dumps(obj, ensure_ascii=False, indent=indent)

def json_minify(text: str) -> str:
    """JSON压缩"""
    obj = json.loads(text)
    return json.dumps(obj, ensure_ascii=False, separators=(',', ':'))

# ==================== 主程序 ====================
def main():
    parser = argparse.ArgumentParser(
        description=colorize('DevForge-CLI - 开发者瑞士军刀 | Zero Dependencies, Offline, Privacy-First', 'cyan'),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  devforge encode base64 "Hello World"
  devforge hash sha256 "text"
  devforge uuid v4
  devforge time now
  devforge color #ff5722
  devforge regex "\\d+" "test123"
  devforge -l

工具分类:
  encode      编码解码工具 (base64, url, html, unicode)
  hash        哈希计算工具 (md5, sha1, sha256, sha512)
  uuid        UUID生成工具 (v1, v4, v5)
  password    密码生成与检测
  jwt         JWT解码
  time        时间工具 (timestamp, cron, timezone)
  regex       正则表达式测试
  text        文本处理 (stats, case, diff)
  color       颜色转换与预览
  random      随机数据生成
  morse       莫尔斯电码
  json        JSON格式化与压缩
        """
    )

    parser.add_argument('-l', '--list', action='store_true', help='列出所有可用工具')
    parser.add_argument('-v', '--version', action='version', version='DevForge-CLI v1.0.0')
    parser.add_argument('tool', nargs='?', help='工具名称')
    parser.add_argument('subtool', nargs='?', help='子工具')
    parser.add_argument('input', nargs='?', help='输入值')
    parser.add_argument('--extra', nargs='?', help='额外参数')

    args = parser.parse_args()

    # 列出所有工具
    if args.list:
        print_header("DevForge-CLI 可用工具列表")
        categories = {
            "📦 编码解码 (encode)": ["base64", "url", "html", "unicode", "binary", "hex"],
            "🔐 哈希计算 (hash)": ["md5", "sha1", "sha256", "sha512"],
            "🆔 UUID生成 (uuid)": ["v1", "v4", "v5"],
            "🔑 密码工具 (password)": ["generate", "strength"],
            "🎫 JWT工具 (jwt)": ["decode"],
            "⏰ 时间工具 (time)": ["now", "timestamp", "cron"],
            "📝 正则工具 (regex)": ["test"],
            "📄 文本工具 (text)": ["stats", "case", "diff"],
            "🎨 颜色工具 (color)": ["hex2rgb", "rgb2hex", "preview"],
            "🎲 随机工具 (random)": ["string", "number", "hex"],
            "📡 莫尔斯电码 (morse)": ["encode", "decode"],
            "📋 JSON工具 (json)": ["format", "minify"],
        }
        for cat, tools in categories.items():
            print(colorize(f"\n{cat}", 'bold'))
            print(', '.join(f"  {t}" for t in tools))
        print()
        return

    if not args.tool:
        parser.print_help()
        return

    tool = args.tool.lower()
    subtool = args.subtool.lower() if args.subtool else None
    input_val = args.input

    try:
        # Base64工具
        if tool == 'encode' or tool == 'base64':
            if subtool == 'encode' or subtool == 'e' or subtool == 'enc':
                if input_val:
                    result = base64_encode(input_val)
                    print_success(f"Base64编码结果:")
                    print(result)
                else:
                    print_error("请提供要编码的文本")
            elif subtool == 'decode' or subtool == 'd' or subtool == 'dec':
                if input_val:
                    result = base64_decode(input_val)
                    print_success("Base64解码结果:")
                    print(result)
                else:
                    print_error("请提供要解码的Base64字符串")
            else:
                print_error(f"未知的子工具: {subtool}")
                print_info("可用: encode, decode")

        # URL工具
        elif tool == 'url':
            if subtool == 'encode' or subtool == 'enc':
                if input_val:
                    result = url_encode(input_val)
                    print_success("URL编码结果:")
                    print(result)
                else:
                    print_error("请提供要编码的URL")
            elif subtool == 'decode' or subtool == 'dec':
                if input_val:
                    result = url_decode(input_val)
                    print_success("URL解码结果:")
                    print(result)
                else:
                    print_error("请提供要解码的URL")
            elif subtool == 'parse':
                if input_val:
                    result = url_parse(input_val)
                    print_success("URL解析结果:")
                    for k, v in result.items():
                        print(f"  {k}: {v}")
                else:
                    print_error("请提供要解析的URL")
            else:
                print_error(f"未知的子工具: {subtool}")

        # HTML工具
        elif tool == 'html':
            if subtool == 'encode' or subtool == 'enc':
                if input_val:
                    result = html_encode(input_val)
                    print_success("HTML编码结果:")
                    print(result)
                else:
                    print_error("请提供要编码的HTML")
            elif subtool == 'decode' or subtool == 'dec':
                if input_val:
                    result = html_decode(input_val)
                    print_success("HTML解码结果:")
                    print(result)
                else:
                    print_error("请提供要解码的HTML")

        # 哈希工具
        elif tool == 'hash' or tool == 'md5':
            algo = 'md5'
            if tool != 'hash' or subtool:
                algo = subtool or 'md5'

            if input_val:
                if algo == 'md5':
                    result = hash_md5(input_val)
                elif algo == 'sha1':
                    result = hash_sha1(input_val)
                elif algo == 'sha256':
                    result = hash_sha256(input_val)
                elif algo == 'sha512':
                    result = hash_sha512(input_val)
                else:
                    print_error(f"不支持的哈希算法: {algo}")
                    return
                print_success(f"{algo.upper()}哈希结果:")
                print(result)
            else:
                print_error("请提供要哈希的文本")

        # UUID工具
        elif tool == 'uuid':
            if subtool == 'v1':
                print_success("UUID v1 (基于时间):")
                print(uuid_v1())
            elif subtool == 'v4':
                print_success("UUID v4 (随机):")
                print(uuid_v4())
            elif subtool == 'v5':
                namespace = input_val or 'example.com'
                name = args.extra or 'name'
                print_success(f"UUID v5 (基于命名空间 '{namespace}'):")
                print(uuid_v5(namespace, name))
            else:
                print_info("可用UUID类型: v1, v4, v5")
                print(f"\n  v1 (时间): {uuid_v1()}")
                print(f"  v4 (随机): {uuid_v4()}")

        # 密码工具
        elif tool == 'password' or tool == 'pass':
            if subtool == 'generate' or subtool == 'gen' or subtool == 'gen':
                length = int(args.extra) if args.extra else 16
                result = generate_password(length)
                print_success(f"生成的密码 (长度: {length}):")
                print(colorize(result, 'green'))
            elif subtool == 'strength' or subtool == 'check':
                if input_val:
                    score, feedback = password_strength(input_val)
                    print_success("密码强度分析:")
                    print(f"  密码: {'*' * len(input_val)}")
                    print(f"  强度: {score}/7")
                    print(f"  评估: {feedback}")
                else:
                    print_error("请提供要检测的密码")
            else:
                length = int(input_val) if input_val else 16
                result = generate_password(length)
                print_success(f"生成密码 (长度: {length}):")
                print(colorize(result, 'green'))

        # JWT工具
        elif tool == 'jwt':
            if subtool == 'decode' or subtool == 'd':
                if input_val:
                    result = jwt_decode(input_val)
                    print_success("JWT解码结果:")
                    print(f"\nHeader:")
                    print(json.dumps(result['header'], indent=2))
                    print(f"\nPayload:")
                    print(json.dumps(result['payload'], indent=2, ensure_ascii=False))
                    print(f"\nSignature: {result['signature']}")
                else:
                    print_error("请提供JWT Token")
            else:
                print_info("用法: devforge jwt decode <token>")

        # 时间工具
        elif tool == 'time' or tool == 'timestamp':
            print_success("当前时间信息:")
            print(f"  Unix时间戳: {current_timestamp()}")
            print(f"  ISO格式: {now_iso()}")
            print(f"  可读格式: {timestamp_to_datetime()}")

            if input_val:
                try:
                    ts = float(input_val)
                    print(f"\n时间戳 {ts} 转换:")
                    print(f"  -> {timestamp_to_datetime(ts)}")
                except:
                    print_error(f"无效的时间戳: {input_val}")

        elif tool == 'cron':
            if input_val:
                result = parse_cron(input_val)
                print_success(f"Cron表达式解析: {input_val}")
                for exp in result['explanations']:
                    print(f"  {exp}")
            else:
                print_info("用法: devforge cron \"* * * * *\"")
                print_info("格式: 分 时 日 月 周")

        # 正则工具
        elif tool == 'regex' or tool == 're':
            pattern = input_val
            text = args.extra

            if not pattern:
                print_info("用法: devforge regex <pattern> <text>")
                print_info("示例: devforge regex '\\d+' 'test123abc'")
                return

            if not text:
                text = input("请输入测试文本: ")

            result = regex_test(pattern, text)
            if result['valid']:
                print_success(f"正则匹配结果 (匹配 {result['match_count']} 个):")
                for i, m in enumerate(result['matches'], 1):
                    print(f"\n  匹配 {i}:")
                    print(f"    内容: {colorize(m['match'], 'green')}")
                    print(f"    位置: {m['start']}-{m['end']}")
                    if m['groups']:
                        print(f"    分组: {m['groups']}")
            else:
                print_error(f"正则表达式错误: {result['error']}")

        # 文本工具
        elif tool == 'text':
            if subtool == 'stats':
                if input_val:
                    stats = text_stats(input_val)
                    print_success("文本统计:")
                    for k, v in stats.items():
                        print(f"  {k}: {v}")
                else:
                    print_error("请提供要统计的文本")
            elif subtool == 'case':
                text_val = input_val or ""
                print_success("大小写转换示例:")
                print(f"  原文本: {text_val}")
                print(f"  UPPER: {case_convert(text_val, 'upper')}")
                print(f"  lower: {case_convert(text_val, 'lower')}")
                print(f"  Title: {case_convert(text_val, 'title')}")
                print(f"  camelCase: {case_convert(text_val, 'camel')}")
                print(f"  snake_case: {case_convert(text_val, 'snake')}")
                print(f"  kebab-case: {case_convert(text_val, 'kebab')}")
            else:
                if input_val:
                    stats = text_stats(input_val)
                    print_success("文本统计:")
                    for k, v in stats.items():
                        print(f"  {k}: {v}")

        # 颜色工具
        elif tool == 'color' or tool == 'colour':
            if not input_val:
                print_info("用法: devforge color <hex> [rgb|hsl|preview]")
                return

            try:
                r, g, b = hex_to_rgb(input_val)
                h, s, l = rgb_to_hsl(r, g, b)

                print_success(f"颜色: {input_val}")
                print(f"\n{preview_color(input_val)}")
                print(f"  HEX: {input_val.upper()}")
                print(f"  RGB: rgb({r}, {g}, {b})")
                print(f"  HSL: hsl({h}, {s}%, {l}%)")

                if subtool == 'rgb':
                    print(f"\nRGB: rgb({r}, {g}, {b})")
                elif subtool == 'hex':
                    print(f"\nHEX: {input_val.upper()}")
                elif subtool == 'preview':
                    print(f"\n颜色预览:")
                    for i in range(10):
                        shade = f"#{int(r*(1-i/15)):02x}{int(g*(1-i/15)):02x}{int(b*(1-i/15)):02x}"
                        print(preview_color(shade))
            except Exception as e:
                print_error(f"颜色格式错误: {e}")

        # 随机工具
        elif tool == 'random' or tool == 'rand':
            length = int(input_val) if input_val else 16

            if subtool == 'string' or subtool == 'str':
                result = random_string(length)
            elif subtool == 'number' or subtool == 'num':
                result = random_numbers(length)
            elif subtool == 'hex':
                result = random_hex(length)
            else:
                result = random_string(length)

            print_success(f"随机字符串 (长度: {length}):")
            print(colorize(result, 'cyan'))

        # 莫尔斯电码
        elif tool == 'morse':
            if not input_val:
                print_info("用法: devforge morse encode|decode <text>")
                return

            if subtool == 'encode' or subtool == 'enc':
                result = text_to_morse(input_val)
                print_success("莫尔斯电码:")
                print(result)
            elif subtool == 'decode' or subtool == 'dec':
                result = morse_to_text(input_val)
                print_success("解码结果:")
                print(result)
            else:
                print_info("用法: devforge morse encode|decode <text>")

        # JSON工具
        elif tool == 'json' or tool == 'jq':
            if not input_val:
                print_info("用法: devforge json format|minify <json>")
                return

            try:
                if subtool == 'format' or subtool == 'f':
                    result = json_format(input_val)
                elif subtool == 'minify' or subtool == 'm':
                    result = json_minify(input_val)
                else:
                    result = json_format(input_val)

                print_success("JSON处理结果:")
                print(result)
            except json.JSONDecodeError as e:
                print_error(f"JSON格式错误: {e}")
            except Exception as e:
                print_error(f"处理失败: {e}")

        # 进制转换
        elif tool == 'binary' or tool == 'bin':
            if not input_val:
                print_info("用法: devforge binary <text>")
                return

            print_success("二进制转换:")
            print(to_binary(input_val))

        elif tool == 'hex':
            if not input_val:
                print_info("用法: devforge hex <text>")
                return

            print_success("十六进制转换:")
            print(to_hex_str(input_val))

        else:
            print_error(f"未知工具: {tool}")
            print_info("使用 'devforge -l' 查看所有可用工具")

    except Exception as e:
        print_error(f"执行错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
