SELECT relname,
  idx_scan,
  idx_tup_fetch
FROM
  pg_stat_user_tables WHERE schemaname = 'public' and relname like
  'july_%' order by relname;
