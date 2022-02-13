import os
import subprocess

GITLAB_DOMAIN = "git@192.168.0.69:SGIBB98/"

cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

repository_filepaths = []
repository_names = []

print("Starting folder scan:")
for subdir, dirs, files in os.walk(cwd):
    for dir in dirs:
        if dir.endswith(".git"):
            filepath = subdir + os.sep
            repository_filepaths.append(filepath)
            print("-----------------------------------")
            print("Git repository Found: " + filepath)
            endIndex = subdir.rfind(os.sep)
            repository_name = subdir[endIndex + 1:subdir.__len__()]
            print("Git repository Name: " + repository_name)
            repository_names.append(repository_name)
            print("-----------------------------------")

for index in range(0, repository_filepaths.__len__()):
    os.chdir(repository_filepaths[index])
    print(os.popen("git remote rename origin old_origin").read())
    print(os.popen("git push --set-upstream {0}{1}.git all".format(GITLAB_DOMAIN, repository_name)).read())
