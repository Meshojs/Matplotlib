from matplotlib import pyplot as plt 

plt.style.use("dark_background")

mon_x = [
    'January', 'February', 'March', 'April', 'May', 'June']

prod_a = [500, 520, 480, 510, 530, 550]
prod_b = [300, 310, 290, 320, 330, 340]


print(plt.style.available)


plt.plot(mon_x , prod_a , label="Product A" , color="r" , linewidth=2  , linestyle=":")
plt.plot(mon_x , prod_b , label="Product B") 

plt.title("the sales of two products")
plt.grid(True)

plt.legend()

plt.xlabel("Months")
plt.ylabel("Sells")
plt.tight_layout()

plt.savefig("plot.png")
plt.show()
