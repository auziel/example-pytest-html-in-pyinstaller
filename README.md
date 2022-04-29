Tested on Mac
# Setup dev env
```
python3 -m venv .venv
. .venv/bin/activate   
pip install -r requirements.txt 
```

# Kick pyinstallar
```
pip install pyinstaller

pyinstaller --onefile --noconfirm --nowindow --exclude-module PyQt5 \
    --add-data "3rdparty/pytest_html:./pytest_html" \
    --add-data  "tests:tests" \
    --add-data "mypkg:mypkg" \
    --additional-hooks-dir=hooks \
    --hidden-import=pytest_html \
    -n example mypkg/main.py
```

# test the bundle
```
./dist/example
```

# 3rdparty
3rdparty/pytest_html is copied from https://github.com/pytest-dev/pytest-html
