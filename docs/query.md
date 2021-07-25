## 基本形
```sql

SELECT *
  FROM credit_card_complaints
 LIMIT 100;

```

```
   complaint_id date_received  ... timely_response consumer_disputed
0        469026    2013-07-29  ...             Yes               Yes
1        469131    2013-07-29  ...             Yes                No
2        479990    2013-07-29  ...             Yes                No
3        475777    2013-07-29  ...             Yes                No
4        469473    2013-07-29  ...             Yes               Yes
..          ...           ...  ...             ...               ...
95       466061    2013-07-25  ...             Yes                No
96       466091    2013-07-25  ...             Yes                No
97       464970    2013-07-24  ...             Yes                No
98       465004    2013-07-24  ...             Yes                No
99       482668    2013-08-07  ...             Yes                No

[100 rows x 18 columns]
```
** COUNT
#+begin_src sql

SELECT COUNT(*)
  FROM credit_card_complaints;

#+end_src

#+begin_src
   count
0  87718
#+end_src
** IS NOT NULL
#+begin_src sql

SELECT COUNT(*)
  FROM credit_card_complaints
 WHERE consumer_complaint_narrative IS NOT NULL;

#+end_src

#+begin_src
   count
0  17433
#+end_src
** IS NULL
#+begin_src sql

SELECT COUNT(*)
  FROM credit_card_complaints
 WHERE consumer_complaint_narrative IS NULL;

#+end_src

#+begin_src
   count
0  70285
#+end_src
