from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

lyrics = """
[Verse 1]
It doesn't hurt me (Ye-yeah, yeah, yo)
Do you want to feel how it feels? (Ye-yeah, yeah, yo)
Do you want to know, know that it doesn't hurt me? (Ye-yeah, yeah, yo)
Do you want to hear about the deal that I'm making? (Ye-yeah, yeah, yo)

[Pre-Chorus]
You
It's you and me

[Chorus]
And if I only could
I'd make a deal with God
And I'd get him to swap our places
Be running up that road
Be running up that hill
Be running up that building
Say, if I only could, oh


[Verse 2]
You don't wanna hurt me (Ye-yeah, yeah, yo)
But see how deep the bullet lies (Ye-yeah, yeah, yo)
Unaware, I'm tearing you asunder (Ye-yeah, yeah, yo)
Oh, there is thunder in our hearts (Ye-yeah, yeah, yo)
Is there so much hate for the ones we love? (Ye-yeah, yeah, yo)
Oh, tell me, we both matter, don't we? (Ye-yeah, yeah, yo)

[Pre-Chorus]
You
It's you and me
It's you and me, won't be unhappy

[Chorus]
And if I only could
I'd make a deal with God
And I'd get him to swap our places
Be running up that road
Be running up that hill
Be running up that building (Ye-yo)
Say, if I only could, oh

[Pre-Chorus]
You (Ye-yeah, yeah, yo)
It's you and me
It's you and me, won't be unhappy (Ye-yeah, yeah, yo)
"""
sentences = sent_tokenize(text=lyrics)
print(sentences)

"""
['', '[Verse 1]', "It doesn't hurt me (Ye-yeah, yeah, yo)", 'Do you want to feel how it feels? (Ye-yeah, yeah, yo)', "Do you want to know, know that it doesn't hurt me? (Ye-yeah, yeah, yo)", "Do you want to hear about the deal that I'm making? (Ye-yeah, yeah, yo)", '', '[Pre-Chorus]', 'You', "It's you and me", '', '[Chorus]', 'And if I only could', "I'd make a deal with God", "And I'd get him to swap our places", 'Be running up that road', 'Be running up that hill', 'Be running up that building', 'Say, if I only could, oh', '', '', '[Verse 2]', "You don't wanna hurt me (Ye-yeah, yeah, yo)", 'But see how deep the bullet lies (Ye-yeah, yeah, yo)', "Unaware, I'm tearing you asunder (Ye-yeah, yeah, yo)", 'Oh, there is thunder in our hearts (Ye-yeah, yeah, yo)', 'Is there so much hate for the ones we love? (Ye-yeah, yeah, yo)', "Oh, tell me, we both matter, don't we? (Ye-yeah, yeah, yo)", '', '[Pre-Chorus]', 'You', "It's you and me", "It's you and me, won't be unhappy", '', '[Chorus]', 'And if I only could', "I'd make a deal with God", "And I'd get him to swap our places", 'Be running up that road', 'Be running up that hill', 'Be running up that building (Ye-yo)', 'Say, if I only could, oh', '', '[Pre-Chorus]', 'You (Ye-yeah, yeah, yo)', "It's you and me", "It's you and me, won't be unhappy (Ye-yeah, yeah, yo)", '']
"""

"""
['', '[Verse 1]', "It doesn't hurt me (Ye-yeah, yeah, yo)", 'Do you want to feel how it feels? (Ye-yeah, yeah, yo)', "Do you want to know, know that it doesn't hurt me? (Ye-yeah, yeah, yo)", "Do you want to hear about the deal that I'm making? (Ye-yeah, yeah, yo)", '', '[Pre-Chorus]', 'You', "It's you and me", '', '[Chorus]', 'And if I only could', "I'd make a deal with God", "And I'd get him to swap our places", 'Be running up that road', 'Be running up that hill', 'Be running up that building', 'Say, if I only could, oh', '', '', '[Verse 2]', "You don't wanna hurt me (Ye-yeah, yeah, yo)", 'But see how deep the bullet lies (Ye-yeah, yeah, yo)', "Unaware, I'm tearing you asunder (Ye-yeah, yeah, yo)", 'Oh, there is thunder in our hearts (Ye-yeah, yeah, yo)', 'Is there so much hate for the ones we love? (Ye-yeah, yeah, yo)', "Oh, tell me, we both matter, don't we? (Ye-yeah, yeah, yo)", '', '[Pre-Chorus]', 'You', "It's you and me", "It's you and me, won't be unhappy", '', '[Chorus]', 'And if I only could', "I'd make a deal with God", "And I'd get him to swap our places", 'Be running up that road', 'Be running up that hill', 'Be running up that building (Ye-yo)', 'Say, if I only could, oh', '', '[Pre-Chorus]', 'You (Ye-yeah, yeah, yo)', "It's you and me", "It's you and me, won't be unhappy (Ye-yeah, yeah, yo)", '']
[[], ['[', 'Verse', '1', ']'], ['It', 'does', "n't", 'hurt', 'me', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], ['Do', 'you', 'want', 'to', 'feel', 'how', 'it', 'feels', '?', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], ['Do', 'you', 'want', 'to', 'know', ',', 'know', 'that', 'it', 'does', "n't", 'hurt', 'me', '?', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], ['Do', 'you', 'want', 'to', 'hear', 'about', 'the', 'deal', 'that', 'I', "'m", 'making', '?', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], [], ['[', 'Pre-Chorus', ']'], ['You'], ['It', "'s", 'you', 'and', 'me'], [], ['[', 'Chorus', ']'], ['And', 'if', 'I', 'only', 'could'], ['I', "'d", 'make', 'a', 'deal', 'with', 'God'], ['And', 'I', "'d", 'get', 'him', 'to', 'swap', 'our', 'places'], ['Be', 'running', 'up', 'that', 'road'], ['Be', 'running', 'up', 'that', 'hill'], ['Be', 'running', 'up', 'that', 'building'], ['Say', ',', 'if', 'I', 'only', 'could', ',', 'oh'], [], [], ['[', 'Verse', '2', ']'], ['You', 'do', "n't", 'wan', 'na', 'hurt', 'me', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], ['But', 'see', 'how', 'deep', 'the', 'bullet', 'lies', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], ['Unaware', ',', 'I', "'m", 'tearing', 'you', 'asunder', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], ['Oh', ',', 'there', 'is', 'thunder', 'in', 'our', 'hearts', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], ['Is', 'there', 'so', 'much', 'hate', 'for', 'the', 'ones', 'we', 'love', '?', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], ['Oh', ',', 'tell', 'me', ',', 'we', 'both', 'matter', ',', 'do', "n't", 'we', '?', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], [], ['[', 'Pre-Chorus', ']'], ['You'], ['It', "'s", 'you', 'and', 'me'], ['It', "'s", 'you', 'and', 'me', ',', 'wo', "n't", 'be', 'unhappy'], [], ['[', 'Chorus', ']'], ['And', 'if', 'I', 'only', 'could'], ['I', "'d", 'make', 'a', 'deal', 'with', 'God'], ['And', 'I', "'d", 'get', 'him', 'to', 'swap', 'our', 'places'], ['Be', 'running', 'up', 'that', 'road'], ['Be', 'running', 'up', 'that', 'hill'], ['Be', 'running', 'up', 'that', 'building', '(', 'Ye-yo', ')'], ['Say', ',', 'if', 'I', 'only', 'could', ',', 'oh'], [], ['[', 'Pre-Chorus', ']'], ['You', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], ['It', "'s", 'you', 'and', 'me'], ['It', "'s", 'you', 'and', 'me', ',', 'wo', "n't", 'be', 'unhappy', '(', 'Ye-yeah', ',', 'yeah', ',', 'yo', ')'], []]
"""