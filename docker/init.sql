CREATE TABLE "general"(
	"id"		INT PRIMARY KEY,
	"owner"		VARCHAR(255) NOT NULL,
	location    VARCHAR(255),
	from_year 	DATE,
	to_year		DATE
);

CREATE TABLE account(
	"id"		SMALLSERIAL PRIMARY KEY,
	username	CHAR(50) NOT NULL UNIQUE,
	"name"		VARCHAR(255),
	"password"  CHAR(61) NOT NULL
);

CREATE TABLE population(
	"id" CHAR(13) PRIMARY KEY,
	full_name VARCHAR(255) NOT NULL,
	other_name VARCHAR(255),
	date_of_birth DATE NOT NULL,
	gender SMALLINT NOT NULL,
	born_location VARCHAR(255),
	domicile VARCHAR(255),
	temp_residence_addr JSON [],
	perm_residence_addr JSON [],
	job JSON [],
	ethnic VARCHAR(255),
	religion VARCHAR(255),
	passport_number CHAR(12),
	household_id CHAR(12),
	relationship_with_householder SMALLINT,
	identification_number CHAR(12),
	updated_date TIMESTAMP
);

CREATE TABLE household(
	"id" CHAR(12) PRIMARY KEY,
	householder_id CHAR(13),
	house_number VARCHAR(255),
	street_hamlet VARCHAR(255),
	commune_ward VARCHAR(255),
	city_district_town VARCHAR(255),
	province VARCHAR(255),
	register_date DATE,
	updated_date TIMESTAMP
);

ALTER TABLE population ADD CONSTRAINT fk_population_household FOREIGN KEY (household_id) REFERENCES household (id);

ALTER TABLE household ADD CONSTRAINT fk_household_population FOREIGN KEY (householder_id) REFERENCES population (id);


INSERT INTO "general"("id", "owner", location,from_year, to_year)
VALUES (1, 'Nguyễn Đức Minh', 'Quận Đống Đa, Thành phố Hà Nội','2020-01-01', '2025-01-01');

INSERT INTO "account"(username, "name", "password")
VALUES
('Long.DT205096@sis.hust.edu.vn', 'Đinh Thành Long', '20205096'),
('Tuan.NQ200563@sis.hust.edu.vn', 'Nguyễn Quang Tuấn', '20200563');

INSERT INTO population( id, 
						full_name, 
						other_name, 
						date_of_birth, 
						gender, 
						born_location, 
						domicile, 
						temp_residence_addr, 
						perm_residence_addr, 
						job,
						ethnic,
						religion,
						passport_number,
						identification_number)
VALUES ('0060020810001', 
		'Nguyễn Quang Tuấn', 
		NULL, 
		'2002-02-22', 
		0, 
		'Hồng Bàng, Hải Phòng', 
		'Hồng Bàng, Hải Phòng', 
		ARRAY[]::json[],
		ARRAY[]::json[],
		ARRAY[]::json[],
		NULL,
		NULL,
		NULL,
		'031202000066');


INSERT INTO household(id, householder_id, house_number, street_hamlet, commune_ward, city_district_town, province)
VALUES ('006002081001', '0060020810001', '125 Binh đoàn 11', 'Hồ Đắc Di', 'Nam Đồng', 'Đống Đa', 'Hà Nội');


UPDATE population SET household_id = '006002081001' WHERE id = '0060020810001';


CREATE TABLE asset(
	id		SERIAL PRIMARY KEY,
	name	VARCHAR(255),
	qty		SMALLINT
);

CREATE TABLE department(
	id 		SERIAL PRIMARY KEY,
	name	VARCHAR(255)
);

CREATE TABLE event(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	owner VARCHAR(255),
	owner_contact CHAR(10),
	department_id INT,
	fee	INT,
	status SMALLINT,
	from_time TIMESTAMP,
	to_time TIMESTAMP,
	accepter VARCHAR(255),
	FOREIGN KEY (department_id) REFERENCES department(id)
);

INSERT INTO asset(name, qty)
VALUES ('Bàn', 10),
	   ('Ghế', 50),
	   ('Mic', 3),
	   ('Loa', 5);


INSERT INTO department(name)
VALUES ('Hội trường tầng 1'), ('Phòng chức năng 1'), ('Phòng chức năng 2'), ('Phòng chức năng 3');