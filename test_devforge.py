#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevForge-CLI 功能测试脚本
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import devforge

def test_base64():
    """测试Base64编解码"""
    print("测试 Base64...")
    text = "Hello, DevForge!"
    encoded = devforge.base64_encode(text)
    decoded = devforge.base64_decode(encoded)
    assert decoded == text, f"Base64测试失败: {decoded} != {text}"
    print("✓ Base64 测试通过")

def test_hash():
    """测试哈希计算"""
    print("测试 Hash...")
    text = "test"
    md5 = devforge.hash_md5(text)
    sha256 = devforge.hash_sha256(text)

    # 验证已知值
    assert md5 == "098f6bcd4621d373cade4e832627b4f6", f"MD5错误: {md5}"
    assert sha256 == "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08", f"SHA256错误: {sha256}"
    print("✓ Hash 测试通过")

def test_uuid():
    """测试UUID生成"""
    print("测试 UUID...")
    v1 = devforge.uuid_v1()
    v4 = devforge.uuid_v4()

    assert len(v1) == 36, f"UUID v1长度错误: {len(v1)}"
    assert len(v4) == 36, f"UUID v4长度错误: {len(v4)}"
    print("✓ UUID 测试通过")

def test_password():
    """测试密码生成"""
    print("测试 Password...")
    pwd = devforge.generate_password(16)
    assert len(pwd) == 16, f"密码长度错误: {len(pwd)}"

    score, feedback = devforge.password_strength("StrongP@ss123!")
    assert score > 0, "密码强度检测失败"
    print("✓ Password 测试通过")

def test_regex():
    """测试正则表达式"""
    print("测试 Regex...")
    result = devforge.regex_test(r'\d+', 'test123abc')
    assert result['valid'] == True, "正则验证失败"
    assert result['match_count'] == 1, f"匹配数量错误: {result['match_count']}"
    assert result['matches'][0]['match'] == '123', f"匹配结果错误: {result['matches'][0]['match']}"
    print("✓ Regex 测试通过")

def test_color():
    """测试颜色转换"""
    print("测试 Color...")
    r, g, b = devforge.hex_to_rgb('#ff5722')
    assert r == 255 and g == 87 and b == 34, f"RGB转换错误: ({r}, {g}, {b})"

    hex_color = devforge.rgb_to_hex(255, 87, 34)
    assert hex_color == '#ff5722', f"HEX转换错误: {hex_color}"
    print("✓ Color 测试通过")

def test_time():
    """测试时间工具"""
    print("测试 Time...")
    ts = devforge.current_timestamp()
    assert ts > 0, "时间戳获取失败"

    dt = devforge.timestamp_to_datetime(ts)
    assert len(dt) > 0, "时间转换失败"
    print("✓ Time 测试通过")

def test_morse():
    """测试莫尔斯电码"""
    print("测试 Morse...")
    morse = devforge.text_to_morse("SOS")
    assert morse == "... --- ...", f"编码错误: {morse}"

    text = devforge.morse_to_text("... --- ...")
    assert text == "SOS", f"解码错误: {text}"
    print("✓ Morse 测试通过")

def test_text():
    """测试文本工具"""
    print("测试 Text...")
    stats = devforge.text_stats("Hello\nWorld")
    assert stats['lines'] == 2, f"行数错误: {stats['lines']}"
    assert stats['words'] == 2, f"词数错误: {stats['words']}"

    snake = devforge.case_convert("Hello World", "snake")
    assert snake == "hello_world", f"snake转换错误: {snake}"
    print("✓ Text 测试通过")

def run_all_tests():
    """运行所有测试"""
    print("\n" + "="*60)
    print("DevForge-CLI 功能测试")
    print("="*60 + "\n")

    tests = [
        test_base64,
        test_hash,
        test_uuid,
        test_password,
        test_regex,
        test_color,
        test_time,
        test_morse,
        test_text,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"✗ {test.__name__} 测试失败: {e}")
            failed += 1

    print("\n" + "="*60)
    print(f"测试完成: {passed} 通过, {failed} 失败")
    print("="*60 + "\n")

    return failed == 0

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
