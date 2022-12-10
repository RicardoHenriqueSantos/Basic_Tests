import matplotlib.pyplot as plt

fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 0.62, color='white')
lbls = ['Doar', 'Receber', 'Contas', 'Investir', 'Poupar', 'Curtir']

ax.pie([10, 5, 60, 10, 10, 5],
       labels=lbls,
       autopct='%1.1f%%',
       pctdistance=.82)
ax.add_artist(circle)
ax.set_title('Organização Finanças', fontsize=16)
plt.show()


