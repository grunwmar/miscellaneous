import math


class UFloat:

    def __init__(self, int_part, point_position):
        exp_int_part = int(math.log10(int_part))
        exp_frac_part = int(math.log10(fraction_part))

        exponent = exp_frac_part + exp_int_part

        power_of_ten_int = pow(10, exp_int_part)
        power_of_ten_frac = pow(10, exp_frac_part)

        self._tuple = ((int_part, exp_int_part), (fraction_part, exp_frac_part), exponent)
        
        print(self._tuple)



uf = UFloat(23, 33434543)
print(uf)        