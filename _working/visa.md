%% Design for a chatbot platform
%% =============================

%% Purpose: to define what the language should be

%% Design: use the syntax, but not semantics, of Prolog
%% Additional rules to define language translations


%% Example: find a visa for the UK

%% % This type of definition shouldn't be needed - should be able to infer possible values

%% % `duration` is a variable with values that are lengths of time
%% variable(duration, length_of_time).

%% % `purpose` is a variable whose values can be one of `business`, `tourism` or `study`
%% variable(purpose, options([business, tourism, study])).


say("How long do you want to come to the UK for?", what(duration)).
say("What is the purpose of your visit?", what(purpose)).
say("Are you coming for business?", is(purpose(business))).
say("You can get a short term study visa", visa_type(short_term_study)).

hear("I'm coming to study.", purpose(study)).
hear("I want to come for five months.", duration(months(5))).


visa_type(short_term_study) :- less_than(duration, months(6)),
			       purpose(study).


