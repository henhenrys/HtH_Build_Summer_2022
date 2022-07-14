import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

videogame_sales_data = pandas.read_csv("best_selling_games.csv")

print(videogame_sales_data)
