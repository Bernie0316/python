from pytest import approx
from water_flow import pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction,water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
import pytest


def test_water_column_height():
    height = water_column_height(0, 0)
    assert height == approx(0) 
    height = water_column_height(0, 10)
    assert height == approx(7.5) 
    height = water_column_height(25, 0)
    assert height == approx(25)   
    height = water_column_height(48.3, 12.8)
    assert height == approx(57.9) 
    
def test_pressure_gain_from_water_height():
    pressure = pressure_gain_from_water_height(0)
    assert pressure == approx(0, abs=0.001)
    pressure = pressure_gain_from_water_height(30.2)
    assert pressure == approx(295.628, abs=0.001)
    pressure = pressure_gain_from_water_height(50)
    assert pressure == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    lost_presure = pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75)
    assert lost_presure == approx(0, abs=0.001)
    lost_presure = pressure_loss_from_pipe(0.048692, 200, 0, 1.75)
    assert lost_presure == approx(0, abs=0.001) 
    lost_presure = pressure_loss_from_pipe(0.048692, 200, 0.018, 0)
    assert lost_presure == approx(0, abs=0.001)    
    lost_presure = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75)
    assert lost_presure == approx(-113.008, abs=0.001)  
    lost_presure = pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65)
    assert lost_presure == approx(-100.462, abs=0.001)   
    lost_presure = pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65)
    assert lost_presure == approx(-61.576, abs=0.001)  
    lost_presure = pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65)
    assert lost_presure == approx(-110.884, abs=0.001)    

def test_pressure_loss_from_fittings():
    test = pressure_loss_from_fittings(0, 3)
    assert test == approx(0, abs=0.001)
    test = pressure_loss_from_fittings(1.65, 0)
    assert test == approx(0, abs=0.001)
    test = pressure_loss_from_fittings(1.65, 2)
    assert test == approx(-0.109, abs=0.001)
    test = pressure_loss_from_fittings(1.75, 2)
    assert test == approx(-0.122, abs=0.001)
    test = pressure_loss_from_fittings(1.75, 5)
    assert test == approx(-0.306, abs=0.001)

def test_reynolds_number():
    test = reynolds_number(0.048692, 0)
    assert test == approx(0, abs=1)
    test = reynolds_number(0.048692, 1.65)
    assert test == approx(80069, abs=1)
    test = reynolds_number(0.048692, 1.75)
    assert test == approx(84922, abs=1)
    test = reynolds_number(0.28687, 1.65)
    assert test == approx(471729, abs=1)
    test = reynolds_number(0.28687, 1.75)
    assert test == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    test = pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692)
    assert test == approx(0, abs=0.001)
    test = pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    assert test == approx(-163.744, abs=0.001)
    test = pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)
    assert test == approx(-184.182, abs=0.001)
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])