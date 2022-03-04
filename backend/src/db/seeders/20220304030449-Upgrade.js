'use strict';

module.exports = {
  up: (queryInterface, Sequelize) =>
    queryInterface.bulkInsert(
      'Upgrades',
      [
        {
          date_value: new Date(2022, 1, 1),
          records: 10,
          createdAt: new Date(),
          updatedAt: new Date(),
        },
      ],
      {}
    ),

  down: (queryInterface, Sequelize) =>
    queryInterface.bulkDelete('Upgrades', null, {}),
};
