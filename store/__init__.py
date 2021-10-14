import yaml

cfg = yaml.safe_load(open("./conf/db.yaml", "r"))

if cfg['mode'] == 'sqlite3':
    from . import SQLite3Store
    theStore = SQLite3Store(cfg['sqlite3']['loc'])

