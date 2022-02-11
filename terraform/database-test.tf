resource "azurerm_postgresql_server" "pgs-alzver-proj-test" {
  name                = "pgs-${var.postfix}-test"
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

resource "azurerm_postgresql_database" "pgdb-alzver-proj-test" {
  name                = var.dbname
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  server_name         = azurerm_postgresql_server.pgs-alzver-proj-test.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}

resource "azurerm_private_endpoint" "pendp-alzver-proj-test" {
  name                = "pendp-alzver-proj-test"
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  location            = var.location
  subnet_id           = azurerm_subnet.subnet-aks.id

  private_service_connection {
    name                           = "pendp-pgs-alzver-proj-test"
    private_connection_resource_id = azurerm_postgresql_server.pgs-alzver-proj-test.id
    subresource_names              = ["postgresqlServer"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name = "dns-grp-alzver-proj"
    private_dns_zone_ids = [ azurerm_private_dns_zone.pdns-zone-alzver-proj.id ]
  }
}

