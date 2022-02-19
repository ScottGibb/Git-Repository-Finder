import os
import subprocess
import time

MAX_COUNT = 10000000
counter = 0
root_dir = os.getcwd()
cwd = os.getcwd()

"""
User Input
"""
print("Current working directory: {0}".format(cwd))
gitlab_domain = input("Please enter the domain of the remote you want to push too:")
folder_path = input("Enter the filepath for which you want to start looking for git repositories:")
os.chdir(folder_path)
cwd = os.getcwd()

"""
Locate repositories
"""
repository_filepaths = []
repository_names = []
f = open("repository_filepaths", "a")
print("Starting folder scan:")
for subdir, dirs, files in os.walk(cwd):
    for dir in dirs:
        if dir.endswith(".git"):
            filepath = subdir + os.sep
            repository_filepaths.append(filepath)
            f.write(filepath+"\n")
            print("-----------------------------------")
            print("Git repository Found: " + filepath)
            endIndex = subdir.rfind(os.sep)
            repository_name = subdir[endIndex + 1:subdir.__len__()]
            repository_name = repository_name.replace(" ", "-")
            print("Git repository Name: " + repository_name)
            repository_names.append(repository_name)
            print("-----------------------------------")
        if counter == MAX_COUNT:
            print("Im Still going!)")
            counter = 0
        counter += 1
f.close()
print("Found {0} repositories".format(repository_filepaths.__len__()))


"""
Update repositories
"""
os.chdir(root_dir)
f = open("Repositories.txt", "a")
for index in range(0, repository_filepaths.__len__()):
    if repository_names[index].__contains__("MT3"):
        print("HERE")
    os.chdir(repository_filepaths[index])
    print("Uploading to new Remote Repository")
    print("Current Working Directory:{0}".format(repository_filepaths[index]))
    print(os.popen("git remote rename origin old_origin").read())
    print(os.popen("git add .").read())
    print(os.popen("git commit -m \"Final Commit:{0}\"".format(repository_filepaths[index])).read())
    print(os.popen("git remote add origin {0}{1}.git".format(gitlab_domain, repository_names[index])).read())
    print(os.popen("git push origin --all").read())
    print(os.popen("git push origin --tags").read())
    f.write(repository_names[index])

f.close()
print("DONE :D")
