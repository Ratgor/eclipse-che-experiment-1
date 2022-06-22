gr = f"Hello from Eclipse Che VS Code IDE"
print(gr)

import os, sys
print(f"currnet working directory {os.getcwd()} with the content {os.listdir()}")

print(f"system environment variables:")
for k,v in os.environ.items():
    print(f"{k} == {v}\n") 
