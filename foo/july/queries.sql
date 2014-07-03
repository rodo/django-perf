SELECT relname,
  heap_blks_read,
  heap_blks_hit,
  toast_blks_read,
  toast_blks_hit
FROM
  pg_statio_user_tables WHERE schemaname = 'public' and relname like
  'july_%' order by relname;
