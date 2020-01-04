import platform
os = platform.system()

if os == "Darwin":
  print("mac")
elif os == "Windows":
  print("window")
else:
  print("linux")