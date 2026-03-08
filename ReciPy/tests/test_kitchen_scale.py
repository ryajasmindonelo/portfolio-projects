from src.kitchen_scale import Weight_Scale
from src.kitchen_scale import Volume_Scale


def test_convert_weight():
    scale = Weight_Scale()    
    amount = 1
    from_unit = 'kg'
    to_unit = 'g'
    
    expected_result = 1000
    actual_result = scale.convert_weight(amount, from_unit, to_unit)

    assert actual_result == expected_result

def test_convert_volume():
    scale = Volume_Scale()    
    amount = 2
    from_unit = 'c'
    to_unit = 'gal'
    
    expected_result = 0.125
    actual_result = scale.convert_volume(amount, from_unit, to_unit)

    assert actual_result == expected_result

