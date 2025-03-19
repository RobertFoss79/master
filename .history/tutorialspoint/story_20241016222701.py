storyFormat = '''
Once upon a time, deep in an ancient jungle,
there lived a small {animal}. This {animal}
liked to eat {food}, but the jungle had
very little {food} to offer. One day, an
explorer found the {animal} and discovered
it liked {food}. The explorer took the
{animal} back to the {city}, where it could
eat as much {food} as it wanted. However,
the {animal} became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of {food}.

The End
'''

def tellStory():
    userPicks = dict()
    addpick('animal', userPicks)
    addpick('food', userPicks)
    addpick('city', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)

def addPick(cue, dictionary):
    prompt = 'Enter an example for ' + cue + ": "
    response = input(prompt)
    dictionary(cue) = response

tellstory()
input('Press Enter to end the program.')
