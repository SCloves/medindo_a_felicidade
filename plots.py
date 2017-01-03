import matplotlib.pyplot as plt

def top_10_languages(df):

	tweets_by_lang = df['lang'].value_counts()

	fig, ax = plt.subplots()

	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Idiomas', fontsize=15)
	ax.set_ylabel('Numero de tweets' , fontsize=15)
	ax.set_title('Top 10', fontsize=15, fontweight='bold')
	tweets_by_lang[:10].plot(ax=ax, kind='bar', color='red')
	
	plt.show()


def top_10_countrys(df):

	tweets_by_country = df['country'].value_counts()

	fig, ax = plt.subplots()

	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Countrys', fontsize=15)
	ax.set_ylabel('Numero de tweets' , fontsize=15)
	ax.set_title('Top 10', fontsize=15, fontweight='bold')
	tweets_by_country[:10].plot(ax=ax, kind='bar', color='red')

	plt.show()
