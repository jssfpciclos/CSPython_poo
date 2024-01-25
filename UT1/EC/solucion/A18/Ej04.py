from enum import IntFlag


class PermisoFicheroEnum(IntFlag):
    NADA = 0
    LECTURA = 1
    ESCRITURA = 2
    EJECUCION = 4


    @staticmethod
    def letter_to(letter: str):
        if letter == "r":
            return PermisoFicheroEnum.LECTURA
        if letter == "w":
            return PermisoFicheroEnum.ESCRITURA
        if letter == "x":
            return PermisoFicheroEnum.EJECUCION

        return PermisoFicheroEnum.NADA


class PermisoOpcionEnum(IntFlag):
    USUARIO = 1
    GRUPO = 2
    OTROS = 3


class PermisoFichero:

    def __init__(self, fichero: str, permisos: str):
        self.name = fichero
        self.__permisos: dict[PermisoOpcionEnum, PermisoFicheroEnum] = {}
        self.__permisos = self.__convert_permiso_letras_to_dict(permisos)

    def __convert_permiso_letras_to_dict(self, permisos: str):
        permisos_calculados: dict = {}

        # 1. dividir los permisos en 3 partes
        permisos_calculados[PermisoOpcionEnum.USUARIO] = self.__convert_partletter_enum(permisos[1:4])
        permisos_calculados[PermisoOpcionEnum.GRUPO] = self.__convert_partletter_enum(permisos[4:7])
        permisos_calculados[PermisoOpcionEnum.OTROS] = self.__convert_partletter_enum(permisos[7:10])

        return permisos_calculados

    def __convert_partletter_enum(self, letters: str) -> PermisoFicheroEnum:
        permiso = PermisoFicheroEnum.NADA
        for letra in letters: # r-x
            permiso += PermisoFicheroEnum.letter_to(letra)

        return permiso

    # --- Metodos publicos ---
    def get_permiso(self, parte: PermisoOpcionEnum) -> PermisoFicheroEnum:
        return self.__permisos[parte]

    def get_permiso_numerico(self) -> str:
        pass

    def set_permiso(self, permiso: str | dict[PermisoOpcionEnum, PermisoFicheroEnum]) -> None:
        pass


def main():
    ficheroPermisos = PermisoFichero("fichero.txt", "----r--rwx")
    assert ficheroPermisos.get_permiso(PermisoOpcionEnum.USUARIO) in PermisoFicheroEnum.ESCRITURA


if __name__ == '__main__':
    main()
