####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'P Waites Snitch Hunters' # Only 10 chars displayed.
strategy_name = 'Snitches Get Le Stitches'
strategy_description = 'Snitch and you end up inna ditch'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
if len(my_history)==0:
    return 'c'
    elif my_history[-1] == 'c' and their_history[-1] == 'c':
        return 'c'
    else:
        return 'b'