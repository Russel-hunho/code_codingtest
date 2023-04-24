# LEFT JOIN



# DATE_FORMAT


# HOUR()
 -> 인트형으로 되는듯!

LIMIT N;
-- ORDER BY 이후 상위 N개만 출력
-- 모든 구문의 맨 마지막!


-- 구문 순서
SELECT A, COUNT(*), AVG(B+C) AS D
FROM AA

JOIN BB AS C
ON AA.A = C.D

WHERE AA.A > 10

GROUP BY C.F
HAVING C.F > 8

ORDER BY C.F ASC, C.D DESC --C.F기준 오름차순 후 C.D 기준 내림차순

LIMIT 8 --상위 8개만 출력
