import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
iris=sns.load_dataset('iris')
print(iris.info())
species_count=iris["species"].value_counts()


plt.figure()
plt.bar(species_count.index,species_count.values)
plt.title("Species Count (Matplotlib)")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()
#seabron

plt.figure()
sns.countplot(x="species",data=iris)
plt.title("Species Count (Seaborn)")
plt.show()

#matplotlib

plt.figure()
plt.hist(iris["sepal_length"],bins=10)
plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()
#seabron

plt.figure()
sns.histplot(iris["sepal_length"],bins=10,kde=True)
plt.title("Sepal Length Distribution")
plt.show()

mean_sepal=iris.groupby("species")["sepal_length"].mean()
plt.figure()
plt.plot(mean_sepal.index,mean_sepal.values,marker="o")
plt.title("Mean SepalLength by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length")
plt.show()
#histogram
plt.figure()
sns.histplot(iris["sepal_length"],bins=10,kde=True)
plt.title("Speal Length Distribution")
plt.show()

#line diagram
mean_sepal=iris.groupby("species")["sepal_length"].mean()
plt.figure()
plt.plot(mean_sepal.index,mean_sepal.values,marker="o")
plt.title("Mean Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length")
plt.show()
#seaborn
plt.figure()
sns.lineplot(x="species",y="sepal_length",data=iris,estimator="mean")
plt.title("Mean Sepal Length by Species ")
plt.show()

# #scatter plot
# #matplotlib
# plt.figure()
# plt.scatter(iris["sepal_length"],iris["petal_length"])
# plt.title("Sepal Length vs Petal Length")
# plt.xlabel("Sepal Length")
# plt.ylabel("Petal Length")
# plt.show()
# #seaborn
# plt.figure()
# sns.scatterplot(x="sepal_length",y="petal_length",hue="species",data=iris)
# plt.title("Sepal Length vs Petal Length")
# plt.show()