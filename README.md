# ReName Subtitles (RNS)
A simple python script to sort, rename and reorder subtitle files depending on their videos names.
### Dependencies
* python
* [inquirer](https://pypi.org/project/python-inquirer/)
### Install
#### Linux
first you need to install the inquirer module
```
pip install inquirer
```
clone the repo and run the script as shown in the Usage section.
```bash
git clone https://github.com/BishrGhalil/rns.git
cd rns
rns --help
```
#### Windows
1. Download the setup.exe file and install it.
2. Open the rns folder and run rns.exe.
### Usage
```bash
rns <videos directory> <subtitles directory>
```
### Example
```bash
rns "$HOME/Videos/Series/BreakingBad" "$HOME/Downloads/BreakingBad-Subs"
```
