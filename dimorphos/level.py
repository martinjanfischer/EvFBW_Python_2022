class Level:
    def __init__(self,
        asteroiden_anzahl = 6,
        asteroiden_groesse = 1,
        asteroiden_geschwindigkeit_minimum = 30,
        asteroiden_geschwindigkeit_maximum = 100,
        asteroiden_dreh_geschwindigkeit_maximum = 300
    ):
        self.asteroiden_anzahl = asteroiden_anzahl
        self.asteroiden_groesse = asteroiden_groesse
        self.asteroiden_geschwindigkeit_minimum = asteroiden_geschwindigkeit_minimum
        self.asteroiden_geschwindigkeit_maximum = asteroiden_geschwindigkeit_maximum
        self.asteroiden_dreh_geschwindigkeit_maximum = asteroiden_dreh_geschwindigkeit_maximum
