from abc import ABC, abstractmethod
from validadorclave.modelo.errores import *


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self._longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) > self._longitud_esperada:
            return True
        else:
            return False

    def _contiene_mayuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isupper():
                return True
        return False

    def _contiene_minuscula(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        for caracter in clave:
            if caracter.isdigit():
                return True
        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class Validador:

    def __init__(self, regla: ReglaValidacion):
        self.regla = regla

    def es_valida(self, clave: str) -> bool:
        if self.regla.es_valida(clave):
            return True
        else:
            return False


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        for caracter in clave:
            if caracter in ["@", "_", "#", "$", "%"]:
                return True
            else:
                pass
        return False

    def es_valida(self, clave: str) -> bool:
        if self._validar_longitud(clave):
            if self._contiene_mayuscula(clave):
                if self._contiene_minuscula(clave):
                    if self._contiene_numero(clave):
                        if self.contiene_caracter_especial(clave):
                            return True
                        else:
                            raise NoTieneCaracterEspecialError
                    else:
                        raise NoTieneNumeroError
                else:
                    raise NoTieneLetraMinusculaError
            else:
                raise NoTieneLetraMayusculaError
        else:
            raise NoCumpleLongitudMinimaError


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave: str) -> bool:
        clave_minusculas = clave.lower()
        s = clave_minusculas.find("calisto")
        if s == -1:
            return False
        else:
            contador = 0
            if clave.isupper():
                return False
            else:
                for caracter in clave:
                    if caracter.isupper():
                        contador += 1
                        if contador >= 2:
                            return True
                return False

    def es_valida(self, clave: str) -> bool:
        if self._validar_longitud(clave):
            if self._contiene_numero(clave):
                if self.contiene_calisto(clave):
                    return True
                else:
                    raise NoTienePalabraSecretaError
            else:
                raise NoTieneNumeroError
        else:
            raise NoCumpleLongitudMinimaError