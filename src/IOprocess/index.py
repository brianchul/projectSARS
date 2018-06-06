import importlib

moduleName = ["adviseInput", "calculateQuantify", "clearScreen",
    "docx", "inputTitle", "keyboardInput", "printScoreData", "readFile", "writeToHTML"]
for name in moduleName:
    importlib.import_module(name + ".py")

