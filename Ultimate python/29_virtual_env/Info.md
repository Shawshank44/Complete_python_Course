A Python Virtual Environment (`venv`) is an isolated Python environment that allows you to install and manage project-specific packages without affecting your system-wide Python installation.

## 1. Create a complete Python virtual environment

Step 1: Create a project folder

```
mkdir my_python_project
cd my_python_project
```

Step 2: Create the virtual environment

```
python -m venv venv
```

If that doesn't work, try:

```
python3 -m venv venv
```

Step 3: Activate the virtual environment

\- Windows (CMD):

```
venv\Scripts\activate
```

\- Windows (PowerShell):

```
.\venv\Scripts\Activate.ps1
```

\- Linux / macOS:

```
source venv/bin/activate
```

Step 4: Upgrade pip

```
python -m pip install --upgrade pip
```

Step 5: Install Python packages

```
pip install numpy pandas matplotlib requests flask django
```

Step 6: Check installed packages

```
pip list
```

Step 7: Save dependencies

```
pip freeze > requirements.txt
```

Step 8: Deactivate the environment

```
deactivate
```

## 2. Project folder structure

my_python_project/

&#x20;venv/

Virtual environment

&#x20;main.py

&#x20;requirements.txt

&#x20;.gitignore

## 3. Create a test Python program

Create `main.py`:

```
import numpy as npimport pandas as pdimport matplotlib.pyplot as pltprint("Virtual Environment Working!")data = [10, 20, 30, 40, 50]print("NumPy Array:", np.array(data))df = pd.DataFrame(data, columns=["Values"])print(df)plt.plot(data)plt.title("Python Virtual Environment Test")plt.show()
```

Run it:

```
python main.py
```

## 4. Important commands

| Task                 | Command                           |
| -------------------- | --------------------------------- |
| Create environment   | `python -m venv venv`             |
| Activate (Windows)   | `venv\Scripts\activate`           |
| Activate (Linux)     | `source venv/bin/activate`        |
| Install package      | `pip install package_name`        |
| List packages        | `pip list`                        |
| Save dependencies    | `pip freeze > requirements.txt`   |
| Install dependencies | `pip install -r requirements.txt` |
| Deactivate           | `deactivate`                      |
| Delete environment   | Delete the `venv` folder          |
