# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile('test.txt', 'copy.txt')     #source then destination
                                            # destination can be a path location also


shutil.copy2('test.txt', 'copyy.txt')                              