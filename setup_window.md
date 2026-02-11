# Setup virtual environment in python (windows - cmd, powershell, bash)

## 1 Create the virtual environment by running the venv module. It is a common practice to name the environment folder venv or .venv:
python -m venv .venv


## 2 Activate the virtual environment. The activation command depends on the shell you are using:

For Command Prompt (CMD):
.venv\Scripts\activate.bat

For PowerShell:
.\\.venv\\Scripts\\Activate.ps1

For Git Bash:
source .venv/Scripts/activate


## 3 Install packages. With the environment active, use pip to install packages. They will be installed locally to this environment only, not globally:

pip install package_name

## You can also install all packages listed in a requirements.txt file using the command:
pip install -r requirements.txt

## 4 Deactivate the environment. When you are finished working on the project, you can exit the virtual environment by simply typing:

deactivate