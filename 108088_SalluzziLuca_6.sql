-- Listar el padrón de aquellos alumnos que, por lo menos, tienen nota en todas las materias que aprobó el alumno del padrón 83000.WITH
-- Paso 1: Obtener las materias aprobadas por el alumno 83000
SELECT distinct
    n1.padron
FROM
    notas n1
    INNER JOIN (
        SELECT n2.codigo, n2.numero
        FROM notas n2
        WHERE
            n2.padron = 83000
            and n2.nota >= 4
    ) as materias_aprobadas_por_83000 USING (codigo, numero)
WHERE
    n1.padron <> 83000;
-- Resultados --
-- 85000
-- 84000