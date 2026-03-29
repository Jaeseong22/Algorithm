def solution(genres, plays):
    total = {}
    songs = {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in total:
            total[genre] = 0
            songs[genre] = []
        
        total[genre] += play
        songs[genre].append((play, i))
    
    sorted_genres = sorted(total.keys(), key = lambda x : total[x], reverse=True)
    
    answer = []
    
    for genre in sorted_genres:
        sorted_songs = sorted(songs[genre], key = lambda x : (-x[0], x[1]))

        for song in sorted_songs[:2]:
            answer.append(song[1])
        
    return answer
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))