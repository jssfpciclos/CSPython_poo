from enum import IntEnum, IntFlag
from typing import Self, Tuple, List


class NivelAccesoEnum(IntEnum):
    # Completa este enumerado
    SIN_ACCESO = 0
    RESTRICTIVO = 1
    NORMAL = 2
    TOTAL = 3

    @staticmethod
    def verificar_acceso(nivel_acceso_usuario: Self, nivel_acceso_check: Self) -> bool:
        return nivel_acceso_usuario >= nivel_acceso_check


class ModuloEnum(IntFlag):
    VENTAS = 1
    COMPRAS = 2
    ALMACEN = 4
    CONTABILIDAD = 8
    RRHH = 16
    ADMINISTRACION = 32
    DIRECCION = 64


class UserAuth:
    def __init__(self, nombre: str, login: str):
        self.nombre = nombre
        self.login = login
        self.__nivel_acceso: dict[ModuloEnum, NivelAccesoEnum] = {}

    def get_module_access_level(self, module: ModuloEnum) -> NivelAccesoEnum:
        # Completa este método
        if module in self.__nivel_acceso:
            return self.__nivel_acceso[module]

        return False

    def assing_all_module_access(self, modules: dict[ModuloEnum, NivelAccesoEnum]):
        # Recorrer todos los módulos, y asignar acceso
        for moduloEnum, acceso in modules.items():
            self.__nivel_acceso[moduloEnum] = acceso

    def assign_module_access(self, module: ModuloEnum, nivel_acceso: NivelAccesoEnum):
        self.__nivel_acceso[module] = nivel_acceso

    def unassing_module_access(self, module: ModuloEnum):
        self.__nivel_acceso[module] = NivelAccesoEnum.SIN_ACCESO

    def reset_module_access(self):
        self.__nivel_acceso = {}

    def is_module_access(self, module: ModuloEnum) -> bool:
        if self.__nivel_acceso.get(module) and self.__nivel_acceso[module] > 0:
            return True

        return False

    def has_module_access(self, module: ModuloEnum, nivel_acceso: NivelAccesoEnum) -> bool:
        if self.__nivel_acceso.get(module) and self.__nivel_acceso[module] == nivel_acceso:
            return True
        return False


def main():
    user1 = UserAuth("Juan", "juanin")
    user1.assing_all_module_access({ModuloEnum.VENTAS: NivelAccesoEnum.NORMAL, ModuloEnum.COMPRAS: NivelAccesoEnum.RESTRICTIVO})

    assert user1.is_module_access(ModuloEnum.VENTAS) is True
    assert user1.is_module_access(ModuloEnum.COMPRAS) is True
    assert user1.is_module_access(ModuloEnum.ALMACEN) is False

    user1.unassing_module_access(ModuloEnum.VENTAS)
    assert user1.is_module_access(ModuloEnum.VENTAS) is False

    user1.reset_module_access()
    assert user1.is_module_access(ModuloEnum.VENTAS) is False
    assert user1.is_module_access(ModuloEnum.COMPRAS) is False

    user1.assign_module_access(ModuloEnum.COMPRAS, NivelAccesoEnum.TOTAL)
    user1.assign_module_access(ModuloEnum.VENTAS, NivelAccesoEnum.NORMAL)
    assert user1.has_module_access(ModuloEnum.VENTAS, NivelAccesoEnum.NORMAL) is True
    assert user1.has_module_access(ModuloEnum.VENTAS, NivelAccesoEnum.TOTAL) is False
    assert user1.has_module_access(ModuloEnum.COMPRAS, NivelAccesoEnum.NORMAL) is False
    assert user1.has_module_access(ModuloEnum.COMPRAS, NivelAccesoEnum.SIN_ACCESO) is False


if __name__ == "__main__":
    main()
