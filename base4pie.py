from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.2,0]

plt.pie(slices,labels=labels ,
        explode=explode , 
        shadow=True,
        autopct="%1.1f%%",
        wedgeprops={"edgecolor":"black"})

plt.show()