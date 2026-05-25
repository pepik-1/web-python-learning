create table employee_profiles(
	id SERIAL primary key,
	employee_id INT unique references employees(id),
	phone TEXT unique,
	address TEXT,
	birth_date DATE
	)
	
insert into employee_profiles(employee_id,phone,address,birth_date)
values(1,'+7000000000','address-1','1980-05-25'),
	(2,'+7000000001','address-1','1981-05-25'),
	(3,'+7000000002','address-1','1982-05-25');

select
	e.name as employee_name,
	ep.phone,
	ep.address,
	ep.birth_date
from employees e
join employee_profiles ep on ep.employee_id = e.id 

insert into employee_profiles(
employee_id, phone, address, birth_date)
values 
	(1,'+70000000003','address-4','1995-05-25');

-- -------------------------------------------------
-- N -N
create table skills(
	id SERIAL primary key,
	name TEXT not null unique 
);

create table employee_skills(
	employee_id INT references employees(id),
	skill_id int references skills(id),
	primary key (employee_id,skill_id)
	
);

insert into skills(name) values('SQL'), ('PostgressSQL'), ('MySQL'), ('Excel');

insert into employee_skills(employee_id,skill_id) values(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,4);

select
	e.name as employee_name,
	s.name as skill_name
from employee_skills es
join employees e on es.employee_id = e.id 
join skills s on es.skill_id = s.id
order by e.name,s.name;


select 
	e.name as employee_name,
	e.salary,
	d.name as department_name,
	ep.phone,
	ep.address,
	p.name as project_name,
	s.name as skill_name
	from employees e
	left join departments d on d.id = e.department_id 
	left join employee_profiles ep on e.id = ep.employee_id 
	left join projects p on p.employee_id = e.id 
	left join employee_skills es on es.employee_id = e.id 
	left join skills s on es.skill_id = s.id
	order by e.name,p.name,s.name
	

-- ----------------------------------------------------------------

select
	e.name as employee_name,
	coalesce(sum(p.budget),0) as total_budget
	from employees e 
	left join projects p on e.id = p.employee_id
	group by e.id,e.name
	order by e.name

-- ----------------------------------------------------------------
	
select
	p.name as project_name,
	p.budget,
	e.name as employee_name,
	d.name as department_name
	from employees e
	join departments d	on d.id = e.department_id
	join projects p on p.employee_id = e.id 
	where p.is_active = true and p.budget > 200000 
	order by p.budget desc;
	
-- --------------------------------------------------------------------

select 
	e.name as employee_name,
	e.salary,
	d.name as department_name,
	p.name as project_name,
	p.budget 
	from employees e 
	left join departments d on d.id = e.department_id
	left join projects p on p.employee_id = e.id
	where e.salary between 90000 and 170000 and d.name in ('HR','IT','Finance') and p.is_active = true and p.budget > aug(e.salary)
	order by e.name,d.name,p.name
	
	
	
	
	
	
	
	
	
	