'''
helper.py by Mosklia

'''

import json
import sys # For command line args
import os

def main(args):
    if len(args) < 3:
        displayHelp()
        return
    originFile, outputFile = args[1], args[2]
    if not os.path.exists(originFile):
        print(f"Error: Original file {args[0]} not exist.")
    else:
        process(originFile, outputFile)

def process(originFile, outputFile):
    # print(f"originFile={originFile}", f"outputFile={outputFile}")
    oldStr, outputStr = {}, {}
    if os.path.exists(outputFile):
        with open(outputFile, "r") as old:
            oldStr = json.loads(old.read())
        os.rename(outputFile, outputFile + '.bak')
    with open(originFile, "r") as origin:
        originStr = json.loads(origin.read())
    print(originStr)
    for key, text in originStr.items():
        result = requireTranslation(key, text, oldStr.get(key))
        if result: outputStr[key] = result
    with open(outputFile, "w") as output:
        json.dump(outputStr, output, indent=4, ensure_ascii=False)

def requireTranslation(key, origin, old = None):
    if old:
        return input(
f'''--------------------
Translation key: {key}
Original text: {origin}
Old translated text: {old}
Enter new translation, or a blank to keep unchanged:
'''
        ) or old
    else:
        return input(
f'''--------------------
Translation key: {key}
Original text: {origin}
No old translated text found.
Enter new translation, or a blank to skip:
'''
        ) or None

def displayHelp():
    print(
'''Usage: python helper.py <origin> <output>
- origin: the original lang file to translate.
- output: the result lang file.'''
    )

if __name__ == "__main__":
    main(sys.argv)