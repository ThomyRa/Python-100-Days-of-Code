from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pidgey", "Squirtle", "Charmander"])
table.add_column("type", ["Flying", "Water", "Fire"])
table.align = "l"
print(table)
