import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
species_count=iris["species"].value_counts()

#Scatter
#Matplotlib
plt.figure()
plt.scatter(iris["sepal_length"],iris["petal_length"])
plt.title("Sepal Length vs Petal Length(matplotlin)")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()


#Seaborn
plt.figure()
sns.scatterplot(x="sepal_length",y="petal_length",hue="species",data=iris)
plt.title("Sepal Length Vs Petal Length(sns)")
plt.show()

#Pie Chart
#Matplotlib
plt.figure()
plt.pie(species_count,labels=species_count.index,autopct="%1.1f%%")
plt.title("Species Distribution")
plt.show()


#Heat Map
corr =iris.corr(numeric_only=True)
#Matplotlib
plt.figure()
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)),corr.columns,rotation=45)
plt.yticks(range(len(corr.columns)),corr.columns)
plt.table("Correlation Heat Map")
plt.show()

#Seaborn
plt.figure()
sns.heatmap(corr,annot=True)
plt.table("Correlation Heat Map")
plt.show()


#PairPlot
sns.pairplot(iris,hue="species")
plt.show()




#Box Plot
#Matplotlib
plt.figure()
iris.boxplot(column="sepal_length",by="species")
plt.title("Sepal Length by Species")
plt.suptitle("")
plt.show()

#Seaborn
plt.figure()
sns.boxplot(x="species",y="sepal_length",data=iris)
plt.title("Sepal Length by Species")
plt.show()