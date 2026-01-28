-- =====================================================
-- SUPABASE POSTGRES – VERIFICATION & DEBUG QUERIES
-- Project: flask-crud-sqlite-supabase
-- Database: Supabase (Postgres)
-- =====================================================

-- -----------------------------------------------------
-- 1. LIST ALL TABLES IN PUBLIC SCHEMA
-- -----------------------------------------------------
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

-- Expected tables:
-- alembic_version
-- user


-- -----------------------------------------------------
-- 2. VIEW ALL USERS
-- -----------------------------------------------------
SELECT *
FROM public."user"
ORDER BY created_at DESC;


-- -----------------------------------------------------
-- 3. VIEW SELECTED COLUMNS
-- -----------------------------------------------------
SELECT id, full_name, email, phone
FROM public."user";


-- -----------------------------------------------------
-- 4. CHECK SPECIFIC USER BY EMAIL
-- -----------------------------------------------------
SELECT full_name, phone, age, gender
FROM public."user"
WHERE email = 'rahul@gmail.com';


-- -----------------------------------------------------
-- 5. COUNT TOTAL USERS
-- -----------------------------------------------------
SELECT COUNT(*) AS total_users
FROM public."user";


-- -----------------------------------------------------
-- 6. VERIFY UPDATE (RECENT RECORD)
-- -----------------------------------------------------
SELECT *
FROM public."user"
ORDER BY created_at DESC
LIMIT 1;


-- -----------------------------------------------------
-- 7. VERIFY DELETE (COUNT CHECK)
-- -----------------------------------------------------
SELECT COUNT(*) 
FROM public."user";


-- -----------------------------------------------------
-- 8. CHECK UNIQUE EMAIL CONSTRAINT (TEST ONLY)
-- -----------------------------------------------------
-- This should FAIL if email already exists
INSERT INTO public."user"
(full_name, email, phone)
VALUES
('Duplicate Test', 'anjali.v@company.com', '9000000000');


-- -----------------------------------------------------
-- 9. CHECK ALEMBIC MIGRATION VERSION
-- -----------------------------------------------------
SELECT * FROM alembic_version;
