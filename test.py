import islpy as isl

s.apply(sch1.reverse()).apply(k).intersect(r).is_empty()
True
k = isl.Map("{S0[i, j] -> S0[i' = 1 + i, j' = j]}") // dep
r = s.apply(sch1.reverse()) // result
s = isl.Set("[n]->{S0[i,j]:i=n}")
sch = isl.Map("{ S0[i, j] -> S0[i + j, j] }") schezdule

r = isl.Set("[n]->{S0[i,j]:i=n}").apply(isl.Map("{ S0[i, j] -> S0[i + j, j] }").reverse())

>>>r.apply(isl.Map("{S0[i, j] -> S0[i' = 1 + i, j' = j]}"))


s.apply(sch.reverse()).apply(dep).apply(sch).lex_ge_set(s).is_empty()



solve and rank before/after :



isl.Map.lex_lt(s.get_space()).intersect(isl.Map("{S0[i,j]->S0[i-1,j+10]}")).is_empty()




{ S0[t5, t6, t7] -> S0[0, 0, i = t5, 0, j = t6, 0, k = t7, 0] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }
{ S0[t5, t6, t7] -> S0[t14 = 0, t15 = 0, i0 = t5 - t6, t17 = 0, j0 = t6, t19 = 0, k = t7, t21 = 0] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }
{ S0[t5, t6, t7] -> S0[t14 = 0, t15 = 0, i0 = t5 + t6, t17 = 0, j0 = t6, t19 = 0, k = t7, t21 = 0] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }
{ S0[t5, t6, t7] -> S0[t14 = 0, t15 = 0, i0 = 2t5 + t6, t17 = 0, j0 = t5 + t6, t19 = 0, k = t7, t21 = 0] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }
{ S0[t5, t6, t7] -> S0[t14 = 0, t15 = 0, i0 = t6, t17 = 0, j0 = -t5 + t6, t19 = 0, k = t7, t21 = 0] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }



s1 = isl.Set("[n1,n2]->{S0[n1,n2,j]:n1>0 and n2>0}")
s2 = isl.Set("[n1,n2]->{S0[n1+1,n2,j]:n1>0 and n2>0}")
decalage = isl.Map("{S0[i,j,k]->S0[i,j+1,k]}")

#sch = isl.Map("{S0[i,j,k]->S0[i,j,k]}")
sch = isl.Map("{ S0[t5, t6, t7] -> S0[ i0 = 2t5 + t6, j0 = t5 + t6, k = t7] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }")
app1 = s1.apply(sch)
app2 = s2.apply(sch)
app1.union(app2).intersect(app1.intersect(app2).complement()).is_empty()


s1 = isl.Set("[n1,n2]->{S0[n1,n2,j]:n1>0 and n2>0}")
s2 = isl.Set("[n1,n2]->{S0[n1,n2+1,j]:n1>0 and n2>0}")
sch = isl.Map("{ S0[t5, t6, t7] -> S0[ i0 = 2t5 + t6, j0 = t5 + t6, k = t7] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }")
app1 = s1.apply(sch).apply(decalage)
app2 = s2.apply(sch.reverse())


#test range
sch = isl.Map("{ S0[i, j] -> S0[i + j, j] }")
s = isl.Set("[n]->{S0[i,j]:i=n+1}")
s.apply(sch.reverse())


s2 = isl.Set("[n]->{S0[i,j]:i=n}")
decalage = isl.Map("{S0[i,j]->S0[i+1,j]}")
s2.apply(sch.reverse()).apply(decalage.apply_range(sch.reverse())


#important
sch.apply_range(decalage.apply_range(sch.reverse()))

s1 = isl.Set("[n1,n2]->{S0[n1,j,n2]:n1>0 and n2>0}")
s2 = isl.Set("[n1,n2]->{S0[n1+1,j,n2]:n1>0 and n2>0}")
decalage = isl.Map("{S0[i,j,k]->S0[i+1,j,k]}")
sch = isl.Map("{ S0[t5, t6, t7] -> S0[ i0 = 2t5 + t6, j0 = t5 + t6, k = t7] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }")
decalage_in_domain = sch.apply_range(decalage.apply_range(sch.reverse()))

app1 = s1.apply(sch.reverse()).apply(decalage_in_domain)
app2 = s2.apply(sch.reverse())

#make empty
s1 = isl.Set("[n1,n2]->{S0[n1,n2,j]:n1>0 and n2>0}")
s2 = isl.Set("[n1,n2]->{S0[n1,n2+1,j]:n1>0 and n2>0}")
decalage = isl.Map("{S0[i,j,k]->S0[i+1,j,k]}")
sch = isl.Map("{ S0[t5, t6, t7] -> S0[ i0 = t5 + t6, j0 =  t6, k = t7] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }")
decalage_in_domain = sch.apply_range(decalage.apply_range(sch.reverse()))

app1 = s1.apply(sch.reverse()).apply(decalage_in_domain)
app2 = s2.apply(sch.reverse())
app2.complement.intersect(app1)


#tired direct lex approch try second var unrolling test
sch = isl.Map("{ S0[t5, t6, t7] -> S0[ i0 = t5 + t6, j0 =  t6, k = t7] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }")
s1 = isl.Set("[n1,n2]->{S0[n1,n2,j]}")
s2 = isl.Set("[n1,n2]->{S0[n1,n2+1,j]}")

#2dim test
s1 = isl.Set("[n1]->{S0[n1,j]}")
s2 = isl.Set("[n1]->{S0[n1+1,j]}")
sch = isl.Map("{S0[i,j]->S0[i,j]}")
app1 = s1.apply(sch.reverse())
app2= s2.apply(sch.reverse())
app1.lex_lt_set(app2).is_empty()
app1.lex_gt_set(app2).is_empty()

#str approch
#calculate sch_raw.reverse()
#find my var within the set & liberate + fixe all / all_before in Set s
#application . polyhedral_hull
#for each and "stmt" if inequality
# count[used_var]++
#correct if count[*]<2




#testing dep calculation 
{ C_init[t1, t2, t3] -> C_init[0, 0, i = t1, 0, j = t2, 0, k = t3, 0] : 0 <= t1 <= 99 and 0 <= t2 <= 99 and 0 <= t3 <= 9 }
{ S0[t5, t6, t7] -> S0[0, 10, i = t5, 0, j = t6, 0, k = t7, 0] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 }
{ S1[t9, t10, t11] -> S1[0, 20, i = t9, 0, j = t10, 0, k = t11, 0] : 0 <= t9 <= 99 and 0 <= t10 <= 99 and 0 <= t11 <= 9 }

{ C_init[i, j, k] -> b_A2[j' = j, k' = k];
 S0[i, j, k] -> b_A2[ j' = j, k' = k]; 
S0[i, j, k] -> b_A2[ j' = j, k' = -1 + k];
 S0[i, j, k] -> b_output[ j' = 1 + j, k' = k];
 S0[i, j, k] -> b_output[ j' = -1 + j, k' = k] }




{ S0[i, j, k] -> b_A2[j, k] }
{ C_init[i, j, k] -> b_A[j, k] }
{ S1[i, j, k] -> b_output[j, k] }


{ S0[i, j, k] -> S0[i,j+1, k] }
{ C_init[i, j, k] -> b_A[j, k] }
{ S1[i, j, k] -> b_output[j, k] }


{ C_init[t1, t2, t3] -> [0, 0, i = t1, 0, j = t2, 0, k = t3, 0] : 0 <= t1 <= 99 and 0 <= t2 <= 99 and 0 <= t3 <= 9 ; S0[t5, t6, t7] -> [0, 10, i = t5, 0, j = t6, 0, k = t7, 0] : 0 <= t5 <= 99 and 0 <= t6 <= 99 and 0 <= t7 <= 9 ; S1[t9, t10, t11] -> [0, 20, i = t9, 0, j = t10, 0, k = t11, 0] : 0 <= t9 <= 99 and 0 <= t10 <= 99 and 0 <= t11 <= 9 }


{ S0[i, j, k] -> b_A2[j, k] ; C_init[i, j, k] -> b_A[j, k] ; S1[i, j, k] -> b_output[j, k] }


dep = isl.Map("{S0[i,j]->S0[i+1,j-1]}")

sched = isl.Map("{S0[i,j]->[i+j,j]}")

d = dep.apply_range(sched).apply_domain(sched)
d
d.equate(isl.dim_type.in_,0,isl.dim_type.out,0)






{ must_dependence: "{
S0[t5 = 99, t6, t7] -> [S1[t9, t10 = t6, t11 = -1 + t7] -> b_output[t6, -1 + t7]] : 0 <= t6 <= 99 and 0 < t7 <= 9 and 0 <= t9 <= 99; 
S0[t5 = 99, t6, t7 = 9] -> [S1[t9, t10 = t6, t11 = 9] -> b_output[t6, 9]] : 0 <= t6 <= 99 and 0 <= t9 <= 99;
C_init[t1 = 99, t2 = 0, t3] -> [S0[t5 = 0, t6 = 0, t7 = t3] -> b_A2[0, t3]] : 0 <= t3 <= 9; 
S0[t5, t6, t7] -> [S0[t5' = t5, t6' = 1 + t6, t7' = t7] -> b_A2[1 + t6, t7]] : 0 <= t5 <= 99 and 0 <= t6 <= 98 and 0 <= t7 <= 9; 
S0[t5, t6 = 1, t7] -> [S0[t5' = 1 + t5, t6' = 0, t7' = t7] -> b_A2[0, t7]] : 0 <= t5 <= 98 and 0 <= t7 <= 9 }",


 may_dependence: "{

 S0[t5 = 99, t6, t7] -> [S1[t9, t10 = t6, t11 = -1 + t7] -> b_output[t6, -1 + t7]] : 0 <= t6 <= 99 and 0 < t7 <= 9 and 0 <= t9 <= 99;
 S0[t5 = 99, t6, t7 = 9] -> [S1[t9, t10 = t6, t11 = 9] -> b_output[t6, 9]] : 0 <= t6 <= 99 and 0 <= t9 <= 99;
 S0[t5, t6, t7] -> [S0[t5' = t5, t6' = 1 + t6, t7' = t7] -> b_A2[1 + t6, t7]] : 0 <= t5 <= 99 and 0 <= t6 <= 98 and 0 <= t7 <= 9;
 S0[t5, t6 = 1, t7] -> [S0[t5' = 1 + t5, t6' = 0, t7' = t7] -> b_A2[0, t7]] : 0 <= t5 <= 98 and 0 <= t7 <= 9;
 C_init[t1 = 99, t2 = 0, t3] -> [S0[t5 = 0, t6 = 0, t7 = t3] -> b_A2[0, t3]] : 0 <= t3 <= 9 }",

 must_no_source: "{ C_init[t1, t2, t3] -> b_A[t2, t3] : 0 <= t1 <= 99 and 0 <= t2 <= 99 and 0 <= t3 <= 9 }",

 may_no_source: "{ C_init[t1, t2, t3] -> b_A[t2, t3] : 0 <= t1 <= 99 and 0 <= t2 <= 99 and 0 <= t3 <= 9 }






