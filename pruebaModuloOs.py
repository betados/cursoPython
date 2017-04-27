import os
print(os.name)

for (nom, value) in list(os.environ.items()):
    print("%s - %s" % (nom, value))
