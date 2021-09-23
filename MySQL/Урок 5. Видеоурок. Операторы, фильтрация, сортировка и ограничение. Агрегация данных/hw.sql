/*  
����� � ������� users ���� created_at � updated_at ��������� ��������������. 
��������� �� �������� ����� � ��������.
*/  
UPDATE users 
SET created_at = NOW(), updated_at = NOW();

/*  
������� users ���� �������� ��������������. 
������ created_at � updated_at ���� ������ ����� VARCHAR � � ��� ������ ����� ���������� 
�������� � ������� 20.10.2017 8:10. ���������� ������������� ���� � ���� DATETIME, 
�������� �������� ����� ��������.
*/ 
UPDATE users
SET 
created_at = STR_TO_DATE(created_at, '%d/%m/%Y %h:%i'), 
updated_at = STR_TO_DATE(created_at, '%d/%m/%Y %h:%i');

/*  
� ������� ��������� ������� storehouses_products � ���� value ����� ����������� ����� ������ �����: 0,
���� ����� ���������� � ���� ����, ���� �� ������ ������� ������. ���������� ������������� 
������ ����� �������, ����� ��� ���������� � ������� ���������� �������� value. 
������ ������� ������ ������ ���������� � �����, ����� ���� 
*/ 
SELECT * FROM storehouses_products ORDER BY CASE WHEN value = 0 THEN 9999999999 ELSE value END;
