-- Obtener el padrón y apellido de aquellos alumnos que tienen nota en las materias 75.40 y 75.41 y no tienen nota ni en la materia 62.05 ni en 75.0

SELECT DISTINCT
    a.padron,
    a.apellido
from alumnos a, notas n
where
    a.padron = n.padron
    and (
        n.codigo = 75
        and (
            n.numero = 40
            OR n.numero = 41
        )
    )
    and not exists (
        select 1
        from notas n2
        where
            n2.padron = a.padron
            and (
                n2.codigo = 62
                and n2.numero = 05
            )
            or (
                n2.codigo = 75
                and n2.numero = 0
            )
    )
    -- Resultado --
    -- 83000	Gómez
    -- 84000	López
    -- 85000	Fernández