-- Quem é o motorista que faz mais multas no Paraná? 
-- R: Marcos Vinicius Nogueira
SELECT * FROM "db_multas"."multas_partitioned"
WHERE state='PR'
ORDER BY "total_multas" DESC;

-- 2 Qual o gênero que faz mais multas no Brasil?
-- R: Não binário
SELECT "genero", sum("total_multas")
FROM "db_multas"."multas_partitioned"
GROUP BY "genero";

-- 3. Qual o estado que mais faz multas no Brasil?
-- R: Paraná
SELECT "state", sum("total_multas")
FROM "db_multas"."multas_partitioned"
GROUP BY "state"
ORDER BY sum("total_multas") DESC;