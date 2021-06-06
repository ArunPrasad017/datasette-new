create table result as
with cte_home as
(
    select 
    HomeTeam as home_team,
    sum(case when ftr='h' then 3 
             when ftr='d'then 1
             else 0 end
       ) as home_pts
    from laliga1819
    group by HomeTeam
),
cte_away as (
    select 
    awayteam as away_team,
    sum(case when lower(ftr)='a' then 3 
             when lower(ftr)='d' then 1
             else 0 end
       ) as away_pts
    from laliga1819
    group by awayteam
),
cte_total as(
    select home_team as team_name, home_pts as total_points
    from cte_home
    union all
    select away_team as team_name, away_pts as total_points
    from cte_away
)
select t.team_name as team, coalesce(sum(t.total_points),0) as season_total_points
from cte_total t
group by t.team_name
order by season_total desc,t.team_name;