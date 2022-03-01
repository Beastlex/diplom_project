const models = require('../db/models');
const Sequelize = require('sequelize');

exports.getCountries = (req, res, next) => {
  try {
    const countries = await models.CovStat.findAll({
      attributes: [
        Sequelize.fn('DISTINCT', Sequelize.col('country_code')),
        'country_code',
      ],
    });
    if (countries.length === 0) {
      res.status(204).json({ message: 'There is no country list' });
    }
    res.status(200).json(countries.map((cnt) => cnt.country_code));
  } catch (error) {
    return res.status;
  }
};

exports.postStat = (req, res, next) => {
  const startDate = req.body.startDate;
  const endDate = req.body.endDate;
  const countryCode = req.body.countryCode;
  res
    .status(200)
    .json({ message: `${countryCode} => ${startDate} - ${endDate}` });
};
