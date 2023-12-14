import matplotlib.pyplot as plt
import json

from datetime import datetime

from fileManager import fileManager

class dataAnalyzer:

    def __init__(self):
        self.f = fileManager()
        #self.data = json.loads(self.f.readAllfromTxt())

        self.times=[]
        self.prices={}
        self.fig = None
        self.ax = None

        
    def updatePrice(self, currensy, limit, data):
        data_dict = json.loads(data)

        t = data_dict["status"]["timestamp"]
        t = t[:-5]
        timestamp_datetime = datetime.fromisoformat(t)
        time = timestamp_datetime.strftime("%H:%M:%S")

        currencyInfo = data_dict["data"]
        currentPrice = None
        for i in range(int(limit)):
            if (currencyInfo[i]["name"] == currensy):
                currentPrice = currencyInfo[i]["quote"]["USD"]["price"]
                break
            else:
                i+=1
        
        if (currentPrice is None):
            e = priceIsNoneException(message=f"Prisen til {currensy} i dataAnalyzer.updatePrice() er None")
            raise e
        
        self.times.append(time)
        if (currensy in self.prices.keys()):
            prices = self.prices[currensy]
            prices.append(currentPrice)
            self.prices[currensy] = prices
        else:
            self.prices[currensy] = [currentPrice]
        


    def createPlot(self, currency):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel("time")
        self.ax.set_ylabel("price")
        self.ax.set_title(currency)
        self.ax.grid(True)



    def updatePlot(self, currency, pause):
        # now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        # self.times.append(current_time)
        # self.prices[currency].append(price)

        self.ax.clear() #fjerner tidligere plot
        self.ax.plot(self.times, self.prices[currency], label=currency)
        self.ax.legend()
        plt.pause(pause)

    def showPlot(self):
        plt.show()


class priceIsNoneException(Exception):
    def __init__(self, message):
        super().__init__(message)

