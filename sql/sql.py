from lib.db import *

# 是否计提应交增值税-科研事业收入:4101.02,2101
sql_keyanshouru='''
SELECT
DISTINCT aa.voucher_code
from
(
SELECT
*
from 
(SELECT 
tvr.voucher_code,
tvr.debit_money,
tvr.credit_money,
IFNULL(tvr.debit_money,'0')+IFNULL(tvr.credit_money,'0') as account_money,
tvr.subject_code
FROM t_voucher_record tvr
WHERE tvr.business_date >= '2019-01-01'
AND tvr.subject_code REGEXP '^4101.2|4101.02'
) as tt
WHERE tt.account_money >= '1000000'
) as aa
JOIN
(
SELECT 
dd.voucher_code,
dd.subject_code_left
from 
(SELECT
	voucher_code,
	GROUP_CONCAT(LEFT(subject_code, 4)) AS subject_code_left
FROM
	t_voucher_record
WHERE 
business_date >= '2019-01-01'
and IFNULL(credit_money,'0')>0
GROUP BY
	voucher_code
ORDER BY
	voucher_code
) as dd
WHERE dd.subject_code_left not REGEXP '2101'
) as bb
on aa.voucher_code=bb.voucher_code
;
'''

# results=database.query(sql_keyanshouru)
# print(results)

