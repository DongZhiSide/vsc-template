templates = []

generate_settings_key = "general/settings.txt"
generate_settings = {
    generate_settings_key: {
        "prefix": "gs",
        "body": [],
        "description": "生成通用配置",
        "exclude": "",
        "include": ["**/.vscode/settings.json", "**/*.code-workspace"],
        "isFileTemplate": False,
        "scope": "jsonc",
    }
}

generate_extensions_key = "general/extensions.txt"
generate_extensions = {
    generate_extensions_key: {
        "prefix": "ge",
        "body": [],
        "description": "生成通用扩展",
        "exclude": "",
        "include": ["**/.vscode/extensions.json", "**/*.code-workspace"],
        "isFileTemplate": False,
        "scope": "jsonc",
    }
}

templates.append("golang")

golang_settings_key = "golang/settings.txt"
golang_settings = {
    golang_settings_key: {
        "prefix": "gos",
        "body": [],
        "description": "生成 golang 配置",
        "exclude": "",
        "include": ["**/.vscode/settings.json", "**/*.code-workspace"],
        "isFileTemplate": False,
        "scope": "jsonc",
    }
}

golang_extensions_key = "golang/extensions.txt"
golang_extensions = {
    golang_extensions_key: {
        "prefix": "gol",
        "body": [],
        "description": "生成 golang 扩展",
        "exclude": "",
        "include": ["**/.vscode/extensions.json", "**/*.code-workspace"],
        "isFileTemplate": False,
        "scope": "jsonc",
    }
}

templates.append("python")

python_settings_key = "python/settings.txt"
python_settings = {
    python_settings_key: {
        "prefix": "pys",
        "body": [],
        "description": "生成 python 配置",
        "exclude": "",
        "include": ["**/.vscode/settings.json", "**/*.code-workspace"],
        "isFileTemplate": False,
        "scope": "jsonc",
    }
}

python_extensions_key = "python/extensions.txt"
python_extensions = {
    python_extensions_key: {
        "prefix": "pye",
        "body": [],
        "description": "生成 python 扩展",
        "exclude": "",
        "include": ["**/.vscode/extensions.json", "**/*.code-workspace"],
        "isFileTemplate": False,
        "scope": "jsonc",
    }
}