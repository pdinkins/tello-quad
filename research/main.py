__package__ = "tello-quad.research.main"
__version__ = "0.1.20"
import os

def download_repos():
    # dji sdk tello python 
    gitclone("https://github.com/dji-sdk/Tello-Python.git")
    # micro linux 
    gitclone("https://github.com/microlinux/tello.git")
    # jabrils tellotv 
    gitclone("https://github.com/Jabrils/TelloTV.git")
    # hanyazou tellopy 
    gitclone("https://github.com/hanyazou/TelloPy.git")
    # parakhm95 tello position controller 
    gitclone("https://github.com/parakhm95/Ryze-Tello-Position-Controller.git")
    # damia fuentes dji tello py
    gitclone("https://github.com/damiafuentes/DJITelloPy.git")


def gitclone(repo):
    # download the git repo into the downloads folder
    cmd = "git clone " + str(repo)
    os.system(cmd) 

def dr():
    download_repos()

def return_package_details():
    return (__package__ , __version__)


if __name__ == "__main__":
    return_package_details()