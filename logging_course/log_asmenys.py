from my_logger import logger


class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde
        logger.info(f"Sukurtas darbuotojas: {self.vardas} {self.pavarde}")


tadas = Asmuo("Tomas", "Kucinskas")
rokas = Asmuo("Rokas", "Radzevicius")
