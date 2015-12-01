import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# remove rows with null values
loansData.dropna(inplace=True)

loansData.boxplot(column='Amount.Requested', return_type='axes')

plt.show()

loansData.hist(column='Amount.Requested')
plt.show()


plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm",
        plot=plt)
plt.show()

print "The mean Amount Requested is " + str(loansData['Amount.Requested'].mean())
print "The mean Amount Funded is " + str(loansData['Amount.Funded.By.Investors'].mean())
print "Is it fair to say that the amount requested is typically funded?"

print "It would appear that the distribtions of the requested amount and funded amount are similar. Based on the histogram, qq-plot, and box-plot"
