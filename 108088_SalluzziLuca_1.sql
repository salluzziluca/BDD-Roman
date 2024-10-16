-- Obtener el padrón y apellido de el/los alumno/s que tenga/n la mayor cantidad de
-- materias promocionadas (asumiendo que se promociona si la nota es mayor o igual
-- a 7).

-- Paso 1: Contar la cantidad de materias promocionadas por cada alumno
WITH
    materias_promocionadas AS (
        SELECT a.padron, a.apellido, COUNT(*) AS cantidad_promocionadas
        FROM alumnos a
            JOIN notas n ON a.padron = n.padron
        WHERE
            n.nota >= 7
        GROUP BY
            a.padron,
            a.apellido
    ),
    -- Paso 2: Encontrar la cantidad máxima de materias promocionadas
    max_promocionadas AS (
        SELECT MAX(cantidad_promocionadas) AS max_cantidad
        FROM materias_promocionadas
    )
    -- Paso 3: Seleccionar los alumnos que tienen esa cantidad máxima de materias promocionadas
SELECT mp.padron, mp.apellido
FROM
    materias_promocionadas mp
    JOIN max_promocionadas mx ON mp.cantidad_promocionadas = mx.max_cantidad;

-- Resultados --
-- --
-- 88000	Vargas
-- 86000	Díaz
-- 83000	Gómez
-- 85000	Fernández