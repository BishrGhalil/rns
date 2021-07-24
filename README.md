# SubMan (Subtitle Manager)
A simple python script to manage subtitle files.
### Dependencies
##### for linux only
* python
* [inquirer](https://pypi.org/project/python-inquirer/)
### Install
#### Linux
first you need to install the inquirer module
```
pip install inquirer
```
clone the repo and run the script.
```bash
git clone https://github.com/BishrGhalil/subman
cd subman
sudo ln -s subman /bin/subman
```
#### Windows
1. Download the setup.exe file and install it.
2. Open the rns folder and run rns.exe.
### Usage
You can pass the directories as arguments:
```bash
subman <videos directory> <subtitles directory>
```
Or you can run it without arguments:
```
$ subman
Enter videos path:
Enter Subtitles path:
```
