resource "azurerm_virtual_network" "vnet-alzver-proj" {
  name                = "vnet-${var.postfix}"
  location            = var.location
  resource_group_name = azurerm_resource_group.rg-alzver-proj.name
  address_space       = ["10.0.0.0/16"]

  subnet {
    name           = "subnet-gw"
    address_prefix = "10.0.1.0/24"
  }

  subnet {
    name              = "subnet-db"
    address_prefix    = "10.0.2.0/24"
    service_endpoints = ["Microsoft.Sql"]
  }

  subnet {
    name           = "subnet-aks"
    address_prefix = "10.0.3.0/24"
  }

  tags = {
    owner = var.owner
  }
}

