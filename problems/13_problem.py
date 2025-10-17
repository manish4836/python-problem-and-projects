teams = [('A', 15, 3), ('B', 22, 1), ('C', 18, 5)]
sorted_teams = sorted(teams, key= lambda x:x[1], reverse=True)

print(sorted_teams)