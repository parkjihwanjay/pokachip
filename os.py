import platform

# 해당 운영체제 확인
def checkSystem():
    os = platform.system()

    if os == "Darwin":
        return "mac"
    elif os == "Windows":
        return "win"
    else:
        return "linux"