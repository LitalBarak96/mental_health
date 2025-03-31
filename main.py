import config
print(config.path_dataset)
#print("Path to dataset files:", path)

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='treatment', bins=30)
plt.title('התפלגות גיל לפי טיפול בבריאות הנפש')
plt.xlabel('גיל')
plt.ylabel('כמות אנשים')
plt.tight_layout()
plt.show()
