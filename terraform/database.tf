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

resource "azurerm_private_endpoint" "pendp-alzver-proj" {
  name                = "pendp-alzver-proj"
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  location            = var.location
  subnet_id           = azurerm_subnet.subnet-aks.id

  private_service_connection {
    name                           = "pendp-pgs-alzver-proj"
    private_connection_resource_id = azurerm_postgresql_server.pgs-alzver-proj.id
    subresource_names              = ["postgresqlServer"]
    is_manual_connection           = false
  }

  private_dns_zone_group {
    name = "dns-grp-alzver-proj"
    private_dns_zone_ids = [ azurerm_private_dns_zone.pdns-zone-alzver-proj.id ]
  }
}

resource "azurerm_private_dns_zone" "pdns-zone-alzver-proj" {
  name                = "privatelink.postgres.database.azure.com"
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
}

resource "azurerm_private_dns_zone_virtual_network_link" "example" {
  name                  = "dnslink-${var.postfix}"
  resource_group_name   = azurerm_resource_group.rg-alzver-proj.name
  private_dns_zone_name = azurerm_private_dns_zone.pdns-zone-alzver-proj.name
  virtual_network_id    = azurerm_virtual_network.vnet-alzver-proj.id
  registration_enabled  = false
}
