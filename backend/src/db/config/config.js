module.exports = {
  production: {
    username: process.env.POSTGRES_USER.trim(),
    password: process.env.POSTGRES_PASSWORD.trim(),
    database: process.env.POSTGRES_DB.trim(),
    host: process.env.POSTGRES_HOST.trim(),
    port: process.env.POSTGRES_PORT.trim(),
    dialect: 'postgres',
    logging: console.log,
    pool: {
      max: 5,
      min: 0,
      idle: 20000,
      acquire: 20000,
    },
  },
  test: {
    dialect: 'sqlite',
    storage: './database.sqlite3',
  },
};
