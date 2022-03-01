const models = require('../db/models');
const Sequelize = require('sequelize');

exports.getPerformUpdate = (req, res, next) => {
  res.status(201).json({ message: 'Updates' });
};

exports.getLastUpdate = async (req, res, next) => {
  const year = new Date().getFullYear();
  startDate = new Date(year, 1, 1);
  endDate = new Date(year, 12, 31);
  try {
    const updateRec = await models.Upgrade.findOne({
      order: [['date_value', 'DESC']],
      where: {
        date_value: {
          [Sequelize.Op.between]: [startDate, endDate],
        },
      },
    });

    if (updateRec) {
      return res.status(200).json(updateRec);
    }
    return res.status(204).json({ message: 'Updates not found in this year' });
  } catch (error) {
    console.log(error.message);
    return res.status(500).json({ message: 'Error quering countries' });
  }
};

exports.getHealth = (req, res, next) => {
  res.status(200).json({ message: 'OK' });
};
