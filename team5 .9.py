####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'No snitches' # Only 10 chars displayed.
strategy_name = 'The Collusion'
strategy_description = 'Never snitch?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)==0:
        return 'c'
    elif my_history[-1] == 'c' and their[-1] == 'b':
        return 'b'
    else:
        return 'c'

