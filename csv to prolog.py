'''

Make class for concept 
each class has list of the other classes names it has connections to and with the strenghts 
run the simulation 
output in low and high


class Concept:
    def __init__(name,connections,others):
        self.name = name
        self.connections = connections
        self.others = others

grow = Concept('GRW',('BUG',0.03012592379347004))
water = Concept('WTR',('GRW':0.2963379685755752,"ROT":0.03012592379347004))
fertilizer = Concept('FRT',)
rot = Concept('ROT')
over_fertilizer = Concept('OFT')
bug = Concept('BUG')
posion = Concept('')

names = ['GRW','WTR','FRT','ROT','OFT','BUG','POS']





not_member(_, []) :- !.

not_member(X, [Head|Tail]) :-
     X \= Head,
    not_member(X, Tail).

check_io(A) :- 
    not_member(A,[0,1]),_
    write("Wrong input....."),
    nl,
    write("Do y your plant inside or outside (0 = inside, 1 = outside):"),
    read(A) ,
    check_io(A).

        
'''

name = 'orchid_fertilizer'
low = 25
mid = low*2
high = low*3

s = '''
% {name_var} assigning low medium and high
{name}({name_var},{name_var}_value) :- 
    {name_var} =< {low},
    {name_var}_value = "low".
   
{name}({name_var},{name_var}_value) :- 
    {name_var} > {mid},
    {name_var} =< {high},
    {name_var}_value = "medium".

{name}({name_var},{name_var}_value) :- 
    {name_var} =< {high},
    {name_var}_value = "high".

{name}({name_var},{name_var}_value) :- 
    {name_var} > {high},
    {name_var}_value = "too high".
'''.format(name=name,name_var=name.title(),low=low,mid=mid,high=high)

print(s)

