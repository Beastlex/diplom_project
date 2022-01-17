resource "azurerm_postgresql_server" "pgs-alzver-proj" {
  name                = "pgs-${var.postfix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name

  sku_name = "GP_Gen5_2"

  storage_profile {
    storage_mb            = 5120
    backup_retention_days = 7
    geo_redundant_backup  = "Disable"
  }

  administration_login          = var.pglogin
  administartion_password       = var.pgpasswd
  version                       = "9.5"
  ssl_enforcement               = "Enabled"
  public_network_access_enabled = false
}

resource "azurerm_postgresql_database" "pgdb-alzver-proj" {
  name                = var.dbname
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  server_name         = azurerm_postgresql_server.pgs-alzver-proj.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}
