#This code returns some mad libs text based on the user input
#Is the code always returnin the correct input?
#What do you think I did to write this code that I shouldn't have done?

def change_name(adjective)
    if adjective == 'red':
        return "The quick brown fox jumps over the red dog"
    elif adjective == 'lazy':
        return "The quick brown fox jumps over the lazy dog"
    elif adjective == 'energetic':
        return "The quick brown fox jumps over the energetic dog"
    elif adjective == 'happy':
        return "The quick brown fox jumps over the happy dog"
    elif adjective == 'sad':
        return "The quick brown fox jumps over the happy dog"
    else:
        return "No case for that adjective found!"
    
