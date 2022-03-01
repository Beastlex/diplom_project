const models = require('../db/models');
const Sequelize = require('sequelize');

exports.getCountries = async (req, res, next) => {
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
    console.log(error.message);
    return res.status(500).json({ message: 'Error quering countries' });
  }
};

exports.postStat = async (req, res, next) => {
  const countryCode = req.body.country;
  const sortField = req.body.sort_field === 'deaths' ? 'deaths' : 'date_value';
  const year = new Date().getFullYear();
  try {
    const stats = await models.CovStat.findAll({
      order: [sortField],
      where: {
        $and: [
          Sequelize.where(
            Sequelize.fn('YEAR', Sequelize.col('date_value')),
            year
          ),
          { country_code: countryCode },
        ],
      },
    });
    res.status(200).json({ statistics: stats });
  } catch (error) {
    console.log(error.message);
    return res.status(500).json({ message: 'Error quering statistics' });
  }
  res
    .status(200)
    .json({ message: `${countryCode} => ${startDate} - ${endDate}` });
};
