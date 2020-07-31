import json

##Relative file paths of inpput and output files.
inputPath = "/home/alex/UnlockAcademy/Python/input.json"
outputPath = "/home/alex/UnlockAcademy/Python/output.txt" 

### with open() as something is basically same as using in c#
with open(inputPath, "r") as input:
    obj = json.load(input)
    with open(outputPath, "w") as output:
        output.write(obj["name"] + "'s Hobbies:\n")
        for hobby in obj["hobbies"]:
            output.write(hobby + "\n")

print("Written to Json file")
