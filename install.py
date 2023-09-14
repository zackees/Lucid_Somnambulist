# curl -sSL https://raw.githubusercontent.com/zackees/Lucid_Somnambulist/main/install.py | python3

import os
import subprocess

def run_command(command):
    return subprocess.run(command, shell=True, check=True, text=True)

def conda_installed():
    return os.path.isdir(os.path.expanduser("~/miniconda3"))

try:
    run_command("conda deactivate")
except subprocess.CalledProcessError:
    pass

if not conda_installed():
    run_command("wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh")
    run_command("chmod +x Miniconda3-latest-Linux-x86_64.sh")
    run_command("./Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3")
    with open(os.path.expanduser("~/.bashrc"), "a") as file:
        file.write('export PATH="$HOME/miniconda3/bin:$PATH"\n')
    run_command("source $HOME/.bashrc")

run_command("conda --version")

if os.path.exists("molli_firstgen"):
    run_command("rm -rf molli_firstgen")
run_command("git clone https://github.com/SEDenmarkLab/molli_firstgen.git")
os.chdir("molli_firstgen")
run_command("git pull")
run_command("pip install .")
os.chdir("..")

if os.path.exists("Lucid_Somnambulist"):
    run_command("rm -rf Lucid_Somnambulist")
run_command("git clone https://github.com/zackees/Lucid_Somnambulist")
os.chdir("Lucid_Somnambulist")

try:
    run_command("conda deactivate")
except subprocess.CalledProcessError:
    pass

env_list = run_command("conda info --envs").stdout
if 'somn' in env_list:
    run_command("conda env remove --name somn")
    
run_command("conda env create --name somn --file Lucid_Somnambulist/somn.yml")
run_command("conda init")
run_command("conda activate somn")
os.chdir("Lucid_Somnambulist")
run_command("pip install -e .")
os.chdir("..")

try:
    run_command("source .")
except subprocess.CalledProcessError:
    pass

run_command("conda init")
run_command("conda activate somn")
try:
    run_command("python -c 'import somn'")
    print("Installation test successful. 'import somn' executed without errors.")
except subprocess.CalledProcessError:
    pass

print("Running 'somn'...")
run_command("conda activate somn")
run_command("somn")
