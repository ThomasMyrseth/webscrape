from datetime import datetime

separation_mark = "===================="


class fileManager:
    def __init__(self):
        None

    def saveToTxt(self, text):
        try:
            with open("gptSummary.txt", "a") as f:
                currentTime = datetime.now()
                currentTimeFormatted = currentTime.strftime("%Y-%m-%d %H:%M:%S")
                f.write("time when written: " + currentTimeFormatted + "\n")
                f.write(text + "\n")
                f.write(separation_mark + "\n")
            print("wrote to gptSummary.txt succesfully")
        except Exception as e:
            print("an IO error occured:")
            print(e)
            return e


    def readMostRecentFromTxt(self):
        summary = ""
        currentLine = ""
        try:
            with open("gptSummary.txt", "r") as f:
                while (currentLine != separation_mark + "\n"):
                    currentLine = f.readline()
                    summary += currentLine + "\n"
            return summary
        except Exception as e:
            print("En IO-feil har skjedd")
            print(e)
            return e


    def readAllfromTxt(self):
        summaries = ""
        currentLine = "_"
        try:
            with open("gptSummary.txt", "r") as f:
                while (currentLine != ""):
                    currentLine = f.readline()
                    if (currentLine != separation_mark):
                        summaries += currentLine
                    else:
                        summaries += "\n \n"
            return summaries
        except Exception as e:
            print("En IO-feil har skjedd")
            print(e)
            return e
