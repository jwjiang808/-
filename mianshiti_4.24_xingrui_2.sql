SELECT 
  keyword, 
  DATE_FORMAT(date, '%Y-%m') AS month, 
  SUM(pc) AS pc_count, 
  SUM(mobile) AS mobile_count
FROM keyword_index 
WHERE date >= '2010-01-01' AND date < '2022-01-01'
GROUP BY keyword, month;
