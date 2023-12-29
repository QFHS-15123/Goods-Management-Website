CREATE TABLE box (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  comment TEXT,
  updated_time TEXT NOT NULL,
  created_time TEXT NOT NULL,
  is_deleted integer default 0 not null
);

CREATE TABLE goods (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  status TEXT NOT NULL,
  comment TEXT,
  updated_time TEXT NOT NULL,
  created_time TEXT NOT NULL,
  box_id INTEGER NOT NULL,
  FOREIGN KEY (box_id) REFERENCES box(id)
);