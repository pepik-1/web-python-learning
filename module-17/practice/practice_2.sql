select name,salary,
	case 
		when salary >= 150000 then 'high'
		when salary >= 100000 then 'middle'
		else 'low'
	end as salary_level
from employees;
	
-- -----------------------

select 
	e.name as employee_name, 
	coalesce(d.name,'no department') as department_name
from employees e 
left join departments d on e.department_id = d.id

-- --------------------------------------------

select 
	d.id,
	d.name
from departments d
where exists(
select 1 from employees e 
where e.department_id = d.id 
);


-- ------------------------------------------------

select 
	e.name,
	e.id
from employees e 
where exists(
select 1 from projects p
where e.id = p.employee_id 
);

-- ----------------------------------------------

select
	name as project_name,
	budget,
	case 
		when is_active = true then 'active'
		else  'close'
	end as project_status
from projects;

	
-- ----------------------------------------------

select
	e.name as employee_name,
	COUNT(p.id) as projects_count
from employees e 
left join projects p on p.employee_id = e.id
group by e.id, e."name" 
order by projects_count desc;

-- ----------------------------------------------

update projects
set budget = budget + 50000
where is_active = true
returning id, budget;

-- ----------------------------------------------

delete from projects 
where is_active = false 
returning id,name;


