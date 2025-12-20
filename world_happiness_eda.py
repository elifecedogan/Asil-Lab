
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings

warnings.filterwarnings("ignore")

df = pd.read_csv('World-happiness-report-2024.csv')

df['Country name'] = df['Country name'].str.strip().replace({
    'Turkiye': 'Turkey', 'United States': 'USA', 'Palestinian Territories': 'Palestine',
    'Hong Kong S.A.R. of China': 'Hong Kong', 'Taiwan Province of China': 'Taiwan',
    'Congo (Kinshasa)': 'DR Congo', 'Czechia': 'Czech Republic', 'North Macedonia': 'Macedonia',
    'Ivory Coast': "Côte d'Ivoire",
})

numeric_df = df.select_dtypes(include=[np.number])

fig = px.choropleth(df, locations="Country name", locationmode='country names', color="Ladder score",
                    hover_name="Country name", color_continuous_scale='RdYlGn', title="Dünya Mutluluk Haritası",
                    labels={'Ladder score': 'Mutluluk Puanı', 'Country name': 'Ülke'})
fig.show()


plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Ladder score', kde=True, bins=20, color='seagreen')
plt.title('Mutluluk Puanı Dağılımı (0-10 Skalası)')
plt.xlabel('Mutluluk Puanı')
plt.ylabel('Ülke Sayısı')
plt.xlim(0, 10)
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='RdYlGn', fmt=".2f")
plt.title('İlişki Tablosu'); plt.show()

top10 = df.nlargest(10, 'Ladder score')
bot10 = df.nsmallest(10, 'Ladder score')

fig, ax = plt.subplots(1, 2, figsize=(18, 6))
sns.barplot(x='Ladder score', y='Country name', data=top10, palette='Greens_r', ax=ax[0], hue='Country name', legend=False)
ax[0].set_title('En Mutlu 10 Ülke'); ax[0].set_ylabel(''); ax[0].set_xlabel('Mutluluk Puanı')
ax[0].set_xlim(0, 8)

sns.barplot(x='Ladder score', y='Country name', data=bot10, palette='Reds_r', ax=ax[1], hue='Country name', legend=False)
ax[1].set_title('En Mutsuz 10 Ülke'); ax[1].set_ylabel(''); ax[1].set_xlabel('Mutluluk Puanı')
ax[1].set_xlim(0, 8)
plt.tight_layout(); plt.show()

plt.figure(figsize=(15, 8))
sns.boxplot(x='Ladder score', y='Regional indicator', data=df, palette='Spectral', hue='Regional indicator', legend=False)
plt.title('Bölgelerin Mutluluk Dağılımı')
plt.xlabel('Mutluluk Puanı')
plt.ylabel('Bölge')
plt.xticks(rotation=45)
plt.xlim(0, 10)
plt.show()


px.scatter(df, x="Log GDP per capita", y="Ladder score", color="Ladder score", size="Ladder score",
           hover_name="Country name", color_continuous_scale='RdYlGn', title="Gelir ve Mutluluk",
           labels={'Ladder score': 'Mutluluk Puanı', 'Log GDP per capita': 'Gelir', 'Country name': 'Ülke'}).show()


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Freedom to make life choices', y='Ladder score', hue='Ladder score', palette='RdYlGn', s=100, legend=False)
plt.title('Özgürlük ve Mutluluk')
plt.xlabel('Özgürlük Puanı')
plt.ylabel('Mutluluk Puanı')
plt.show()


plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Social support', y='Ladder score', scatter_kws={'alpha':0.5, 'color':'green'}, line_kws={'color':'red'})
plt.title('Sosyal Destek Etkisi')
plt.xlabel('Sosyal Destek Puanı')
plt.ylabel('Mutluluk Puanı')
plt.show()