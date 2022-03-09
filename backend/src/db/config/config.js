const trimEnvVar = (envVar) => {
  return envVar ? envVar.trim() : '';
};

module.exports = {
  production: {
    username: trimEnvVar(process.env.POSTGRES_USER),
    password: trimEnvVar(process.env.POSTGRES_PASSWORD),
    database: trimEnvVar(process.env.POSTGRES_DB),
    host: trimEnvVar(process.env.POSTGRES_HOST),
    port: trimEnvVar(process.env.POSTGRES_PORT),
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
