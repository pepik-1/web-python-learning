# база данных
### create

Создает обьект:Таблица,база, индекс
```sql
CREATE TABLE employees(
   id SERIAL PRIMARY KEY,
   name TEXT NOT NULL,
   salary NUMERIC
)
```
### TABLE
```sql
CREATE TABLE departaments(
   id SERIAL PRIMARY KEY,
   name TEXT,
   
)
```

### `alter`

```sql
ALTER TABLE employees
ADD COLUMN email TEXT;
```
### `add`
Добавляет колонку или ограничения
```sql
ALTER TABLE employees
ADD COLUMN phone TEXT
```

### `DROP`
Удаляет обьект(таблицу)
```sql
DROP TABLE projects;
```

### `IF EXISTS`
allow to avoid errors if no object
```
DROP TABLE IF EXISTS old_projects;
```

### `IF NOT EXISTS`
create an object if it does not exists
```
CREATE TABLE IF NOT EXISTS department(
 id SERIAL PRIMARY KEY,
 name TEXT
);
```

### 'RENAME'
rename an object
```sql
 ALTER TABLE employees
 RENAME COLUMN name to full_name;
```
### `TRUNCATE`
quick table delete
```sql
 TRUNCATE TABLE projects;
```

## 2.work with data
### `SELECT`
select data
```sql
SELECT name,salary FROM employees;

### `FROM`
points sourse of data
```sql
SELECT name,salery FROM employees
```

### `INSERT`
add strings
```sql
INSERT INTO departments(name)
VALUES ('IT'),('HR'),'FINANCE')
```

### `INTO`
points where to paste data
```sql
INSERT INTO employees(name,salary,department_id)
VALUES ('Ann',12000,1)
```
### `VALUES`
gives certain data
```sql
INSERT INTO projects(name,employee_id,budget)
VALUES('CRM System',1,50000)
```



## 2. work with data

### `update`
refreshing strings
``` sql
UPDATE employees
SET salary = salary * 1.10
WHERE department_id = 1;
```

### `SET`
Sets new 

```sql
UPDATE projects
SET is_active = FALSE
WHERE budget < 100000;
```

### 'DELETE'
deletes strings
```sql
DELETE FROM employees
WHERE salary < 50000
```

## 3. data filtration

### 'WHERE'
filting strs
``` sql
SELECT
FROM employees
WHERE salary > 100000
```

### `AND`
bouth conditions must be True

### 'OR'
one of condition might be true
``` sql
SELECT
FROM employees
WHERE salary > 100000
    or departament_id = 1;
```

### `NOT`
negative condition
``` sql
SELECT 
FROM projects
WHERE NOT is_active
```

### `IN`
Checks condition in a list
``` sql
SELECT *
FROM employees
WHERE department_id IN (1,2);
```

### `NOT IN`
checks that value not in a list
```sql
SELECT *
FROM employees
WHERE department_id NOT IN (1,2);
```

### `BETWEEN`
checks a range
```sql
SELECT *
FROM employees
WHERE salary BETWEEN 80000 AND 150000
```

### `LIKE`

```sql
search by template
SELECT *
FROM employees 
WHERE name ILITE "a%";
```

### `IS NULL` 
Checks value with 'NULL'
```sql
SELECT *
FROM employees
WHERE department_id IS NULL;
```

### `IS NOT NULL` 
Checks value with not 'NULL'
```sql
SELECT *
FROM employees
WHERE department_id IS NOT NULL;
```

### `EXISTS`
checks existance
```sql
SELECT *
FROM departaments AS d
WHERE EXISTS(
    SELECT 1
    FROM employees AS e
    WHERE e.departments_id = d.id
)

## 4. Sorting and limiting

Sorts result
```sql
SELECT *
FROM employees
ORDER BY salary;
```

### 'ASC'
sort by raising
```sql
SELECT *
FROM employees
ORDER BY salary ASC
```

### 'DESC`
Sort by downing
```sql
SELECT *
FROM employees
ORDER BY salary DESC
```

### `LIMIT`

limit an amount of strs

``sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 5
```

### `OFFSET`
skips a pointed amount of strs
``sql
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 10 OFFSET 20
```

## 5. Grouping and agregats

### `GROUP BY `
groups strings
```sql
SELECT department_id, COUNT(*) as employee_count
FROM employees
GROUP BY department_id
```

### 'HAVING'
Filters groups after `Group by`
```sql
SELECT department_id, AVG(salary) as avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 100000
```

### `COUNT`
counts strings.
```sql
SELECT COUNT(*)
FROM employees:
```

### `Sum`
sums values
```sql
SELECT SUM(budget)
FROM projects;
```

### `AVG`
counts aerage result
```sql
SELECT AVG(budget)
FROM projects;
```

### `MIN`
minimum value
counts aerage result
```sql
SELECT MIN(budget)
FROM projects;
```

### `max`
max value
counts aerage result
```sql
SELECT MAX(salary)
FROM employees;
```


### `DISTINCT`

deletes dubles

```sql
SELECT DISTINCT department_id
FROM employees
```

## 6. unaiting tabbles

### `JOIN`
joins tables

```sql
SELECT e.name, d.name as department
FROM employees AS e
JOIN departments d ON e.department_id = d.id
```

### `INNER JOIN`
join that shows only simular strings 

```sql
SELECT e.name, p.name AS project
FROM employees AS e
INNER JOIN projects p ON p.employee_id = e.id
```



### `LEFT JOIN`
shows strings from the left table, even if the right one doesn`t have simularities
```sql
SELECT e.name, p.name AS project
FROM employees AS e
LEFT JOIN projects p ON p.employee_id = e.id
```



### `RIGHT JOIN`
shows strings from the left table, even if the right one doesn`t have simularities
```sql
SELECT e.name, p.name AS project
FROM employees AS e
RIGHT JOIN projects p ON p.employee_id = e.id
```


### `FULL JOIN`
Shows all strings from bouth tables
```sql
SELECT e.name, p.name, AS project
FROM employees AS e
FULL JOIN projects p ON p.employee_id = e.id
```


### `ON`
condition of connection
```sql
SELECT employees AS e
JOIN departments d ON e.department_id = d.id
```

## 7. aliases

### `AS`
Gives a nickname to the pilar or the table
```sql
SELECT name AS employee_name,
    salary AS mounthly_salary
FROM employees AS e
```

```sql
SELECT e.name
FROM employees e
```

## 8. tables limiting

### `PRIMARY KEY`
The main KEY
```sql
CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name TEXT
)
```


### `FOREIGN KEY`
an outside KEY
```sql
CREATE TABLE departments(
    id SERIAL PRIMARY KEY,
    name TEXT,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments
    (id)
)
```
short writing
```sql
department_id INT REFERENCES departments(id),
```

### `REFERENCES`
point on what table or column points the key
```sql
department_id INT REFERENCES departments(id),
```

### `NOT NULL`
Prohibits NULL
```sql
name TEXT NOT NULL
```


### ` NULL`
no NULL
```sql
INSERT INTO employees(name,salary,department_id)
VALUES ('IVAN',NULL,1)
```

### `unique`
value must be unique
```sql
ALTER TABLE employees
ADD CONSTRAINT unique_employee_email UNIQUE(email);
```


### `CONSTRAINT`
gives a name to the limit
```sql
ALTER TABLE employees
ADD CONSTRAINT salary_positive CHECK (salary > 0);
```

### `CHECK`
checks condition
```sql
ALTER TABLE employees
ADD CONSTRAINT salary_positive CHECK (salary > 0);
```

### `DEFAULT`
default value
```sql
ALTER TABLE projects
ALTER COLUMN is_active SET DEFAULT TRUE;
```

