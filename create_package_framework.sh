touch main.py
touch requirements.txt
mkdir ${PWD##*/}
touch ${PWD##*/}/__init__.py
mkdir ${PWD##*/}/src
touch ${PWD##*/}/src/__init__.py
touch ${PWD##*/}/src/utils.py
echo "from .utils import *" >> ${PWD##*/}/src/__init__.py
echo "from .src import *" >> ${PWD##*/}/__init__.py
rm create_package_framework.sh