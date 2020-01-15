####
# Each team's file must define four tokens:
#     team_name: 'team 0'
#     strategy_name: 'You better not betray me'
#     strategy_description: 'Collude'
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 0' # Only 10 chars displayed.
strategy_name = 'You Better Not Betray Me'
strategy_description = 'Collude'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len (my_history)==0:
        return 'c'
    elif my_history[-1]== 'b' and their_history[-1] == 'b':
        return 'b'
    else:
        return 'c'