const models = require('../db/models');

exports.getPerformUpdate = (req, res, next) => {
  res.status(201).json({ message: 'Updates' });
};

exports.getLastUpdate = (req, res, next) => {
  res.status(201).json({ message: 'Last update' });
};

exports.getHealth = (req, res, next) => {
  res.status(200).json({ message: 'OK' });
};
