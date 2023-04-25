-- 코드를 입력하세요
SELECT B.USER_ID, B.NICKNAME,
    CONCAT(B.CITY," ",B.STREET_ADDRESS1," ",B.STREET_ADDRESS2) AS "전체주소",
    -- 여러 문자열 합치기: CONCAT(a,b,c,...)
    CONCAT(LEFT(B.TLNO,3),"-",SUBSTR(B.TLNO,4,4),"-",RIGHT(B.TLNO,4)) AS "전화번호"
    -- LEFT: 문자열의 LEFT부터 n개
    -- RIGHT: 문자열의 RIGHT부터 n개 (순서는 정순 유지!!)
    -- SUBSTR(A,n,m): 문자열의 n번째 문자부터(포함), 총 m개의 문자
FROM USED_GOODS_BOARD AS A

LEFT JOIN USED_GOODS_USER AS B
ON A.WRITER_ID = B.USER_ID

GROUP BY A.WRITER_ID
HAVING COUNT(*) >= 3

ORDER BY USER_ID DESC