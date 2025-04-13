You're not alone—many devs working across projects end up with a tangled mess of Python versions 😅. Here's a **clean, reliable, and dev-friendly** way to manage multiple Python versions on macOS:

---

## ✅ **Best Practice: Use `pyenv` + `pyenv-virtualenv`**

### 🔧 **Step 1: Install `pyenv` (Manages Python versions)**  
```bash
brew update
brew install pyenv
```

> Tip: Add this to your `~/.zshrc` (or `~/.bash_profile`):
```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```
Then reload:
```bash
source ~/.zshrc
```

---

### 🧰 **Step 2: Install `pyenv-virtualenv` (Optional but awesome)**  
```bash
brew install pyenv-virtualenv
```

Add this to your `.zshrc`:
```bash
eval "$(pyenv virtualenv-init -)"
```

---

### 🐍 **Step 3: Install and Use Python Versions**  
```bash
pyenv install 3.11.7
pyenv install 3.10.13
pyenv install 3.9.18
```

Set your global Python version:
```bash
pyenv global 3.11.7
```

Set a local version per project:
```bash
cd ~/your_project
pyenv local 3.10.13 # setup the python version to current project folder. 
```

Check current Python version:
```bash
pyenv version
python --version
```

---

### 📦 **Step 4 (Optional): Create Virtual Envs Per Project**  
```bash
pyenv virtualenv 3.10.13 project-env # it will create virtual env under the ~/.pyenv folder
pyenv activate project-env
```

Or just set `.python-version` in the project folder to the virtualenv name.

---

## 🧹 **Cleaning Up Old Python Versions**
If you installed Python manually or through other methods:
```bash
# See where your python executables are:
which -a python
which -a python3

# Check what Homebrew installed:
brew list | grep python
```

You can uninstall unneeded versions:
```bash
brew uninstall python@3.X
```

Just be cautious about the **system Python** (`/usr/bin/python`), which is used by macOS itself—**don't touch it**.

---

## 🔁 Bonus: Quick Switch with Aliases  
* The pyenv shell command is used to temporarily set the Python version for the current shell session. 
* When you run pyenv shell 3.11.7, you are telling pyenv to use Python version 3.11.7 for the **current terminal session only**.

You can create terminal aliases like:
```bash
alias py310="pyenv shell 3.10.13"
alias py311="pyenv shell 3.11.7"
```

---

Want me to help you audit your current Python setup and clean it up safely? Just drop the output of:  
```bash
which -a python python3
pyenv versions
```

---
## create virtualenv under each project
Yes, you are absolutely correct!

You can use `pyenv` to **lock the Python version** for a specific project with the `pyenv local` command, and then use `python -m venv .venv` to create a **virtual environment** inside the project directory. Here's a step-by-step guide to make it work:

### **Steps:**

1. **Set the Python Version for Your Project:**
   Use `pyenv` to **set the Python version** locally for the project folder. This ensures that whenever you are in the project directory, `pyenv` will automatically use the specified Python version.

   Example:
   ```bash
   pyenv local 3.10.17
   ```

   This will create a `.python-version` file in your project folder, which locks the Python version to `3.10.17` for that project.

2. **Create the Virtual Environment:**
   Now that `pyenv` is using the correct version (e.g., `3.10.17`), you can create the virtual environment in the project folder using:
   ```bash
   python -m venv .venv
   ```

   This will create a `.venv` folder in your project directory, containing the isolated Python environment.

3. **Activate the Virtual Environment:**
   To activate the virtual environment, use:
   - For macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - For Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install Dependencies:**
   With the virtual environment activated, you can install your project dependencies using `pip`:
   ```bash
   pip install <your-dependency>
   ```

5. **Deactivating the Virtual Environment:**
   When you're done, you can deactivate the virtual environment with:
   ```bash
   deactivate
   ```

---

### **Summary:**
- Use `pyenv local <python-version>` to lock the Python version for your project.
- Use `python -m venv .venv` to create the virtual environment inside the project folder.
- Activate the virtual environment and install dependencies as needed.

This approach gives you both version control for Python (using `pyenv`) and isolated environments for each project (using `python -m venv`). It's a great way to manage multiple projects with different Python versions and dependencies!





## Deactivate
1. using `pyenv deactivate` your virtualenv, 
2. If you still see the environment name in your prompt, manually clear it: 
```sh
unset VIRTUAL_ENV
```
3. Sometimes the shell keeps the virtual environment active. Reset it using:
```sh
exec $SHELL -l # Force Deactivation (Reset Shell)
```