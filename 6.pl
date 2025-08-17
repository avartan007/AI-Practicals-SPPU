:- dynamic known/2.

disease(flu) :- 
    symptom(fever), 
    symptom(cough), 
    symptom(sore_throat).

disease(cold) :- 
    symptom(runny_nose), 
    symptom(sneezing), 
    symptom(sore_throat).

disease(malaria) :- 
    symptom(fever), 
    symptom(chills), 
    symptom(sweating).

disease(typhoid) :- 
    symptom(fever), 
    symptom(headache), 
    symptom(stomach_pain), 
    symptom(fatigue).

symptom(S) :- 
    known(S, yes), !.

symptom(S) :- 
    known(S, no), !, fail.

symptom(S) :-
    ask(S).

ask(S) :-
    format("Do you have ~w? (yes/no)~n", [S]),
    read(Response),
    asserta(known(S, Response)),
    Response == yes.

start :-
    retractall(known(_, _)), % clear memory before new diagnosis
    disease(D),
    format("You might be suffering from ~w.~n", [D]), 
    !.

start :-
    write("Sorry, diagnosis is inconclusive or symptoms not recognized."), nl.
