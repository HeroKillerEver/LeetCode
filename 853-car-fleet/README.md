## Idea

we just sort the locations with respect to every car according to the place relative distance with respect to destination. And then we can calculate the relative time to the destination: `[t1, t2, t3, t4, t5, ...., tn]`. 

Then after sometime thinking, we can find out that if `tn < tm` for `m < n`, then `n` and `m` must follow the same fleet. So it means that the slowest car will hinder the fleet.  

So the idea is to loop over the whole array, every time we find `cur_time > prev_time`, there becomes a new fleet.  