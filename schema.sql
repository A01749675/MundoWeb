DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS regional;
DROP TABLE IF EXISTS fmf_news;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE regional (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  event TEXT NOT NULL,
  url TEXT NOT NULL,
  direction TEXT NOT NULL
);

CREATE TABLE fmf_news (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT UNIQUE NOT NULL,
  description TEXT NOT NULL,
  date TEXT NOT NULL,
  link TEXT NOT NULL
);
