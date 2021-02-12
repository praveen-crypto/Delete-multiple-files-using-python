import os
#input = ("Enter the full path")

print("Enter the Full path name:")
path = input()
print("\n")

print("Enter the Extension name:")
extension = input()
print("\n")

files_in_directory = os.listdir(path)

filtered_files = []
count = 0

for file in files_in_directory:
    if file.endswith(extension):
        count += 1
        filtered_files.append(file)
        print(file)

print("\nTotal files found:", count)

answer = input("Do you want to delete these files (y/n) ")

answer = answer.lower()

if answer == "y":
    for file in filtered_files:
        path_to_file = os.path.join(path, file)
        os.remove(path_to_file)
elif answer == "n":
    print("\nDeletion Aborted!!")

else:
    print("Incorrect argument incountered aborting!!")
