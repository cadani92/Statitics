import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

average_group1 = 40
average_group2 = 45

standard_deviation = 5.6

samples_group1 = 40
samples_group2 = 35

data_group1 = np.random.randn(samples_group1) * standard_deviation + average_group1
data_group2 = np.random.randn(samples_group2) * standard_deviation + average_group2

ns = [samples_group1, samples_group2]

datalims = [np.min(np.hstack((data_group1, data_group2))), np.max(np.hstack((data_group1, data_group2)))]

print(datalims)

fig,ax = plt.subplots(1,2,figsize=(6,4))

ax[0].violinplot(data_group1)
ax[0].plot(1+np.random.randn(samples_group1)/10,data_group1,'ko')
ax[0].set_ylim(datalims)
ax[0].axis('off')

ax[1].violinplot(data_group2)
ax[1].plot(1+np.random.randn(samples_group2)/10,data_group2,'ko')
ax[1].set_ylim(datalims)
ax[1].axis('off')


# 2-group t-test
t,p = stats.ttest_ind(data_group1,data_group2)

# print the information to the title
sigtxt = ('',' NOT')
plt.title('The two groups are%s significantly different! t(%g)=%g, p=%g'%(sigtxt[int(p>.05)],sum(ns)-2,np.round(t,2),np.round(p,3)))

print("Graphics: ")

plt.show()
