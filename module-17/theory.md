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
gives curtain data
```sql
INSERT INTO projects(name,employee_id,budget)
VALUES('CRM System',1,50000)
```


