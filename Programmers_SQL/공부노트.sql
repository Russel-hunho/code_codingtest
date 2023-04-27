---- Join 방법
-- 1. LEFT JOIN
SELECT*
FROM A
LEFT JOIN B
ON A.item = B.item
-- A+ (A교B)
-- A는 다 유지, B가 추가되면서
---- A중 B에 없는 item은 NULL로 생성, 
---- B중 A에 없는 item은 추가 안됨
-- 2. JOIN: 교집합만 생성
-- 3. RIGHT JOIN: B + (A교B)


---- 문자열 합치기
CONCAT(B.CITY," ",B.STREET_ADDRESS1," ",B.STREET_ADDRESS2) AS "전체주소",
-- 여러 문자열 합치기: CONCAT(a,b,c,...)
CONCAT(LEFT(B.TLNO,3),"-",SUBSTR(B.TLNO,4,4),"-",RIGHT(B.TLNO,4)) AS "전화번호"
-- LEFT: 문자열의 LEFT부터 n개
-- RIGHT: 문자열의 RIGHT부터 n개 (순서는 정순 유지!!)
-- SUBSTR(A,n,m): 문자열의 n번째 문자부터(포함), 총 m개의 문자




# DATE_FORMAT
DATE_FORMAT(DATETIME,"%Y-%m-%d")
-- "2022-10-01" 형식의 문자열로 바꿔줌

# HOUR()
 -> 인트형으로 되는듯!

LIMIT N;
-- ORDER BY 이후 상위 N개만 출력
-- 모든 구문의 맨 마지막!


-- https://velog.io/@ygh7687/SQL-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC
-- 구문 문법 순서:
SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY
-- 실행 순서:
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY
SELECT A, COUNT(*), AVG(B+C) AS D
FROM AA

JOIN BB AS C
ON AA.A = C.D

WHERE AA.A > 10

GROUP BY C.F
HAVING C.F > 8

ORDER BY C.F ASC, C.D DESC --C.F기준 오름차순 후 C.D 기준 내림차순

LIMIT 8 --상위 8개만 출력









---- 2중쿼리 (sub Query)
-- 1. SELECT 절 서브쿼리
SELECT A.item,
    A.DATE,
    (
        SELECT B.ITEM
        
    )
FROM TB AS A
...

-- 2. FROM 절 서브쿼리
SELECT A.item 
FROM
(
    SELECT

) AS A -- FROM절에 사용한 테이블 형식의 쿼리에, 이름을 반드시 부여해야함! (Alias 할당)
WHERE A.item > 0
ORDER By A.DATE