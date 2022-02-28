'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class CovStat extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  CovStat.init({
    date_value: DataTypes.DATE,
    country_code: DataTypes.STRING(3),
    confirmed: DataTypes.INTEGER,
    deaths: DataTypes.INTEGER,
    stringency_actual: DataTypes.DECIMAL(10, 2),
    stringency: DataTypes.DECIMAL(10, 2)
  }, {
    sequelize,
    modelName: 'CovStat',
  });
  return CovStat;
};