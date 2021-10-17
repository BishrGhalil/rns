# SubMan (Subtitle Manager)
A simple python script to manage subtitle files.
### Dependencies
##### for linux only
* python
* [inquirer](https://pypi.org/project/python-inquirer/)
### Install
#### Linux
```bash
git clone https://github.com/BishrGhalil/subman.git
cd subman
pip3 install -r requirements.txt
sudo make
```
#### Windows
1. Download the setup.exe file and install it.
2. Open the subman folder and run subman.exe.
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
