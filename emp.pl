% Employee Performance Evaluation Expert System

:- dynamic known/2.

evaluate(excellent) :-
    attendance(good),
    task_completion(high),
    meets_deadlines(yes),
    teamwork(good).

evaluate(average) :-
    attendance(average),
    task_completion(medium),
    meets_deadlines(yes),
    teamwork(average).

evaluate(poor) :- attendance(poor).
evaluate(poor) :- task_completion(low).
evaluate(poor) :- meets_deadlines(no).
evaluate(poor) :- teamwork(poor).

% Asking questions
attendance(Value) :- ask(attendance, Value).
task_completion(Value) :- ask(task_completion, Value).
meets_deadlines(Value) :- ask(meets_deadlines, Value).
teamwork(Value) :- ask(teamwork, Value).

% Ask logic with memory
ask(Question, Value) :-
    known(Question, Value). % already known

ask(Question, Value) :-
    \+ known(Question, _),
    format('What is the ~w? ', [Question]),
    read(UserInput),
    asserta(known(Question, UserInput)),
    UserInput = Value.

% Start rule
start :-
    evaluate(Result),
    format('~nEmployee performance is: ~w~n', [Result]), nl.

start :-
    write('~nSorry, performance evaluation is inconclusive or inputs not recognized.'), nl.

% To clear known facts
clear :- retract(known(_, _)), fail.
clear.
