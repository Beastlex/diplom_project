'use strict';
module.exports = {
  async up(queryInterface, Sequelize) {
    await queryInterface.createTable('CovStats', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      date_value: {
        type: Sequelize.DATE
      },
      country_code: {
        type: Sequelize.STRING(3)
      },
      confirmed: {
        type: Sequelize.INTEGER
      },
      deaths: {
        type: Sequelize.INTEGER
      },
      stringency_actual: {
        type: Sequelize.DECIMAL(10, 2)
      },
      stringency: {
        type: Sequelize.DECIMAL(10, 2)
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  async down(queryInterface, Sequelize) {
    await queryInterface.dropTable('CovStats');
  }
};