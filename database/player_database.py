import sqlite3
conn = sqlite3.connect('player_database.db')
c = conn.cursor()
# Creates a table for Players
c.execute("""CREATE TABLE players (
  refnum integer,
  team text,
  name text,
  str integer,
  str_mod integer,
  dex integer,
  dex_mod integer,
  wis integer,
  wis_mod integer,
  cha integer,
  cha_mod integer,
  mag integer,
  mag_mod integer,
  dmag integer,
  dmag_mod integer,
  gk integer,
  gk_mod integer
  )""");

c.execute("""CREATE TABLE captains (
  team text,
  name text
  )""")


c.execute("INSERT INTO players VALUES (1,'Ghosts', 'Gobro Gons',	14,	2,	14,	2,	16,	3,	15,	2,	15,	2,	15,	2,	13,	1)")

c.execute("INSERT INTO players VALUES (2,'Ghosts','Basiliano Milano',	11,	0,	10,	0,	12,	1,	13,	1,	14,	2,	14,	2, 0, 0)")

c.execute("INSERT INTO players VALUES (3,'Ghosts','Cora Twill',	10,	0,	13,	1,	12,	1,	13,	1,	10,	0,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (4,'Ghosts','Nadezda York',	8,	-1,	8,	-1,	16,	3,	10,	0,	15,	2,	12,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (5,'Ghosts','Vasanti Cruz',	16,	3,	14,	2,	12,	1,	15,	2,	14,	2,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (1,'Conjurers','Hashad Kahn',	10,	0,	11,	0,	16,	3,	9,	-1,	14,	2,	11,	0,	17,	3)")

c.execute("INSERT INTO players VALUES (2,'Conjurers','Jon-Paul Jericho',	14,	2,	12,	1,	13,	1,	15,	2,	13,	1,	17,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (3,'Conjurers','Djimi Koundé',	10,	0,	14,	2,	10,	0,	15,	2,	10,	0,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (4,'Conjurers','Mandy Malakar',	9,	-1,	11,	0,	10,	0,	13,	1,	8,	-1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (5,'Conjurers','Tel''blort',	8,	-1,	8,	-1,	14,	2,	16,	3,	14,	2,	15,	2, 0, 0)")

c.execute("INSERT INTO players VALUES (1,'Wizards','Shalva Pallesen',	12,	1,	8,	-1,	9,	-1,	13,	1,	13,	1,	9,	-1,	15,	2)")

c.execute("INSERT INTO players VALUES (2,'Wizards','Garel''blort',	13,	1,	11,	0,	11,	0,	13,	1,	15,	2,	16,	3, 0, 0)")

c.execute("INSERT INTO players VALUES (3,'Wizards','Karl-Armando Pugh',	9,	-1,	16,	3,	10,	0,	8,	-1,	8,	-1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (4,'Wizards','Holland O’Dafferty',	14,	2,	9,	-1,	11,	0,	10,	0,	10,	0,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (5,'Wizards','Mogan Squip',	14,	2,	9,	-1,	16,	3,	16,	3,	12,	1,	13,	1, 0, 0)")

c.execute("INSERT INTO players VALUES (1,'Omegas','Helias King',	12,	1,	8,	-1,	12,	1,	18,	4,	11,	0,	8,	-1,	18,	4)")

c.execute("INSERT INTO players VALUES (2,'Omegas','Lyman Hollencrantz',	13,	1,	11,	0,	15,	2,	6,	-2,	13,	1,	13,	1,	0, 0)")

c.execute("INSERT INTO players VALUES (3,'Omegas','Pradip Santana',	15,	2,	16,	3,	14,	2,	13,	1,	13,	1,	10,	0,	0, 0)")

c.execute("INSERT INTO players VALUES (4,'Omegas','Amelia Lacroix',	16,	3,	14,	2,	9,	-1,	11,	0,	7,	-2,	13,	1,	0, 0)")

c.execute("INSERT INTO players VALUES (5,'Omegas','Khil Metarot',	10,	0,	15,	2,	12,	1,	10,	0,	17,	3,	14,	2,	0, 0)")

c.execute("INSERT INTO players VALUES (1,'Unicorns','Neuvo Urriciani',  15, 2,  13, 1,  9, -1,  14, 2,  14, 2,  16, 3,  14, 2)")

c.execute("INSERT INTO players VALUES (2,'Unicorns','Igor Rendón',  10, 0,  11, 0,  11, 0,  14, 2,  10, 0,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Unicorns','Jonatan Towner',  13, 1, 15, 2,  16, 3,  12, 1,  16, 3,  16, 3,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Unicorns','Sofia Mertens',  12, 1,  10, 0,  13, 1,  10, 0,  11, 0,  10, 0,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Unicorns','Diamond Cabbagestalk',  8, -1,  11, 0,  14, 2,  8, -1,  12, 1,  9, -1,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'Curves','Gwong Klopso',  12, 1,  11, 0,  13, 1,  11, 0,  12, 1,  15, 2,  14, 2)")

c.execute("INSERT INTO players VALUES (2,'Curves','Goma Glib',  14, 2,  9, -1,  13, 1,  9, -1,  11, 0,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Curves','Tekkel''blort',  5, -3,  13, 1,  13, 1,  14, 2,  17, 3,  12, 1,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Curves','Ralston Crux',  16, 3,  12, 1,  8, -1,  7, -2,  7, -2,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Curves','Bandy Moscato',  17, 3,  11, 0,  13, 1,  15, 2,  6, -2,  9, -1,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'Dragons','Daisuke Sato',  7, -2,  13, 1,  8, -1,  13, 1,  13, 1,  14, 2,  13, 1)")

c.execute("INSERT INTO players VALUES (2,'Dragons','Paro''blort',  10, 0,  16, 3,  13, 1,  6, -2,  14, 2,  7, -2,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Dragons','Tad Garbaj',  12, 1,  10, 0,  12, 1,  13, 1,  12, 1,  8, -1,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Dragons','Thankful Tenniford',  16, 3,  15, 2,  14, 2,  10, 0,  17, 3,  7, -2,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Dragons','Horus Shelp',  9, -1,  8, -1,  11, 0,  15, 2,  13, 1,  4, -3,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'Frogs','Tamara Edison',  13, 1,  10, 0,  15, 2,  10, 0,  13, 1,  16, 3,  13, 1)")

c.execute("INSERT INTO players VALUES (2,'Frogs','Borjo Blozok',  10, 0,  14, 2,  12, 1,  15, 2,  15, 2,  11, 0,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Frogs','Gauchinho',  11, 0,  12, 1,  14, 2,  14, 2,  15, 2,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Frogs','Sylvia Trask',  10, 0,  17, 3,  13, 1,  15, 2,  13, 1,  12, 1,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Frogs','Talia Jeffers',  13, 1,  11, 0,  14, 2,  13, 1,  13, 1,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'Whales','Sharn''blort',  9, -1,  10, 0,  14, 2,  8, -1,  11, 0,  16, 3,  12, 1)")

c.execute("INSERT INTO players VALUES (2,'Whales','Ptolemy Crass',  10, 0,  15, 2,  12, 1,  15, 2,  15, 2,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'Whales','Cristiana',  17, 3,  15, 2,  10, 0,  15, 2,  12, 1,  16, 3,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'Whales','Martin Murray',  17, 3,  14, 2,  16, 3,  12, 2,  14, 1,  6, -2,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'Whales','Tanner Dulce',  11, 0,  15, 2,  13, 1,  10, 0,  12, 1,  9, -1,  0, 0)")

c.execute("INSERT INTO players VALUES (1,'NFT','Secundus Senior',  8, -1,  16, 3,  8, -1,  12, 1,  13, 1, 11, 0,  18, 4)")

c.execute("INSERT INTO players VALUES (2,'NFT','Shiva Moss',  15, 2,  13, 1,  12, 1, 17, 3,  13, 1,  13, 1,  0, 0)")

c.execute("INSERT INTO players VALUES (3,'NFT','Dooley Tarver',  14, 2,  16, 3,  13, 1,  14, 2,  13, 1,  14, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (4,'NFT','Roger',  13, 1,  10, 0,  14, 2, 9, -1, 15, 2,  15, 2,  0, 0)")

c.execute("INSERT INTO players VALUES (5,'NFT','Gando''blort',  15, 2,  13, 1,  15, 2,  16, 3,  11, 0,  15, 2,  0, 0)")


c.execute("INSERT INTO captains VALUES ('NFT','Shiva Moss')")

c.execute("INSERT INTO captains VALUES ('Whales','Ptolemy Crass')")

c.execute("INSERT INTO captains VALUES ('Frogs','Sylvia Trask')")

c.execute("INSERT INTO captains VALUES ('Dragons','Horus Shelp')")

c.execute("INSERT INTO captains VALUES ('Curves','Bandy Moscato')")

c.execute("INSERT INTO captains VALUES ('Unicorns','Igor Rendón')")

c.execute("INSERT INTO captains VALUES ('Omegas','Helias King')")

c.execute("INSERT INTO captains VALUES ('Wizards','Mogan Squip')")

c.execute("INSERT INTO captains VALUES ('Conjurers','Tel''blort')")

c.execute("INSERT INTO captains VALUES ('Ghosts','Gobro Gons')")




conn.commit()
conn.close()
