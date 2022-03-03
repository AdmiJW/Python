
# Note: This doesn't really involve code. This just note how you can compile your game written in pygame so far into
# a executable file so you can distribute or share to your friends.
#
#
# There are many python executable compiler out there like pyinstaller, cx_freeze, or py2exe. In this note,
# we'll be using pyinstaller to be consistent to dafluffypotato's tutorial.
#
#
# > First, ensure pyinstaller is installed in your pip globally.
#       - Open up a command prompt (not virtual environment). Run `pip install pyinstaller`
#       - Ensure pyinstaller is installed globally by running `pyinstaller` (Sometimes virtual env is not properly
#         set, you need to add the path manually). You should see some manual from pyinstaller
# > With pyinstaller installed, navigate into your game-containing directory. `cd` into the directory
# > Say your entry script into your game is named `main.py`, then run:
#       pyinstaller main.py --noconsole --onefile
#
#   --noconsole > Prevents a console window from showing up when the game is ran
#   --onefile > Bundles your game into one single file .exe
#
# > Wait a while. You should see a `dist` folder being created (Along with other folders like `build`). Inside the
#   dist folder will be your game.
# > However, it may throw some error when you try to run it. The problem is you need to put all your assets (images,
#   musics etc) into the same structural hierarchy as if you run it in main.py. Copy your assets into the dist folder
#   to resolve the issue.
#
#
# > Also, if you are developing your program in Pycharm, you may encounter a problem where the pyinstaller couldn't
#   find the modules that you installed in your venv, but not global python environment.
#   In this case, you have to provide additional options when running the command, as mentioned in this Stackoverflow
#   answer: https://stackoverflow.com/questions/48757977/how-to-include-dependencies-from-venv-directory-when-running-pyinstaller-for-pro
#
#       pyinstaller --onefile --paths path\to\venv\Lib\site-packages main.py


# Tips:
#  > For minimum size executable, make sure you do it in your virtual environment where only needed libraries are
#    installed. Otherwise, it will compile from global environment where some of your libraries like `numpy`, `pandas`
#    etc are bundled together!
