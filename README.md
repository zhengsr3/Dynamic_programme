# Dynamic_programme
Course Homework of operation research. The task of this homework is designing a general algorithm for Dynamic programme.
Algorithm Description:

	This repository contains three file(except this one).

	The first one, named 'dp.py', define a general class(Dynamic_Programme) for Dynamic program. In order to define this class, you need to provide three variable:a function act as providing state choice(take current stage and state as input and return the name of next stage and all possible next state). a function act as recurrence equation(take current state,current stage,nxt state,next stage as input and return the cost for transforming),a variable mark the ending stage.

	In order to use this class to make decision,youn need to initialize a dp  and   it take initial stage and initial state as input and return a list whose first element is decision past and second elements is max return.

	The second file called renew_equipment.py  provide a way to test this algorithm.In this file ,state choosing function is renew_equip_state_choice,recurrent equation is renew_equip_recur_equa and ending stage is 6th year.parameters such as cost,price of new machine, residual value are set in renew_equip_recur_equa. The outcome of this program is same with one of my classmate,which indicate that it is likely to be correct.

	If you want to test this algorithm by your self, you can change the setting in the function(renew_equip_recur_equa)or change the initial state.

	The third file called renew_equipment.py  provide a way to test this algorithm.In this file ,state choosing function is bag_filling_state_choice,recurrent equation is bag_filling_recur_equa and ending stage is 4th bag.parameters such as value ,weight are set in renew_equip_recur_equa. The outcome of this program seems correct.

	If you want to test this algorithm by your self, you can change the setting in the function(bag_filling_recur_equa)or change the initial state.
