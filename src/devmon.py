import platform
import os

repo = os.path.dirname(os.path.dirname(__file__))
binaries = {
    "Linux": os.path.join(repo, "devmon-logi/linux/x64/logi-devmon"),
    "s": os.path.join(repo, "devmon-logi/macos/logi-devmon"),
    "Windows": os.path.join(repo, "devmon-logi/Windows/x64/logi-devmon.exe"),
}

if platform.system() not in binaries:
    print("\x1b[31mYour platform ("+platform.system()+") is not supported by this software.\x1b[0m")
    exit(1)

binary = binaries[platform.system()]
