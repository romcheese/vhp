
def MassVote(N, Votes):
    all = sum(Votes)
    percents = []

    for i in range(len(Votes)): # создаем массив процентов
        percent = round(Votes[i]/all*100, 3)
        if percent > 50:
            return f'majority winner {i+1}'
        percents.append(percent)

    biggest = max(percents)

    for i in range(len(percents)):
        if percents[i] == biggest:
            prev_winner_i = i
            break

    for i in range(len(percents)):
        if percents[i] == biggest and i != prev_winner_i:
            return 'no winner'

    return f'minority winner {prev_winner_i+1}'
