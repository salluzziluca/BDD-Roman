--Para cada nota del alumno con la fecha de ingreso más reciente, mostrar su padrón, código de departamento, número de materia y el valor de la nota.
Select n.padron, n.codigo, n.numero, n.nota
From notas n
    JOIN alumnos a on a.padron = n.padron
WHERE
    a.fecha_ingreso = (
        SELECT MAX(fecha_ingreso)
        from alumnos
    )
-- Result --
-- 88000	75	1	9
-- 88000	71	14	8
-- 88000	75	42	7
-- 88000	75	6	9