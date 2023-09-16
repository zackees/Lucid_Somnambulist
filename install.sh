# Run this command to install everything:
# curl -sSL https://raw.githubusercontent.com/zackees/Lucid_Somnambulist/main/install.sh | bash

set -e

conda deactivate || true


# Check if Miniconda is already installed
if [ ! -d "$HOME/miniconda3" ]; then
  # If it's not installed, download and install it
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  chmod +x Miniconda3-latest-Linux-x86_64.sh
  ./Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3
  echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> $HOME/.bashrc
  source $HOME/.bashrc
fi

# Verify Conda installation
conda --version

# Install molli_firstgen dependency
rm -rf molli_firstgen
git clone https://github.com/SEDenmarkLab/molli_firstgen.git
cd molli_firstgen
git pull
pip install .
cd ..

# Install Lucide_Somnambulist
rm -rf Lucid_Somnambulist
git clone https://github.com/zackees/Lucid_Somnambulist
cd Lucid_Somnambulist
conda deactivate || true
# Check if the environment exists and remove it
if conda info --envs | grep -q '^somn '; then
    conda env remove --name somn
fi
# Create the environment
conda env create --name somn --file Lucid_Somnambulist/somn.lock.yml
source ~/miniconda3/etc/profile.d/conda.sh
conda activate somn
cd Lucid_Somnambulist
pip install -e .
cd ..

# Test the installation
source .
conda init
conda activate somn
python -c "import somn"
if [ $? -eq 0 ]; then
  echo "Installation test successful. 'import somn' executed without errors."
fi

# Run somn
echo "Running 'somn'..."
conda activate somn
somn
