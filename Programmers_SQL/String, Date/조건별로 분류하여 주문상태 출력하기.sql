-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE,"%Y-%m-%d"),
    IF(ISNULL(OUT_DATE),"출고미정",IF(DATEDIFF(OUT_DATE,"2022-05-02")>0,"출고대기","출고완료")) AS "출고여부"
FROM FOOD_ORDER
ORDER BY ORDER_ID