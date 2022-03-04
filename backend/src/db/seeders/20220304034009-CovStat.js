'use strict';

module.exports = {
  up: (queryInterface, Sequelize) =>
    queryInterface.bulkInsert(
      'CovStats',
      [
        {
          date_value: new Date(2022, 0, 1),
          country_code: 'RUS',
          confirmed: 10340011,
          deaths: 303496,
          stringency_actual: 54.17,
          stringency: 54.17,
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          date_value: new Date(2022, 0, 2),
          country_code: 'RUS',
          confirmed: 10358099,
          deaths: 304284,
          stringency_actual: 54.17,
          stringency: 54.17,
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          date_value: new Date(2022, 0, 3),
          country_code: 'RUS',
          confirmed: 10374292,
          deaths: 305096,
          stringency_actual: 54.17,
          stringency: 54.17,
          createdAt: new Date(),
          updatedAt: new Date(),
        },
      ],
      {}
    ),

  down: (queryInterface, Sequelize) =>
    queryInterface.bulkDelete('CovStats', null, {}),
};
