-- 코드를 입력하세요
-- https://jaaamj.tistory.com/155
SET @HOUR = -1; -- SET 구문은 구문된 쿼리문이므로, ';'으로 끝내줘야됨!!

-- 정의된 @HOUR 이용, 0~23 Table 만드는 법
/* 
SELECT (@HOUR := @HOUR +1) AS HOUR
FROM ANIMAL_ID -- 아무 실존하는 Table이면 다 될듯
WHERE @HOUR < 23
*/


SELECT (@HOUR := @HOUR +1) AS HOUR -- SET으로 정의된 변수 사용법: ':=' 기호 사용 주의!
    ,( SELECT COUNT(*)
        FROM ANIMAL_OUTS
        WHERE HOUR(DATETIME) = @HOUR
    ) AS COUNT
FROM ANIMAL_OUTS
WHERE @HOUR < 23;