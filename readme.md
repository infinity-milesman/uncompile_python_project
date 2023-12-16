# This repo shows, how we can generate a compiled file of a Python program and then decompile it using the uncompyle6 library. 
Make two directories compiled_result, and final_result in the root directory and place the original Python file in the root directory.

To compile the file 
> python -m compileall . && mv *.pyc compiled_result/

You will get the compiled file in compiled_result folder.

First, we will need to install the uncompyle6 package to decompile the file. Install that using this command,
pip install uncompyle6

Go to compile_result folder and hit this command,
> uncompyle6 -o ../final_result sample.pyc

You will see the original .py file in final_result folder.

References:

[uncompyle6](https://medium.com/cassandra-cryptoassets/how-to-decompile-compiled-pyc-python-files-50e5f45d1edb)

[Compile all files](https://stackoverflow.com/questions/5607283/how-can-i-manually-generate-a-pyc-file-from-a-py-file)
