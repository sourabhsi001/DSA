def maxNumberOfBalloons(text):

        return min(
            text.count('b'),
            text.count('a'),
            text.count('l') // 2,
            text.count('o') // 2,
            text.count('n')
        )
        
text = "loonbalxballpoon"
print(maxNumberOfBalloons(text))
