### 1. Create table silsilah
DROP TABLE IF EXISTS "silsilah";
DROP SEQUENCE IF EXISTS seq_silsilah;
CREATE SEQUENCE seq_silsilah START 12;
CREATE TABLE IF NOT EXISTS "silsilah" (
"id" INTEGER NOT NULL DEFAULT 0,
"name" VARCHAR(100) NULL DEFAULT NULL,
"gender" VARCHAR(100) NULL DEFAULT NULL,
"status" VARCHAR(100) NULL DEFAULT NULL,
PRIMARY KEY ("id")
);
ALTER TABLE silsilah ALTER COLUMN id SET DEFAULT nextval('seq_silsilah');

### 2. Insert data keluarga
INSERT INTO public.silsilah VALUES
	(1, 'Budi', 'laki-laki', 'Ayah'),
	(2, 'Dedi', 'laki-laki', 'Anak'),
	(3, 'Dodi', 'laki-laki', 'Anak'),
	(4, 'Dede', 'laki-laki', 'Anak'),
	(5, 'Dewi', 'perempuan', 'Anak'),
	(6, 'Feri', 'laki-laki', 'Cucu'),
	(7, 'Farah', 'perempuan', 'Cucu'),
	(8, 'Gugus', 'laki-laki', 'Cucu'),
	(9, 'Gandi', 'laki-laki', 'Cucu'),
	(10, 'Hani', 'perempuan', 'Cucu'),
	(11, 'Hana', 'Perempuan', 'Cucu');

### 3. Query untuk mendapatkan semua anak Budi
SELECT * FROM silsilah WHERE status='Anak';

### 4. Query untuk mendapatkan cucu dari budi
SELECT * FROM silsilah WHERE status='Cucu';

### 5. Query untuk mendapatkan cucu perempuan dari budi
SELECT * FROM silsilah WHERE status='Cucu' AND gender='perempuan';

### 6. Query untuk mendapatkan bibi dari Farah
SELECT * FROM silsilah WHERE status='Anak' AND gender='perempuan';

### 7. Query untuk mendapatkan sepupu laki-laki dari Hani
SELECT * FROM silsilah WHERE status='Cucu' AND gender='laki-laki';

### 8 & 9 pada https://github.com/handole/silsilah.git
### 10. terlampir