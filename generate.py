#!/bin/python3
# -*- coding: utf-8 -*-

import json
import os
import argparse
import shutil
from definition import *

script_dir = os.path.dirname(os.path.abspath(__file__))
dir_name = os.path.join(os.getcwd(), ".vscode")


def make_snippet_data(key: str) -> list:
    body_lines = []
    read_path = os.path.join(script_dir, key)
    with open(read_path, "r", encoding="utf-8") as f:
        for line in f:
            # 转义反斜杠和双引号
            escaped = line.replace("\\", "\\\\").replace('"', '\"').replace('$', '\\$').rstrip("\n")
            body_lines.append(escaped)
    return body_lines


def generate_snippet(objs: dict[str, dict[str, dict]]):
    with open(dir_name + "/vst.code-snippets", "w", encoding="utf-8") as f:
        json.dump(objs, f, indent=4, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--show", action="store_true", help="显示可生成的模板列表"
    )
    parser.add_argument(
        "-w",
        "--generate-workspace",
        action="store_true",
        help="生成 .code-workspace 文件",
    )
    parser.add_argument(
        "-s",
        "--generate-settings",
        action="store_true",
        help="生成 settings.json 文件",
    )
    parser.add_argument(
        "-e",
        "--generate-extensions",
        action="store_true",
        help="生成 extensions.json 文件",
    )
    parser.add_argument(
        "-t", "--generate-tasks", action="store_true", help="生成 tasks.json 文件"
    )
    parser.add_argument(
        "-l", "--generate-launch", action="store_true", help="生成 launch.json 文件"
    )
    parser.add_argument("template", nargs="?", help="要生成的模板列表")
    args = parser.parse_args()

    if args.show:
        for key in templates:
            print(key)
        exit()

    if not args.template:
        print("请输入要生成的模板名称")
        exit()

    if args.template not in templates:
        print("请输入正确的模板名称")
        exit()

    os.makedirs(dir_name, exist_ok=True)

    if args.generate_workspace:
        source = os.path.join(script_dir, "template.code-workspace.json")
        destination = os.path.join(os.getcwd(), "./work.code-workspace")
        shutil.copy(source, destination)

    if args.generate_extensions:
        source = os.path.join(script_dir, "template-extensions.json")
        destination = os.path.join(os.getcwd(), ".vscode/extensions.json")
        shutil.copy(source, destination)

    if args.generate_settings :
        source = os.path.join(script_dir, "template-settings.json")
        destination = os.path.join(os.getcwd(), ".vscode/settings.json")
        shutil.copy(source, destination)

    if args.generate_tasks:
        source = os.path.join(script_dir, "template-tasks.json")
        destination = os.path.join(os.getcwd(), ".vscode/tasks.json")

    if args.generate_launch:
        shutil.copy(source, destination)
        source = os.path.join(script_dir, "template-launch.json")
        destination = os.path.join(os.getcwd(), ".vscode/launch.json")
        shutil.copy(source, destination)

    objs = {}

    generate_settings[generate_settings_key]["body"] = make_snippet_data(
        generate_settings_key
    )
    generate_extensions[generate_extensions_key]["body"] = make_snippet_data(
        generate_extensions_key
    )
    objs.update(generate_extensions)
    objs.update(generate_settings)

    key = args.template

    if key == "golang":
        golang_settings[golang_settings_key]["body"] = make_snippet_data(
            golang_settings_key
        )
        golang_extensions[golang_extensions_key]["body"] = make_snippet_data(
            golang_extensions_key
        )
        objs.update(golang_extensions)
        objs.update(golang_settings)
    elif key == "python":
        python_settings[python_settings_key]["body"] = make_snippet_data(
            python_settings_key
        )
        python_extensions[python_extensions_key]["body"] = make_snippet_data(
            python_extensions_key
        )
        objs.update(python_extensions)
        objs.update(python_settings)

    generate_snippet(objs)


if __name__ == "__main__":
    main()
