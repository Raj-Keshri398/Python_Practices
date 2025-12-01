import statistics

age = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

ages = sorted(age)
print("Mean = ", statistics.mean(ages)) # print average output : 21.09
print("Median = ", statistics.median(ages)) # print middle value output : 22
print("Mode = ", statistics.mode(ages)) # print repeated number output : 20
print("Standard Deviation = ", statistics.stdev(ages))


'''
How to calculate Standard Deviation


1. Total Sum Calculation

-------- 20 + 20 + 4 + 24 + 25 + 22 + 26 + 20 + 23 + 22 + 26 = 252

2. Total Count

-------- 11

3. Calculate Mean

-------- 252 / 11 = 22.9090909

4. find deviation of each element

-------- Deviation = (number - mean)
example: 
20 − 22.909 = –2.909
4 − 22.909 = –18.909
26 − 22.909 = +3.091

5. Squared deviations

Examples:

(–2.909)² = 8.46
(–18.909)² = 357.57
(3.091)² = 9.55

6. (n – 1) se divide karta hai
Variance = 412.18 / 11 − 1 ​= 412.18 / 10 ​= 41.218

6. Square root

Standard Deviation = √Variance
√41.218 = 6.42

'''
