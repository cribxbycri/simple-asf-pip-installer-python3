while 1==1:
  from pip._internal import main as pipmain
  request = input("what package do you wish to install? ")
  pipmain(['install', request])