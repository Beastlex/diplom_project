'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Upgrade extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  Upgrade.init({
    date_value: DataTypes.DATE,
    records: DataTypes.INTEGER
  }, {
    sequelize,
    modelName: 'Upgrade',
  });
  return Upgrade;
};