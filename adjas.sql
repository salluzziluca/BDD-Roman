WITH
    tiempos_ciclistas AS (
        SELECT
            c.cod_ciclista,
            SUM(m.tiempo) AS tiempo_total,
            SUM(m.puntaje) AS puntaje_total
        FROM
            CICLISTAS c
            JOIN MARCAS m ON c.cod_ciclista = m.cod_ciclista
            JOIN ETAPAS e ON e.num_etapa = m.num_etapa
        GROUP BY
            c.cod_ciclista
    )
SELECT
    cod_ciclista,
    tiempo_total,
    puntaje_total
FROM tiempos_ciclistas
WHERE
    tiempo_total = (
        SELECT MIN(tiempo_total)
        FROM tiempos_ciclistas
    );