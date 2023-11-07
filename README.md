# Interior Point Method 

Team Leader: Anastasia Pichugina

Members: Nikita Rashkin, Demyan Zverev, Fanis Zinnurov, Emil Davlityarov, Roman Pakhomov

To see differences between alpha = 0.5 and alpha = 0.9, values were rounded to 6 characters after the dot.

## Examples of tests:
### Test 1:
```
3 2 0 0 0
2 1 1 0 0
2 3 0 1 0
3 1 0 0 1
18 42 24
1e-6
```
Ans:
```
Initial point:
x1: 1.0
x2: 1.0
x3: 15.0
x4: 37.0
x5: 20.0

With alpha = 0.5:
Z: 33.000003
x1: 3.0
x2: 12.000001
x3: 0.0
x4: 1e-06
x5: 3.0

With alpha = 0.9:
Z: 32.999991
x1: 3.000002
x2: 11.999993
x3: 0.0
x4: 0.0
x5: 3.0
```
Ans of simplex:
```
-3    -2    0     0     0     0     
2     1     1     0     0     18    
2     3     0     1     0     42    
3     1     0     0     1     24    

0     -1    0     0     1     24    
0     1/3   1     0     -2/3  2     
0     7/3   0     1     -2/3  26    
1     1/3   0     0     1/3   8     

0     0     3     0     -1    30    
0     1     3     0     -2    6     
0     0     -7    1     4     12    
1     0     -1    0     1     6     

0     0     5/4   1/4   0     33    
0     1     -1/2  1/2   0     12    
0     0     -7/4  1/4   1     3     
1     0     3/4   -1/4  0     3     

x1 = 3     
x2 = 12    
Sol. = 33
```
### Test 2:
```
4 5 4 0 0 0
2 3 -6 1 0 0
4 2 -4 0 1 0
4 6 -8 0 0 1
240 200 160
1
```
Ans: 
```
The method is not applicable!
```
Ans of simplex:
```
-4    -5    -4    0     0     0     0     
2     3     -6    1     0     0     240   
4     2     -4    0     1     0     200   
4     6     -8    0     0     1     160   

-2/3  0     -32/3 0     0     5/6   400/3 
0     0     -2    1     0     -1/2  160   
8/3   0     -4/3  0     1     -1/3  440/3 
2/3   1     -4/3  0     0     1/6   80/3  

The method is not applicable!
```
### Test 3:
```
3 2 0 0 0
2 1 1 0 0
2 3 0 1 0
3 1 0 0 1
-18 42 24
1e-6
```
Ans:
```
The method is not applicable!
```
Ans of simplex:
```
The method is not applicable!
```
### Test 4:
```
9 10 16 0 0 0
18 15 12 1 0 0
6 4 8 0 1 0
5 3 3 0 0 1
360 192 180
1e-6
```
Ans:
```
Initial point:
x1: 1.0
x2: 1.0
x3: 1.0
x4: 315.0
x5: 174.0
x6: 169.0

With alpha = 0.5:
Z: 399.999946
x1: 0.0
x2: 7.999999
x3: 19.999997
x4: 8e-06
x5: 1e-06
x6: 96.000001

With alpha = 0.9:
Z: 400.000003
x1: 0.0
x2: 7.999999
x3: 20.000001
x4: 1e-06
x5: 0.0
x6: 95.999997
```
Ans of simplex:
```
-9    -10   -16   0     0     0     0     
18    15    12    1     0     0     360   
6     4     8     0     1     0     192   
5     3     3     0     0     1     180   

3     -2    0     0     2     0     384   
9     9     0     1     -3/2  0     72    
3/4   1/2   1     0     1/8   0     24    
11/4  3/2   0     0     -3/8  1     108   

5     0     0     2/9   5/3   0     400   
1     1     0     1/9   -1/6  0     8     
1/4   0     1     -1/18 5/24  0     20    
5/4   0     0     -1/6  -1/8  1     96    

x1 = 0     
x2 = 8     
x3 = 20    
Sol. = 400   
```
### Test 5:
```
1 2 0 0 0
-2 1 1 0 0
-1 2 0 1 0
1 0 0 0 1
2 7 3
1e-6
```
Ans:
```
Initial point:
x1: 1.0
x2: 1.0
x3: 3.0
x4: 6.0
x5: 2.0

With alpha = 0.5:
Z: 12.999999
x1: 3.0
x2: 5.0
x3: 3.0
x4: 0.0
x5: 0.0

With alpha = 0.9:
Z: 13.0
x1: 3.0
x2: 5.0
x3: 3.0
x4: 0.0
x5: 0.0
```
Ans of simplex:
```
-1    -2    0     0     0     0     
-2    1     1     0     0     2     
-1    2     0     1     0     7     
1     0     0     0     1     3     

-5    0     2     0     0     4     
-2    1     1     0     0     2     
3     0     -2    1     0     3     
1     0     0     0     1     3     

0     0     -4/3  5/3   0     9     
0     1     -1/3  2/3   0     4     
1     0     -2/3  1/3   0     1     
0     0     2/3   -1/3  1     2     

x1 = 1     
x2 = 4     
x3 = 0     
x4 = 0    
x5 = 2     
Sol. = 9     
```
