# vscode 配置样板

此仓库用于存储 vscode 配置样板.

`template*.json`是样板配置.

不需要手动复制配置, 直接依赖 vscode 的代码片段功能直接生成配置.

```shell
python generate.py -h
# usage: generate.py [-h] [--show] [-w] [-s] [-e] [-t] [-l] [template]
# 
# positional arguments:
#   template              要生成的模板列表
# 
# options:
#   -h, --help            show this help message and exit
#   --show                显示可生成的模板列表
#   -w, --generate-workspace
#                         生成 .code-workspace 文件
#   -s, --generate-settings
#                         生成 settings.json 文件
#   -e, --generate-extensions
#                         生成 extensions.json 文件
#   -t, --generate-tasks  生成 tasks.json 文件
#   -l, --generate-launch
#                         生成 launch.json 文件

# 生成 python 配置
python generate.py python

# 生成的 vst.code-snippets 后,
# 在 vscode 的配置触发建议就可以填充预定义配置
ls .vscode
# vst.code-snippets
```
