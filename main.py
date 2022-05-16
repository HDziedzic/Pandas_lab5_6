import pandas as pd
import re

# s = pd.Series([1, 3, 5, np.nan, 6, 4])
# ss = pd.Series([16, 33, 22], index=['Adam', 'Ala', 'Leszek'])
# print(s)
# print(ss)

# daty = pd.date_range('20220322', periods=5)
# print(daty)
# df = pd.DataFrame(np.random.randn(5, 5), index=daty, columns=list('ABCDE'))
# print(df)

# Zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# Zadanie 2

print(df.groupby(['Rok']).count()['Imie'])
print(df.loc[df['Imie'].str.contains('hubert', flags=re.I, regex=True)])
print('\n\nLiczba wszystkich urodzonych dzieci:', df.Liczba.sum())
print('\n\nDzieci urodzone w latach 2000-2005:\n', df.loc[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)])
print('\n\nsuma urodzonych chłopców :', df[(df["Plec"] == 'M')].Liczba.sum())
print('suma urodzonych dziewczynek :', df[(df["Plec"] == 'K')].Liczba.sum(), '\n\n')
df_k = df.loc[df['Plec'].str.contains('K')].groupby(['Rok']).head(2)
df_M = df.loc[df['Plec'].str.contains('M')].groupby(['Rok']).head(2)
# df_k.to_csv("popularne_imiona_K.csv", index=False)
# df_M.to_excel("popularne_imiona_M.xlsx", index=False)
print('\n\n2 najbardziej popularne imiona dziewczynek w danym roku\n:', df_k)
print('2 najbardziej popularne imiona chłopców w danym roku\n:', df_M, '\n\n')
print('\n\nnajpopularniejsze imię chłopca w całym danym okresie\n',
      df.loc[df['Plec'].str.contains('M')].sort_values(by='Liczba', ascending=False).head(1))
print('najpopularniejsze imię dziewczynki w całym danym okresie\n',
      df.loc[df['Plec'].str.contains('K')].sort_values(by='Liczba', ascending=False).head(1), '\n\n')

# Zadanie 3
df_zam = pd.read_csv('zamowienia.csv', sep=';', decimal='.')
df_zam_u = df_zam.drop_duplicates(subset=['Sprzedawca'])
for index, row in df_zam_u.iterrows():
    print(index, row['Sprzedawca'])

df_zam_max = df_zam.sort_values(by='Utarg', ascending=False).head(5)
print('\n\n', df_zam_max)

df_zam_gr = df_zam
df_zam_gr['One'] = 1
print('\n\n', df_zam_gr.groupby(['Sprzedawca']).sum()['One'])
print('\n\n', df_zam_gr.groupby(['Kraj']).sum()['One'])

df_zam_05 = df_zam_gr[(df_zam_gr['Kraj'] == 'Polska')].loc[df_zam['Data zamowienia'].str.contains('2005', regex=True)]
print('\n\nLiczba zamówień w 2005 dla sprzedawców z Polski: ', df_zam_05.One.sum())

df_zam_04 = df_zam_gr.loc[df_zam['Data zamowienia'].str.contains('2004', regex=True)].Utarg.mean()
print('\n\nŚrednia kwota zamówienia w 2004: ', df_zam_04)

df_04 = df_zam.loc[df_zam['Data zamowienia'].str.contains('2004')]
df_05 = df_zam.loc[df_zam['Data zamowienia'].str.contains('2005')]

print(df_05)
df_04.to_csv('Zamowienia_2004.csv')
df_05.to_csv('Zamowienia_2005.csv')
