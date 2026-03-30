class fixNum:

    def __init__(self, a, b):
        a_int = int(a)
        b_int = int(b)


        # 1) b must be non-negative digit-part.
        if b_int < 0:
            b_int = -b_int

        # 2) If a is non-zero, b must be positive.
        #   (Assignment requires that b must be positive if a is non-zero.)
        if a_int != 0 and b_int == 0:
            b_int = 1

        self.a = a_int
        self.b = b_int

    def __str__(self):
        return str(self.a) + "." + str(self.b)
