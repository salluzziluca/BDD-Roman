-- Mostrar el padrón, apellido y promedio para aquellos alumnos que tienen nota en más de 4 materias y un promedio de al menos 6.

WITH
    -- Paso 1: Contar la cantidad de materias aprobadas por cada alumno
    materias_aprobadas AS (
        SELECT a.padron, COUNT(*) AS cantidad_aprobadas
        FROM alumnos a
            JOIN notas n ON a.padron = n.padron
        WHERE
            n.nota >= 4
        GROUP BY
            a.padron
    ),
    -- Paso 2: Calcular el promedio de notas de cada alumno
    promedio_notas AS (
        SELECT a.padron, AVG(n.nota) AS promedio
        FROM alumnos a
            JOIN notas n ON a.padron = n.padron
        GROUP BY
            a.padron
    )
    -- Paso 3: Seleccionar los alumnos que tienen más de 4 materias aprobadas y promedio de al menos 6
SELECT a.padron, a.apellido, pn.promedio
FROM
    alumnos a
    JOIN materias_aprobadas ma ON a.padron = ma.padron
    JOIN promedio_notas pn ON a.padron = pn.padron
WHERE
    ma.cantidad_aprobadas > 4
    AND pn.promedio >= 6;

SELECT *
from notas
    -- Resultados --
    -- 73000	Molina	6.6000000000000000
    -- 86000	Díaz	7.8000000000000000