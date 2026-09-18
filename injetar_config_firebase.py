#!/usr/bin/env python3
import json
import pathlib
import sys

REQUIRED = ("apiKey", "authDomain", "projectId", "appId")
MARKER = "const FIREBASE_DEFAULT = null;"

if len(sys.argv) != 3:
    raise SystemExit("Uso: injetar_config_firebase.py ARQUIVO_HTML JSON_FIREBASE")

target = pathlib.Path(sys.argv[1])
config = json.loads(sys.argv[2])

missing = [name for name in REQUIRED if not config.get(name)]
if missing:
    raise SystemExit("Configuração Firebase incompleta: " + ", ".join(missing))
if "private_key" in config or config.get("type") == "service_account":
    raise SystemExit("Use a configuração pública do aplicativo Web, nunca uma conta de serviço.")

content = target.read_text(encoding="utf-8")
if MARKER not in content:
    raise SystemExit("Marcador FIREBASE_DEFAULT não encontrado no HTML.")

replacement = "const FIREBASE_DEFAULT = " + json.dumps(
    config, ensure_ascii=False, separators=(",", ":")
) + ";"
target.write_text(content.replace(MARKER, replacement, 1), encoding="utf-8")
print("Configuração Firebase inserida no arquivo de publicação.")

