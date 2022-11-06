# Подсчет количества слогов
def how_many_syllables(example):
    count = 0
    for vowel in 'аеиоуюя':
        count += text.count(vowel)
    return count

