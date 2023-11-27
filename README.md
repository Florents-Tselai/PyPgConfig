# PyPgConfig 🐘❤️🐍

Acceess pg_config from Python

## Installation

Install this tool using `pip`:
```bash
pip install PyPgConfig
```

## Getting started

```python
from pypgconfig import detect

pgconf = detect()
pgconf.version # "15.4"
pgconf.version.major # 15
pgconf.version.minor # 4

pgconf.libs # ["pgcommon", "pgport", "lz4", "xml2" ]

pgconf.with_python # True
pgconf.pythonpath # Path("/opt/homebrew/bin/python3.11")
```

