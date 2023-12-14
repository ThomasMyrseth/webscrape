import time

from cryptoAPIpull import cryptoApiPull
from fileManager import fileManager
from dataAnalyzer import dataAnalyzer


class main:
    def __init__(self):
        self.cryptoApiPull = cryptoApiPull()
        self.fileManager = fileManager()
        self.dataAnalyzer = dataAnalyzer()
        #self.plot = self.dataAnalyzer.createPlot(currency=currency)

    def main(self, currensy, limit, pause, numOfIterations):
        try:
            self.dataAnalyzer.createPlot(currency=currensy)
            for i in range(numOfIterations):
                data = self.cryptoApiPull.apiRunner(limit=limit)
                #print("fetcted data")
                dataAsString = self.cryptoApiPull.dataToStringConverter(data)
                #print("converted data to string")

                self.fileManager.saveToTxt(dataAsString)
                #print("wrote data to file")

                self.dataAnalyzer.updatePrice(limit=limit, currensy=currensy, data=dataAsString)

                self.dataAnalyzer.updatePlot(currency=currensy, pause=pause) #SETTER SEG FAST HER
                print("updated plot")
                
        except Exception as e:
            print("En feil skjedde i loopen i main.main()")
            print(e)
            

m = main()

m.main(currensy="Bitcoin", limit=5, pause=1, numOfIterations=10) #DUNGERER KUN FOR BTC

m.dataAnalyzer.showPlot()

exit()



# #TESTER FUNKER
# d = dataAnalyzer()
# c = cryptoApiPull()

# data = c.apiRunner(limit=5)
# data = c.dataToStringConverter(data)

# d.updatePrice(limit=5, data=data, currensy="Bitcoin")
# d.updatePrice(limit=5, data=data, currensy="Bitcoin") #Hvis updatePrice kjøres to ganger blir prisen satt til None neste gan

# print(d.times)
# print(d.prices)