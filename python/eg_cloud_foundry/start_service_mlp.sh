#export PYTHON_EXE="python"
#which python3 >> /dev/null
#if [ ${?} -eq 0 ];
#then
#        export PYTHON_EXE="python3"
#fi
#echo Using :; $PYTHON_EXE -V

#export PYTHONPATH=./ml-backend/src:.:./data-services/src
#$PYTHON_EXE -V 

.conda/bin/python webapp.py
