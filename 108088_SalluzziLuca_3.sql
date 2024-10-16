--Se necesita saber el promedio general para cada carrera y cada departamento. Devolviendo código de carrera, código de departamento, y el promedio de notas para todos los alumnos de cada departamento, ordenados por carrera y departamento. Nota: no considerar combinaciones de departamento / carrera tal que no haya alumnos de dicha carrera con notas en dicho departamento. Nota 2: Si un alumno está inscripto en más de una carrera, sus notas aportan a los promedios de todas esas carreras.
SELECT
    i.codigo AS codigo_carrera,
    n.codigo AS codigo_departamento,
    AVG(n.nota) AS promedio_nota
FROM
    notas n
    JOIN alumnos a ON n.padron = a.padron
    JOIN inscripto_en i ON i.padron = a.padron
GROUP BY
    i.codigo,
    n.codigo
ORDER BY i.codigo;

-- Resultado --
-- 5	61	7.0000000000000000
-- 5	62	7.2500000000000000
-- 6	61	8.8000000000000000
-- 6	62	7.0000000000000000
-- 9	71	6.7142857142857143
-- 9	75	6.6923076923076923
-- 10	71	6.7500000000000000
-- 10	75	6.5000000000000000