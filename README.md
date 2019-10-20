## Unit Testing Assignment

by Thun Thunkijjanikij


## Test Cases for unique

[![Build Status](https://travis-ci.com/Klan300/unittesting-Klan300.svg?branch=master)](https://travis-ci.com/Klan300/unittesting-Klan300) [![codecov](https://codecov.io/gh/Klan300/unittesting-Klan300/branch/master/graph/badge.svg)](https://codecov.io/gh/Klan300/unittesting-Klan300)

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| what other test case?  |  what result?       |


## Test Cases for Fraction

| Test case(init)         |  Expected Result    |
|------------------------|---------------------|
| with int type          |  instance Fraction class  |
| not integer            |   typeError  |

| Test case(str)         |  Expected Result    |
|------------------------|---------------------|
| positive integer       |  without minus symbol  |
| negative integer       |  with minus symbol  |
| divided by 1           |  wittout "/"        |
| determinator is 0      |  Nan                |

| Test case(add)         |  Expected Result    |
|------------------------|---------------------|
| add has answer with positve |  positive fraction |
| add has answer with negative  |  negative fraction |
| add with determinator is 0  |  Nan           |

| Test case(multiply)         |  Expected Result    |
|------------------------|---------------------|
| mul has answer with positve |  positive fraction |
| mul has answer with negative  |  negative fraction |
| mul with determinator is 0  |  Nan           |

| Test case(equal)         |  Expected Result    |
|------------------------|---------------------|
| same value not same number |  True |
| not same value not same number |  False |







