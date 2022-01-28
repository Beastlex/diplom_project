resource "azurerm_postgresql_server" "pgs-alzver-proj" {
  name                = "pgs-${var.postfix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name

  sku_name = "GP_Gen5_2"

  storage_profile {
    storage_mb            = 5120
    backup_retention_days = 7
    geo_redundant_backup  = "Disabled"
  }

  administrator_login               = var.pglogin
  administrator_login_password      = trimspace(file(var.pgpasswd))
  version                           = "11"
  ssl_enforcement                   = "Enabled"
  infrastructure_encryption_enabled = false
  public_network_access_enabled     = false

  tags = {
    owner = var.owner
  }
}

resource "azurerm_postgresql_database" "pgdb-alzver-proj" {
  name                = var.dbname
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  server_name         = azurerm_postgresql_server.pgs-alzver-proj.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}

resource "azurerm_private_endpoint" "endpdb-azlver-proj" {
  name                = "endpdb-alzver-proj"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  subnet_id           = azurerm_subnet.subnet-db.id

  private_service_connection {
    name                           = "endpdb-alzver-proj-ps"
    private_connection_resource_id = azurerm_postgresql_server.pgs-alzver-proj.id
    subresource_names              = ["postgresqlServer"]
    is_manual_connection           = false
  }
}
