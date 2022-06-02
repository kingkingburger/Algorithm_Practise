## 루시와 엘라 찾기(sql)

컬럼에 특정 문자열이 잇는지 검색할 때 사용합니다.

보통 컬럼에 특정 문자열이 있는지 검색할 때
`컬럼명 LIKE CONCAT('%', '검색할 문자열', '%')` 이런 식으로 사용합니다.



그런데 반대로 특정 문자열 안에 컬럼값이 있는지 저 방법으로 검색되나 싶어

```mysql
-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE 'Lucy, Ella, Pickle, Rogan, Sabrina, Mitty' LIKE CONCAT('%', NAME, '%')
ORDER BY ANIMAL_ID;
```

이런식으로도 가능합니다. 

