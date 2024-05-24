import calc

def test_addition():
    assert calc.addition(3,2) == 5
    assert calc.addition(5,7) == 12
    assert calc.addition(12,19) == 31
    assert calc.addition(45,91) == 136
    assert calc.addition(200,250) == 450

def test_subtraction():
    assert calc.subtraction(400,200) == 200
    assert calc.subtraction(1000,500) == 500
    assert calc.subtraction(10000,9000) == 1000
    assert calc.subtraction(450,1) == 449
    assert calc.subtraction(10,9) == 1

def test_multiplication():
    assert calc.multiplication(1,1) == 1
    assert calc.multiplication(2,2) == 4
    assert calc.multiplication(3,3) == 9
    assert calc.multiplication(100,100) == 10000
    assert calc.multiplication(10000,10000) == 100000000

def test_division():
    assert calc.division(100000000,10000) == 10000
    assert calc.division(10000, 100) == 100
    assert calc.division(9,3) == 3
    assert calc.division(4,2) == 2
    assert calc.division(1,1) == 1