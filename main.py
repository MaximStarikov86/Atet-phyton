# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы

penguins = sb.load_dataset("penguins")
print(penguins.head())

sb.scatterplot(x="species", y="island",data=penguins)
sb.scatterplot(x="species", y="island",data=penguins, size=41)
sb.scatterplot(x="species", y="island", hue="body_mass_g", data=penguins)

# all_colums = ["species","island","bill_length_mm","bill_depth_mm",
#               "flipper_length_mm","body_mass_g","sex"]

# temp = sb.PairGrid(penguins[all_colums])
# temp.map(sb.scatterplot)

# pl.show()

# Создать новый столбец в таблице с
# пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

penguins.loc[penguins["bill_length_mm"] <= 35, "beak"] = "Small"
penguins.loc[(penguins["bill_length_mm"] > 35) & (penguins["bill_length_mm"] < 42), "beak"] = "Medium"
penguins.loc[penguins["bill_length_mm"] >= 42, "beak"] = "Big"

print(penguins.columns)

print(penguins.head(29))

# Изобразить гистограмму по flipper_length_mm
# с оттенком height_group. Сделать анализ


histplot(data=penguins, x ="flipper_length_mm", hue="body_mass_g")
pl.show()